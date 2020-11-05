from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier

class CasesByGender(PowerBiQuerier):
    name = 'V_Combined_data'
    property = 'Gender'
    source = 'v'

    def _parse_data(self, response_json: Dict[str, List]) -> Dict[str, int]:
        results = super()._parse_data(response_json)
        data_pairs = filter(lambda result: len(result) == 2, results)
        label_to_skip = 'D'  # For some reason, there is a 'D' mixed in with genders
        return { gender.lower(): count for gender, count in data_pairs if gender != label_to_skip }

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
