from typing import Dict, List
from .power_bi_querier import PowerBiQuerier

class CasesByAge(PowerBiQuerier):
    name = 'cases_by_age'
    property = 'age_cat'
    source = 'c1'

    def _parse_data(self, response_json: Dict[str, List]) -> List[Dict[str, int]]:
        results = super()._parse_data(response_json)
        return [ { 'group': group, 'raw_count': count } for group, count in results ]
