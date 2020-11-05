from datetime import datetime
from typing import Any, Dict, List
from .power_bi_querier import PowerBiQuerier

class TimeSeriesTests(PowerBiQuerier):
    function = 'Sum'
    model_id = 275728
    name = 'lab_cases_by_date'
    powerbi_resource_key = '1b96a93b-9500-44cf-a3ce-942805b455ce'
    property = 'lab_collection_date'
    source = 'l'

    @staticmethod
    def postprocess_data(data_pairs: List[List]) -> List[Dict[str, Any]]:
        results = [
            {
                'date': TimeSeriesTests._timestamp_to_date(timestamp),
                'tests': positive + negative + pending,
                'positive': positive,
                'negative': negative,
                'pending': pending
            } for timestamp, positive, pending, negative in data_pairs
        ]
        TimeSeriesTests._add_cumulative_data(results)
        return results

    @staticmethod
    def _timestamp_to_date(timestamp_in_milliseconds: int) -> str:
        return datetime.utcfromtimestamp(timestamp_in_milliseconds / 1000).strftime('%Y-%m-%d')

    @staticmethod
    def _add_cumulative_data(results: List[Dict[str, Any]]) -> None:
        running_totals = { 'cumul_tests': 0, 'cumul_pos': 0, 'cumul_neg': 0, 'cumul_pend': 0 }
        for result in results:
            running_totals['cumul_tests'] += result['tests']
            running_totals['cumul_pos'] += result['positive']
            running_totals['cumul_neg'] += result['negative']
            running_totals['cumul_pend'] += result['pending']
            result.update(running_totals)

    def _select(self) -> List[Dict[str, Any]]:
        return [
            {
                'Column': self._column_expression(self.property),
                'Name': f'{self.name}.{self.property}'
            },
            self._aggregation('positive_per_day'),
            self._aggregation('unknown_per_day'),
            self._aggregation('negative_per_day')
       ]

    @staticmethod
    def _binding() -> Dict[str, Any]:
        return {
            'Primary': { 'Groupings': [{ 'Projections': [0, 1, 2, 3] }] },
            'DataReduction': {
                'DataVolume': 4,
                'Primary': { 'Sample': {} }
            },
            'Version': 1
        }
