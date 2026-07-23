from pathlib import Path
import pandas as pd


def load_excel(filepath: Path, sheet_name=0) -> pd.DataFrame:
    """
    Load a specific sheet from an Excel file.
    """
    return pd.read_excel(filepath, sheet_name=sheet_name)


def load_online_retail_dataset(filepath: Path) -> pd.DataFrame:
    """
    Load the Online Retail dataset by merging both yearly sheets.
    """

    sheet_2009 = pd.read_excel(
        filepath,
        sheet_name="Year 2009-2010"
    )

    sheet_2010 = pd.read_excel(
        filepath,
        sheet_name="Year 2010-2011"
    )

    df = pd.concat(
        [sheet_2009, sheet_2010],
        ignore_index=True
    )

    return df