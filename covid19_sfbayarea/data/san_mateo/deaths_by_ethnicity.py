from typing import Dict, List
from .power_bi_querier import PowerBiQuerier

class DeathsByEthnicity(PowerBiQuerier):
    name = 'deaths by race'
    property = 'race'
    source = 'd'

    def _parse_data(self, response_json: Dict[str, List]) -> Dict[str, int]:
        results = super()._parse_data(response_json)
        return { ethnicity.strip(): count for ethnicity, count in results }
