from .power_bi_querier import PowerBiQuerier
from covid19_sfbayarea.data.power_bi.post_processing import postprocess_counts_by_gender

class CasesByGender(PowerBiQuerier):
    name = 'cases_by_sex'
    property = 'sex'
    postprocess_data = postprocess_counts_by_gender
    source = 'c1'
