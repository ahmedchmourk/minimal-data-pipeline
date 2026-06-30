import math
from typing import List, Dict, Union, Optional

class DataPipeline:
    """
    A minimalist, pure-Python data preprocessing utility.
    No external dependencies required.
    """
    
    def __init__(self):
        pass
        
    def impute_missing(self, data: List[Optional[float]], strategy: str = "mean") -> List[float]:
        """
        Imputes missing values (None/NaN) using mean or median strategy.
        """
        valid_vals = [x for x in data if x is not None and not math.isnan(x)]
        if not valid_vals:
            return [0.0] * len(data)
            
        if strategy == "mean":
            fill_value = sum(valid_vals) / len(valid_vals)
        elif strategy == "median":
            sorted_vals = sorted(valid_vals)
            n = len(sorted_vals)
            if n % 2 == 1:
                fill_value = sorted_vals[n // 2]
            else:
                fill_value = (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2.0
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
            
        return [x if (x is not None and not math.isnan(x)) else fill_value for x in data]

    def min_max_scale(self, data: List[float]) -> List[float]:
        """
        Scales features to a [0, 1] range.
        """
        if not data:
            return []
        min_val = min(data)
        max_val = max(data)
        diff = max_val - min_val
        if diff == 0:
            return [0.0] * len(data)
        return [(x - min_val) / diff for x in data]

    def standardize(self, data: List[float]) -> List[float]:
        """
        Standardizes features by removing the mean and scaling to unit variance.
        """
        if not data:
            return []
        n = len(data)
        mean = sum(data) / n
        variance = sum((x - mean) ** 2 for x in data) / n
        std_dev = math.sqrt(variance)
        if std_dev == 0:
            return [0.0] * n
        return [(x - mean) / std_dev for x in data]


if __name__ == "__main__":
    # Quick sanity check
    pipeline = DataPipeline()
    raw_data = [1.0, None, 3.0, 10.0, float('nan')]
    clean_data = pipeline.impute_missing(raw_data, strategy="mean")
    scaled_data = pipeline.min_max_scale(clean_data)
    standardized_data = pipeline.standardize(clean_data)
    print(f"Original:     {raw_data}")
    print(f"Imputed:      {clean_data}")
    print(f"Scaled:       {scaled_data}")
    print(f"Standardized: {standardized_data}")
