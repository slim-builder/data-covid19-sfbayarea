from .power_bi_querier import PowerBiQuerier
from covid19_sfbayarea.data.power_bi.post_processing import postprocess_counts_by_age

class CasesByAge(PowerBiQuerier):
    name = 'cases_by_age'
    property = 'age_cat'
    postprocess_data = postprocess_counts_by_age
    source = 'c1'
