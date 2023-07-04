import pandas as pd
from typing import Callable, List, Tuple

class DataChecker:
    def __init__(self, dataframe: pd.DataFrame, user_id_col: str):
        """
        Initializes a new instance of DataChecker.

        Parameters:
        dataframe (DataFrame): The input data.
        user_id_col (str): The column to use as the user ID.
        """
        if dataframe[user_id_col].is_unique:
            self.dataframe = dataframe.copy()
            self.user_id_col = user_id_col
        else:
            raise ValueError('user_id_col must be unique')

        # The list of checks to apply. Each check is a tuple of (function, description, code).
        self.checks: List[Tuple[Callable[[pd.DataFrame], pd.Series], str, str]] = []

    def add_check(self, check_func: Callable[[pd.DataFrame], pd.Series], description: str, code: str):
        """
        Adds a check to the list of checks to apply.

        Parameters:
        check_func (function): The check function.
        description (str): The check description.
        code (str): The check code.
        """
        # Verify that check_func is a function
        if not callable(check_func):
            raise ValueError('check_func must be a function')

        self.checks.append((check_func, description, code))

    def apply_checks(self):
        """
        Applies all checks to the dataframe.
        """
        for check_func, description, code in self.checks:
            self.dataframe[code] = check_func(self.dataframe)

