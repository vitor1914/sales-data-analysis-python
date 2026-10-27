
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib

# Permite gerar gráficos sem precisar abrir janelas gráficas.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# SALES DATA ANALYSIS WITH PYTHON
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
DATA_FILE = DATA_DIR / "sales.csv"

DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

REQUIRED_COLUMNS = [
    "order_id",
    "date",
    "product",
    "category",
    "quantity",
    "unit_price",
    "region",
    "sales_rep",
]


# ============================================================
# 1. CREATE SAMPLE DATA
# ============================================================

def create_sample_data():
    """Create a fictional sales dataset with 200 records."""

    rng = np.random.default_rng(42)

    products = {
        "Laptop": ("Electronics", 3500.00),
        "Mouse": ("Accessories", 80.00),
        "Keyboard": ("Accessories", 150.00),
        "Monitor": ("Electronics", 1200.00),
        "Headphones": ("Accessories", 250.00),
        "Desk": ("Furniture", 900.00),
        "Chair": ("Furniture", 650.00),
        "Webcam": ("Electronics", 300.00),
    }

    regions = ["North", "South", "East", "West"]
    sales_reps = ["Alice", "Bruno", "Carla", "Daniel"]

    records = []

    for i in range(1, 201):
        product = str(rng.choice(list(products.keys())))
        category, base_price = products[product]

        quantity = int(rng.integers(1, 8))
        unit_price = round(
            base_price * float(rng.uniform(0.90, 1.10)), 2
        )

        date = (
            pd.Timestamp("2025-01-01")
            + pd.Timedelta(days=int(rng.integers(0, 365)))
        )

        records.append({
            "order_id": f"ORD-{i:04d}",
            "date": date.strftime("%Y-%m-%d"),
            "product": product,
            "category": category,
            "quantity": quantity,
            "unit_price": unit_price,
            "region": str(rng.choice(regions)),
            "sales_rep": str(rng.choice(sales_reps)),
        })

    df = pd.DataFrame(records)
    df.to_csv(DATA_FILE, index=False)

    print(f"Sample dataset created: {DATA_FILE}")
    print(f"Sample records: {len(df)}")


# ============================================================
# 2. LOAD AND CLEAN DATA
# ============================================================

def load_data():
    """Load, validate, and clean the sales dataset."""

    # Generate sample data if the file is missing or empty.
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        create_sample_data()

    try:
        df = pd.read_csv(DATA_FILE)
    except pd.errors.EmptyDataError:
        print("Warning: the CSV file is empty. Recreating sample data.")
        create_sample_data()
        df = pd.read_csv(DATA_FILE)

    # Validate required columns.
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    initial_records = len(df)

    # Remove exact duplicate records.
    df = df.drop_duplicates().copy()

    # Convert fields to appropriate data types.
    df["date"] = pd.to_datetime(
        df["date"], errors="coerce"
    )

    df["quantity"] = pd.to_numeric(
        df["quantity"], errors="coerce"
    )

    df["unit_price"] = pd.to_numeric(
        df["unit_price"], errors="coerce"
    )

    # Remove rows with missing required values.
    df = df.dropna(subset=REQUIRED_COLUMNS).copy()

    # Remove invalid quantities and prices.
    df = df[
        (df["quantity"] > 0)
        & (df["unit_price"] >= 0)
    ].copy()

    if df.empty:
        raise ValueError(
            "No valid sales records were found. "
            "Check the contents of data/sales.csv."
        )

    # Calculate revenue and month.
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["month"] = df["date"].dt.to_period("M").astype(str)

    removed_records = initial_records - len(df)

    print("\nDATA VALIDATION")
    print("-" * 45)
    print(f"Original records: {initial_records:,}")
    print(f"Valid records:    {len(df):,}")
    print(f"Removed records:  {removed_records:,}")

    return df


# ============================================================
# 3. CALCULATE KPIs
# ============================================================

def calculate_kpis(df):
    """Calculate overall sales performance indicators."""

    total_records = len(df)
    total_orders = df["order_id"].nunique()
    total_units = df["quantity"].sum()
    total_revenue = df["revenue"].sum()

    average_order_value = (
        total_revenue / total_orders if total_orders else 0
    )

    average_unit_price = (
        total_revenue / total_units if total_units else 0
    )

    kpis = {
        "total_records": total_records,
        "total_orders": total_orders,
        "units_sold": int(total_units),
        "total_revenue": round(float(total_revenue), 2),
        "average_order_value": round(
            float(average_order_value), 2
        ),
        "average_revenue_per_unit": round(
            float(average_unit_price), 2
        ),
    }

    print("\n" + "=" * 52)
    print("              SALES ANALYSIS")
    print("=" * 52)
    print(f"Valid records:          {total_records:,}")
    print(f"Unique orders:          {total_orders:,}")
    print(f"Units sold:             {total_units:,.0f}")
    print(f"Total revenue:          R$ {total_revenue:,.2f}")
    print(f"Average order value:    R$ {average_order_value:,.2f}")
    print(f"Revenue per unit:       R$ {average_unit_price:,.2f}")
    print("=" * 52)

    pd.DataFrame([kpis]).to_csv(
        OUTPUT_DIR / "kpis.csv", index=False
    )

    return kpis


# ============================================================
# 4. GENERATE REPORTS
# ============================================================

def generate_reports(df):
    """Generate CSV reports for different sales dimensions."""

    product_report = (
        df.groupby("product", as_index=False)
        .agg(
            units_sold=("quantity", "sum"),
            total_revenue=("revenue", "sum"),
            number_of_orders=("order_id", "nunique"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    category_report = (
        df.groupby("category", as_index=False)
        .agg(
            units_sold=("quantity", "sum"),
            total_revenue=("revenue", "sum"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    region_report = (
        df.groupby("region", as_index=False)
        .agg(
            total_revenue=("revenue", "sum"),
            units_sold=("quantity", "sum"),
            number_of_orders=("order_id", "nunique"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    monthly_report = (
        df.groupby("month", as_index=False)
        .agg(
            total_revenue=("revenue", "sum"),
            units_sold=("quantity", "sum"),
            number_of_orders=("order_id", "nunique"),
        )
        .sort_values("month")
    )

    sales_rep_report = (
        df.groupby("sales_rep", as_index=False)
        .agg(
            total_revenue=("revenue", "sum"),
            units_sold=("quantity", "sum"),
            number_of_orders=("order_id", "nunique"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    reports = {
        "product_sales.csv": product_report,
        "category_sales.csv": category_report,
        "regional_sales.csv": region_report,
        "monthly_sales.csv": monthly_report,
        "sales_representatives.csv": sales_rep_report,
    }

    for filename, report in reports.items():
        report.to_csv(OUTPUT_DIR / filename, index=False)

    print("\nTOP 5 PRODUCTS BY REVENUE")
    print(product_report.head(5).to_string(index=False))

    print("\nREVENUE BY CATEGORY")
    print(category_report.to_string(index=False))

    print("\nREVENUE BY REGION")
    print(region_report.to_string(index=False))

    print("\nMONTHLY REVENUE")
    print(monthly_report.to_string(index=False))

    print("\nSALES REPRESENTATIVES")
    print(sales_rep_report.to_string(index=False))

    return (
        product_report,
        category_report,
        region_report,
        monthly_report,
        sales_rep_report,
    )


# ============================================================
# 5. GENERATE CHARTS
# ============================================================

def generate_charts(
    df,
    product_report,
    category_report,
    region_report,
    monthly_report,
):
    """Generate and save five sales charts."""

    # Chart 1: Monthly revenue.
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=monthly_report,
        x="month",
        y="total_revenue",
        marker="o",
    )

    plt.title("Monthly Revenue", fontsize=16)
    plt.xlabel("Month")
    plt.ylabel("Revenue (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "monthly_revenue.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close()

    # Chart 2: Top 10 products.
    top_products = (
        product_report.head(10)
        .sort_values("total_revenue")
    )

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=top_products,
        x="total_revenue",
        y="product",
    )

    plt.title("Top 10 Products by Revenue", fontsize=15)
    plt.xlabel("Revenue (R$)")
    plt.ylabel("Product")
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "top_products.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close()

    # Chart 3: Revenue by category.
    plt.figure(figsize=(9, 5))

    sns.barplot(
        data=category_report,
        x="category",
        y="total_revenue",
    )

    plt.title("Revenue by Category", fontsize=15)
    plt.xlabel("Category")
    plt.ylabel("Revenue (R$)")
    plt.xticks(rotation=15)
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "category_revenue.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close()

    # Chart 4: Revenue by region.
    plt.figure(figsize=(9, 5))

    sns.barplot(
        data=region_report,
        x="region",
        y="total_revenue",
    )

    plt.title("Revenue by Region", fontsize=15)
    plt.xlabel("Region")
    plt.ylabel("Revenue (R$)")
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "regional_revenue.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close()

    # Chart 5: Revenue distribution per record.
    plt.figure(figsize=(10, 5))

    sns.histplot(
        data=df,
        x="revenue",
        bins=25,
        kde=True,
    )

    plt.title("Revenue Distribution per Record", fontsize=15)
    plt.xlabel("Revenue (R$)")
    plt.ylabel("Frequency")
    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "revenue_distribution.png",
        dpi=150,
        bbox_inches="tight",
    )
    plt.close()

    print("\nCharts generated successfully.")


# ============================================================
# 6. SAVE CLEANED DATA
# ============================================================

def save_cleaned_data(df):
    """Save the cleaned dataset to CSV."""

    df.to_csv(
        OUTPUT_DIR / "cleaned_sales.csv",
        index=False,
    )

    print("Cleaned dataset saved.")


# ============================================================
# 7. MAIN
# ============================================================

def main():
    """Run the complete sales analysis pipeline."""

    print("\n" + "=" * 52)
    print("       SALES DATA ANALYSIS WITH PYTHON")
    print("=" * 52)

    try:
        df = load_data()

        calculate_kpis(df)

        (
            product_report,
            category_report,
            region_report,
            monthly_report,
            _sales_rep_report,
        ) = generate_reports(df)

        generate_charts(
            df,
            product_report,
            category_report,
            region_report,
            monthly_report,
        )

        save_cleaned_data(df)

        print("\n" + "=" * 52)
        print("ANALYSIS COMPLETED SUCCESSFULLY")
        print(f"Output directory: {OUTPUT_DIR}")
        print("=" * 52)

    except (ValueError, OSError, pd.errors.ParserError) as error:
        print(f"\nAnalysis failed: {error}")
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
