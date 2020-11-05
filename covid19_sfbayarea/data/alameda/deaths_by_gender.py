from typing import Any, Dict, List

from .power_bi_querier import PowerBiQuerier

class DeathsByGender(PowerBiQuerier):
    name = 'V_Combined_data'
    property = 'Gender'
    source = 'v'

    def postprocess_data(self, data_pairs: List[list]) -> Dict[str, int]:
        return { gender.lower(): count for gender, count in data_pairs }

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
