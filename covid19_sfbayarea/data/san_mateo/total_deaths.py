from typing import Any, Dict, List, cast
from .power_bi_querier import PowerBiQuerier
from covid19_sfbayarea.utils import dig

class TotalDeaths(PowerBiQuerier):
    json_path = PowerBiQuerier.DEFAULT_JSON_PATH +  [0, 'M0']
    function = 'Sum'
    name = 'deaths by race'
    property = 'n'
    source = 'd1'

    def _parse_data(self, response_json: Dict[str, List]) -> int: # type: ignore
        return cast(int, dig(response_json, self.json_path))

    def _select(self) -> List[Dict[str, Any]]:
        return [self._aggregation('n')]

    def _binding(self) -> Dict[str, Any]:
        return {
            'Primary': { 'Groupings': [{ 'Projections': [0] }] },
            'DataReduction': {
                'DataVolume': 3,
                'Primary': { 'Top': {} }
            },
            'Version': 1
        }
