from typing import Dict, List
from .power_bi_querier import PowerBiQuerier

class DeathsByAge(PowerBiQuerier):
    name = 'deaths by age'
    property = 'age_cat'
    source = 'd1'

    def postprocess_data(self, data_pairs: List[list]) -> List[Dict[str, int]]:
        return [ { 'group': group, 'raw_count': count } for group, count in data_pairs ]
