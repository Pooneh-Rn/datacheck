
# DataCheck

A lightweight Python toolkit for automated tabular
data quality analysis, validation, and reporting.

## Overview

DataCheck aims to help data scientists and data
engineers identify common data-quality problems
before using datasets in downstream applications.

## Features

- CSV dataset loading
- Dataset profiling
- Missing-value detection
- Duplicate detection
- Statistical outlier detection
- Schema validation
- Data consistency checks
- Quality scoring
- Automated HTML and JSON reports

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/datacheck.git
cd datacheck
```

Create a virtual environment and install:

```bash
python -m venv .venv
pip install -e ".[dev]"
```

## Usage

```bash
datacheck analyze data/customers.csv
```

## Development status

Currently under development.

### Roadmap

- [x] Project structure
- [x] CSV loading
- [ ] Dataset profiling
- [ ] Missing-value detection
- [ ] Duplicate detection
- [ ] Outlier detection
- [ ] Schema validation
- [ ] Quality scoring
- [ ] HTML reports
- [ ] JSON reports

## Tech stack

- Python
- Pandas
- NumPy
- Typer
- Pytest
- Scikit-learn

## License

MIT