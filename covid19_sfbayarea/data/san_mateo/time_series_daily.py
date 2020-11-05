from typing import Dict, List

from .power_bi_querier import PowerBiQuerier

class TimeSeriesDaily(PowerBiQuerier):
    name = 'cases_by_day'
    property = 'date_result'
    source = 'c'

    def postprocess_data(self, data_pairs: List[list]) -> Dict[str, int]:
        return { timestamp: cases for timestamp, cases in data_pairs }
