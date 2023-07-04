Sure, here's a simple outline for the library structure and a draft README file:

File Structure:
```
- data_checker/
  - __init__.py
  - data_checker.py
  - checks.py
  - report.py
- tests/
  - __init__.py
  - test_data_checker.py
- README.md
- setup.py
```

File Descriptions:
- `data_checker/__init__.py`: Initializes the data_checker package.
- `data_checker/data_checker.py`: Contains the `DataChecker` class which manages the dataset, applies the checks, and generates the report.
- `data_checker/checks.py`: Contains predefined check functions that can be used as-is or as examples to define new checks.
- `data_checker/report.py`: Contains functions for generating the report based on the results of the checks.
- `tests/__init__.py`: Initializes the tests package.
- `tests/test_data_checker.py`: Contains unit tests for the `DataChecker` class and other parts of the library.
- `README.md`: The file you are reading now. Explains what the library does and how to use it.
- `setup.py`: Used to install the library. Defines dependencies, version number, and other metadata.

README Draft:

# DataChecker

DataChecker is a Python library that allows you to apply a series of checks to a dataset and generate a report that summarizes the impact of each check.

## Installation

You can install DataChecker with pip:

```
pip install data_checker
```

## Usage

First, import the `DataChecker` class and the check functions you want to use:

```python
from data_checker import DataChecker
from data_checker.checks import check_1, check_2
```

Next, load your dataset into a pandas DataFrame and create a `DataChecker` instance:

```python
import pandas as pd

df = pd.read_csv('my_data.csv')
checker = DataChecker(df, 'user_id')
```

Add the checks you want to apply:

```python
checker.add_check(check_1, 'Check 1 description', 'CHECK_1')
checker.add_check(check_2, 'Check 2 description', 'CHECK_2')
```

Apply the checks and generate the report:

```python
checker.apply_checks()
report = checker.generate_report()
```

## Defining Custom Checks

You can define your own checks by writing Python functions that take a DataFrame as input and return a boolean Series. Here's an example:

```python
def my_check(df):
    return df['my_column'] > 100
```

You can then add your custom check to the `DataChecker` instance just like the predefined checks:

```python
checker.add_check(my_check, 'My check description', 'MY_CHECK')
```

## Generating the Report

The `generate_report()` method returns a DataFrame that summarizes the impact of each check. This includes the number of records dropped by each check, the incremental and cumulative record drops, and the number of records remaining after each check.

## Testing

Unit tests are provided in the `tests/` directory. You can run them using your preferred test runner.

## Contributing

Pull requests are welcome. Please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

