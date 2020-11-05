from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier
from .util import parse_ethnicity_data

class CasesByEthnicity(PowerBiQuerier):
    name = 'V_RaceEth_Rates'
    property = 'RaceEth'
    source = 'v'
    # We have to override this method instead because we need the ethnicity labels
    _parse_data = parse_ethnicity_data

    def _select(self) -> List[Dict[str, Any]]:
        return [
            {
                'Column': self._column_expression(self.property),
                'Name': f'{self.name}.{self.property}'
            },
            self._aggregation('Cases')
       ]
