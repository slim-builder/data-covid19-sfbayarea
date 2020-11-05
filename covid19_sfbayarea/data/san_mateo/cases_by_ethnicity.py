from typing import Dict, List
from .power_bi_querier import PowerBiQuerier

class CasesByEthnicity(PowerBiQuerier):
    name = 'cases_by_race'
    property = 'race_cat'
    source = 'c'

    def postprocess_data(self, data_pairs: List[list]) -> Dict[str, int]:
        return { ethnicity.strip(): count for ethnicity, count in data_pairs }
