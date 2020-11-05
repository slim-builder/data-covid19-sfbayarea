from typing import Dict, List
from .power_bi_querier import PowerBiQuerier

class CasesByGender(PowerBiQuerier):
    name = 'cases_by_sex'
    property = 'sex'
    source = 'c1'

    def _parse_data(self, response_json: Dict[str, List]) -> Dict[str, int]:
        results = super()._parse_data(response_json)
        return { gender.lower(): count for gender, count in results }
