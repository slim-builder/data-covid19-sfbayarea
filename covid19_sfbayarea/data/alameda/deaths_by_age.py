from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier

class DeathsByAge(PowerBiQuerier):
    name = 'V_Combined_data'
    property = 'AgeGroup'
    source = 'v'

    def _parse_data(self, response_json: Dict[str, List]) -> List[Dict[str, int]]:
        results = super()._parse_data(response_json)
        return [ { 'group': group, 'raw_count': count } for group, count in results ]

    def _select(self) -> List[Dict[str, Any]]:
        property = 'NumberOfDeaths'
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
