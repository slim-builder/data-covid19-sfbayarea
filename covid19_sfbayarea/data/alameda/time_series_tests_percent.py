from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier

class TimeSeriesTestsPercent(PowerBiQuerier):
    function = 'Sum'
    model_id = 296535
    name = 'V_Tests_RollingSevenDayPercentagePositive'
    powerbi_resource_key = '032423d3-f7a4-473b-b50c-bf5518918335'
    property = 'Date'
    source = 'v'

    def _select(self) -> List[Dict[str, Any]]:
        return [
            {
                'Column': self._column_expression(self.property),
                'Name': f'{self.name}.{self.property}'
            },
            self._aggregation('RollingSevenDayPercentagePositiveTests')
       ]

    @staticmethod
    def _binding() -> Dict[str, Any]:
        return {
            'Primary': { 'Groupings': [{ 'Projections': [0, 1] }] },
            'DataReduction': {
                'DataVolume': 4,
                'Primary': { 'BinnedLineSample': {} }
            },
            'Version': 1
        }
