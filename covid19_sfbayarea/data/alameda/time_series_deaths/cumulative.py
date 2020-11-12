from typing import Any, Dict, List
from ..power_bi_querier import PowerBiQuerier

class Cumulative(PowerBiQuerier):
    name = 'V_Combined_data'
    property = 'DtDeath'
    source = 'v'

    def _select(self) -> List[Dict[str, Any]]:
        measure = 'Cumulative Deaths'
        return [
            {
                'Column': self._column_expression(self.property),
                'Name': f'{self.name}.{self.property}'
            },
            {
                'Measure': {
                    **self._column_expression(self.property),
                    'Property': measure
                },
                'Name': f'{self.name}.{measure}'
            }
        ]

    def _binding(self) -> Dict[str, Any]:
        return {
            'DataReduction': {
                'DataVolume': 4,
                'Primary': { 'BinnedLineSample': {} }
            },
            'Primary': {
                'Groupings': [{'Projections': [0, 1] }]
            },
            'Version': 1
        }
