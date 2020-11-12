from typing import Any, Dict, List
from ..power_bi_querier import PowerBiQuerier

class Daily(PowerBiQuerier):
    name = 'V_Combined_data'
    property = 'DtCreate'
    source = 'v'

    def _parse_data(self, response_json: Dict) -> Dict[int, int]:
        return dict(super()._parse_data(response_json))

    def _select(self) -> List[Dict[str, Any]]:
        measure = 'NumberOfCases'
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
