from typing import Dict, List

from .power_bi_querier import PowerBiQuerier

class DeathsByGender(PowerBiQuerier):
    name = 'death by sex'
    property = 'sex'
    source = 'd1'

    def postprocess_data(self, data_pairs: List[list]) -> Dict[str, int]:
        return { gender.lower(): count for gender, count in data_pairs }
