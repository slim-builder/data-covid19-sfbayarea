from typing import Dict, List
from covid19_sfbayarea.utils import dig

def parse_ethnicity_data(self, response_json: Dict[str, List]) -> Dict[str, int]:
    results = super()._parse_data(response_json)
    ethnicity_labels = dig(response_json, self.json_path[0:-3] + ['ValueDicts', 'D0'])
    totals = {'Overall', 'Overall Known Race/Ethnicity'}
    return {
        ethnicity_label: count
        for ethnicity_label_index, count in results.items()
        if (ethnicity_label := ethnicity_labels[ethnicity_label_index].strip()) not in totals
    }
