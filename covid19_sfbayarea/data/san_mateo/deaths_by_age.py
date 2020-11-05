from typing import Dict, List
from .power_bi_querier import PowerBiQuerier

class DeathsByAge(PowerBiQuerier):
    name = 'deaths by age'
    property = 'age_cat'
    source = 'd1'

    def _parse_data(self, response_json: Dict[str, List]) -> List[Dict[str, int]]:
        results = super()._parse_data(response_json)
        return [ { 'group': group, 'raw_count': count } for group, count in results ]
