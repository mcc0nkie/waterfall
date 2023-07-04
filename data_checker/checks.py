def check_1(df):
    """
    Check if 'status_1' column equals 'Y'.
    """
    return df['status_1'] == 'Y'

def check_2(df):
    """
    Check if 'status_2' is less than 2000 and 'status_3' is in ['abc', 'asd'].
    """
    return (df['status_2'] < 2000) & df['status_3'].isin(['abc', 'asd'])

