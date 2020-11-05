from typing import Dict, List
from .power_bi_querier import PowerBiQuerier

class DeathsByEthnicity(PowerBiQuerier):
    name = 'deaths by race'
    property = 'race'
    source = 'd'

    def postprocess_data(self, data_pairs: List[list]) -> Dict[str, int]:
        return { ethnicity.strip(): count for ethnicity, count in data_pairs }
