from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier
from covid19_sfbayarea.data.power_bi.post_processing import postprocess_counts_by_gender

class DeathsByGender(PowerBiQuerier):
    name = 'V_Combined_data'
    property = 'Gender'
    postprocess_data = postprocess_counts_by_gender
    source = 'v'

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
