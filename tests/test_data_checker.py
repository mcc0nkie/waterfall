import pandas as pd
from data_checker import DataChecker
from data_checker.checks import check_1

def test_data_checker():
    df = pd.DataFrame({'user_id': [1, 2, 3], 'status_1': ['Y', 'N', 'Y']})
    checker = DataChecker(df, 'user_id')
    checker.add_check(check_1, 'Check if status_1 equals Y', 'CHECK_1')
    checker.apply_checks()
    assert 'CHECK_1' in checker.dataframe.columns
    assert checker.dataframe['CHECK_1'].equals(pd.Series([True, False, True]))

