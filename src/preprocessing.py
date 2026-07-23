import pandas as pd


def remove_missing_customer_ids(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows where Customer ID is missing.
    """
    return df.dropna(subset=["Customer ID"])


def remove_non_positive_prices(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows where Price is less than or equal to zero.
    """
    return df[df["Price"] > 0]


def remove_non_positive_quantities(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows where Quantity is less than or equal to zero.
    """
    return df[df["Quantity"] > 0]


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates()


def clean_data(df: pd.DataFrame):
    """
    Clean the dataset and return:
    1. Cleaned DataFrame
    2. Cleaning summary DataFrame
    """

    summary = []

    original_rows = len(df)

    summary.append({
        "Step": "Original Dataset",
        "Rows Remaining": original_rows,
        "Rows Removed in Step": 0
    })

    steps = [
        ("Removed Missing Customer IDs", remove_missing_customer_ids),
        ("Removed Non-Positive Prices", remove_non_positive_prices),
        ("Removed Non-Positive Quantities", remove_non_positive_quantities),
        ("Removed Duplicate Rows", remove_duplicates)
    ]

    for step_name, function in steps:

        before = len(df)

        df = function(df)

        after = len(df)

        summary.append({
            "Step": step_name,
            "Rows Remaining": after,
            "Rows Removed in Step": before - after
        })

    cleaning_summary = pd.DataFrame(summary)

    return df, cleaning_summary