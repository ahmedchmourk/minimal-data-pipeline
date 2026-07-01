# Minimal Data Pipeline

A clean, premium, and minimalist Python-based utility designed for streamlined data preprocessing, feature scaling, and anomaly detection.

## Features

- **Minimalist Design**: Zero external dependencies (uses pure Python standard library).
- **Streamlined Preprocessing**: Built-in functions for scaling (MinMax, Standard), handling missing values, and filtering anomalies.
- **AI-Agent Ready**: Modular, type-hinted utility functions structured to be easily integrated with LLM or RAG workflows.

## Installation

```bash
git clone https://github.com/ahmedchmourk/minimal-data-pipeline.git
cd minimal-data-pipeline
```

## Quick Start

```python
from pipeline import DataPipeline

# Initialize pipeline
pipeline = DataPipeline()

# Sample dataset with missing values
raw_data = [1.0, None, 3.0, 10.0, float('nan')]

# Impute missing values
clean_data = pipeline.impute_missing(raw_data, strategy="mean")

# Scale features to [0, 1] range
scaled_data = pipeline.min_max_scale(clean_data)

# Standardize features (mean=0, variance=1)
standardized_data = pipeline.standardize(clean_data)
```

## Running Tests

To verify the pipeline logic, execute the script directly using Python:

```bash
python pipeline.py
```




