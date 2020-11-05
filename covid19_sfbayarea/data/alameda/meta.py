from .power_bi_querier import PowerBiQuerier
from ..power_bi.fetch_meta import FetchMeta

class Meta(FetchMeta):
    powerbi_resource_key = PowerBiQuerier.powerbi_resource_key

    def get_data(self) -> str:
        return super().get_data()[2:] # The first two characters are ': '
