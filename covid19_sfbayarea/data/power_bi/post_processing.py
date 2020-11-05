from typing import Dict, List

@staticmethod
def postprocess_counts_by_age(data_pairs: List[List]) -> List[Dict[str, int]]:
    return [ { 'group': group, 'raw_count': count } for group, count in data_pairs ]

@staticmethod
def postprocess_counts_by_gender(data_pairs: List[List]) -> List[Dict[str, int]]:
    return { gender.lower(): count for gender, count in data_pairs }

@staticmethod
def postprocess_counts_by_ethnicity(data_pairs: List[List]) -> List[Dict[str, int]]:
    return { ethnicity.strip(): count for ethnicity, count in data_pairs }
