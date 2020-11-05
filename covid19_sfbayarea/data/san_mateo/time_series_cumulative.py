from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier

class TimeSeriesCumulative(PowerBiQuerier):
    name = 'cases_by_day'
    property = 'date_result'
    source = 'c'

    def _select(self) -> List[Dict[str, Any]]:
        measure = f'Sum of n running total in {self.property}'
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

    @staticmethod
    def _binding() -> Dict[str, Any]:
        return {
            'DataReduction': {
                'DataVolume': 4,
                'Primary': { 'Sample': {} }
            },
            'Primary': {
                'Groupings': [{'Projections': [0, 1] }]
            },
            'Version': 1
        }
