from typing import Dict, List
from .power_bi_querier import PowerBiQuerier

class CasesByAge(PowerBiQuerier):
    name = 'cases_by_age'
    property = 'age_cat'
    source = 'c1'

    def postprocess_data(self, data_pairs: List[list]) -> List[Dict[str, int]]:
        return [ { 'group': group, 'raw_count': count } for group, count in data_pairs ]
