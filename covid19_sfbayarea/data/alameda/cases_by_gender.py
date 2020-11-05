from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier
from covid19_sfbayarea.data.power_bi.post_processing import postprocess_counts_by_gender

class CasesByGender(PowerBiQuerier):
    name = 'V_Combined_data'
    postprocess_counts_by_gender = postprocess_counts_by_gender
    property = 'Gender'
    source = 'v'

    @staticmethod
    def postprocess_data(data_pairs: List[list]) -> Dict[str, int]:
        label_to_skip = 'D'  # For some reason, there is a 'D' mixed in with genders
        filtered_data_pairs = filter(lambda result: len(result) == 2 and result[0] != label_to_skip, data_pairs)
        return CasesByGender.postprocess_counts_by_gender(filtered_data_pairs)

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
