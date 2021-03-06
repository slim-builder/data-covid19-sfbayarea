import json

from datetime import datetime
from typing import Any, Dict, List, cast
from covid19_sfbayarea.utils import dig, parse_datetime

from .cases_by_age import CasesByAge
from .cases_by_ethnicity import CasesByEthnicity
from .cases_by_gender import CasesByGender

from .meta import Meta

from .deaths_by_age import DeathsByAge
from .deaths_by_ethnicity import DeathsByEthnicity
from .deaths_by_gender import DeathsByGender

from .time_series_cases import TimeSeriesCases
from .time_series_tests import TimeSeriesTests
from .total_deaths import TotalDeaths

from ..utils import get_data_model

LANDING_PAGE = 'https://www.smchealth.org/post/san-mateo-county-covid-19-data-1'

def get_county() -> Dict:
    out = get_data_model()
    out.update(fetch_data())
    return out

def fetch_data() -> Dict:
    data : Dict = {
        'name': 'San Mateo County',
        'source_url': LANDING_PAGE,
        'meta_from_source': Meta().get_data(),
        'meta_from_baypd': """
            See power_bi_scraper.py for methods.
            San Mateo does not provide a timestamp for their last dataset update,
            so BayPD uses midnight of the latest day in the cases timeseries as a proxy.

            San Mateo does not provide a deaths timeseries. In lieu of a
            timeseries BayPD provides cumulative deaths for the date of the last
            dataset update.
         """,
        'series': {
            'cases': TimeSeriesCases().get_data(),
            'tests': TimeSeriesTests().get_data()
        },
        'case_totals': {
            'gender': CasesByGender().get_data(),
            'age_group': CasesByAge().get_data(),
            'race_eth': CasesByEthnicity().get_data()
        },
        'death_totals': {
            'gender': DeathsByGender().get_data(),
            'age_group': DeathsByAge().get_data(),
            'race_eth': DeathsByEthnicity().get_data()
        }
    }
    last_updated = most_recent_case_time(data)
    data.update({ 'update_time': last_updated.isoformat() })
    data['series'].update({ 'deaths': cumulative_deaths(last_updated) })
    return data

def most_recent_case_time(data: Dict[str, Any]) -> datetime:
    most_recent_cases = cast(Dict[str, str], dig(data, ['series', 'cases', -1]))
    return parse_datetime(most_recent_cases['date'])

def cumulative_deaths(last_updated: datetime) -> List[Dict[str, Any]]:
    #  There is no timeseries, but there is a cumulative deaths for the current day.
    return [{
        'date': last_updated.strftime('%Y-%m-%d'),
        'deaths': -1,
        'cumul_deaths': TotalDeaths().get_data()
    }]

if __name__ == '__main__':
    """ When run as a script, prints the data to stdout"""
    print(json.dumps(get_county(), indent=4))
