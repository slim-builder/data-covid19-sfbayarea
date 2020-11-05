from typing import Dict, List
from .power_bi_querier import PowerBiQuerier
from covid19_sfbayarea.data.power_bi.post_processing import postprocess_counts_by_ethnicity

class CasesByEthnicity(PowerBiQuerier):
    name = 'cases_by_race'
    postprocess_data = postprocess_counts_by_ethnicity
    property = 'race_cat'
    source = 'c'
