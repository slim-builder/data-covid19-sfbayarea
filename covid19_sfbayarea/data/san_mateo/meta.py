from .power_bi_querier import PowerBiQuerier
from ..power_bi.fetch_meta import FetchMeta

class Meta(FetchMeta):
    powerbi_resource_key = PowerBiQuerier.powerbi_resource_key
