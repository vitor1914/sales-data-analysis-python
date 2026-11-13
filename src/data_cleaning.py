import pandas as pd

from src.config import REQUIRED_COLUMNS


def clean_data(df):
    """Validate and clean the sales dataset."""

    if df.empty:
        raise ValueError("The dataset is empty.")

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    df = df.copy()
    initial_rows = len(df)

    df = df.drop_duplicates()

    text_columns = [
        "order_id", "product", "category", "region", "sales_rep"
    ]

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(
        df["unit_price"], errors="coerce"
    )

    df = df.dropna(subset=REQUIRED_COLUMNS)

    df = df[
        (df["order_id"] != "")
        & (df["product"] != "")
        & (df["category"] != "")
        & (df["region"] != "")
        & (df["sales_rep"] != "")
        & (df["quantity"] > 0)
        & (df["unit_price"] >= 0)
        & (df["quantity"] % 1 == 0)
    ].copy()

    if df.empty:
        raise ValueError("No valid records remain after cleaning.")

    df["quantity"] = df["quantity"].astype(int)
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["month"] = df["date"].dt.to_period("M").astype(str)

    print(f"Initial records: {initial_rows}")
    print(f"Valid records: {len(df)}")
    print(f"Removed records: {initial_rows - len(df)}")

    return df
