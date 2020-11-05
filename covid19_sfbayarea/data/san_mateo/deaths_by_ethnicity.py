from typing import Dict, List
from .power_bi_querier import PowerBiQuerier
from covid19_sfbayarea.data.power_bi.post_processing import postprocess_counts_by_ethnicity

class DeathsByEthnicity(PowerBiQuerier):
    name = 'deaths by race'
    postprocess_data = postprocess_counts_by_ethnicity
    property = 'race'
    source = 'd'
