from typing import Dict

from .power_bi_querier import PowerBiQuerier

class TimeSeriesDaily(PowerBiQuerier):
    name = 'cases_by_day'
    property = 'date_result'
    source = 'c'

    def _parse_data(self, response_json: Dict) -> Dict[int, int]:
        data_pairs = super()._parse_data(response_json)
        return { timestamp: cases for timestamp, cases in data_pairs }
