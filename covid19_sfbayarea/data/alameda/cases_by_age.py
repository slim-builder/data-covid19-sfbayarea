from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier

class CasesByAge(PowerBiQuerier):
    name = 'V_Combined_data'
    property = 'AgeGroup'
    source = 'v'

    def postprocess_data(self, data_pairs: List[list]) -> List[Dict[str, int]]:
        return [ { 'group': group, 'raw_count': count } for group, count in data_pairs ]

    def _select(self) -> List[Dict[str, Any]]:
        property = 'NumberOfCases'
        return [
            {
                'Column': self._column_expression(self.property),
                'Name': f'{self.name}.{self.property}'
            },
            {
                'Measure': self._column_expression(property),
                'Name': f'{self.name}.{property}'
            },
       ]
