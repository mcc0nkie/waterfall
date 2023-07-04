import pandas as pd

def generate_report(df, checks):
    """
    Generates a report summarizing the impact of each check.

    Parameters:
    df (DataFrame): The DataFrame after applying the checks.
    checks (list): The list of checks applied.

    Returns:
    DataFrame: The report.
    """
    reports = []
    cumulative_drops = 0
    records_remaining = len(df)

    for _, description, code in checks:
        # The number of records dropped if only this check was applied.
        records_dropped_if_only_drop = len(df[df[code] == False])

        # The number of records dropped since the last check applied.
        incremental_drops = len(df) - len(df[df[code] == True])
        cumulative_drops += incremental_drops

        # The number of records that would be regained if we removed only this check.
        regain_if_no_scrub = len(df[df[code] == True]) - records_remaining
        records_remaining -= incremental_drops

        reports.append([code, description, records_dropped_if_only_drop, incremental_drops, cumulative_drops, regain_if_no_scrub, records_remaining])

    report_df = pd.DataFrame(reports, columns=['Criteria', 'Description', 'RECORDS_DROPPED_IF_ONLY_DROP', 'INCREMENTAL_RECORD_DROPS', 'CUMULATIVE_RECORD_DROPS', 'REGAIN_IF_NO_SCRUB', 'RECORDS_REMAINING'])
    return report_df

