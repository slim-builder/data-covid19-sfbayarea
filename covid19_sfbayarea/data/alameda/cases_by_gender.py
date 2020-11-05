from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier

class CasesByGender(PowerBiQuerier):
    name = 'V_Combined_data'
    property = 'Gender'
    source = 'v'

    def postprocess_data(self, data_pairs: List[list]) -> Dict[str, int]:
        label_to_skip = 'D'  # For some reason, there is a 'D' mixed in with genders
        data_pairs = filter(lambda result: len(result) == 2 and result[0] != label_to_skip, data_pairs)
        return { gender.lower(): count for gender, count in data_pairs }

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
