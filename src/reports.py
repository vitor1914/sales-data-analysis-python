import pandas as pd

from src.config import OUTPUT_DIR


def generate_reports(df, kpis):
    """Generate CSV reports for sales analysis."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    reports = {
        "product_sales.csv": (
            df.groupby("product", as_index=False)
            .agg(
                quantity_sold=("quantity", "sum"),
                total_revenue=("revenue", "sum"),
            )
            .sort_values("total_revenue", ascending=False)
        ),

        "category_sales.csv": (
            df.groupby("category", as_index=False)
            .agg(
                quantity_sold=("quantity", "sum"),
                total_revenue=("revenue", "sum"),
            )
            .sort_values("total_revenue", ascending=False)
        ),

        "regional_sales.csv": (
            df.groupby("region", as_index=False)
            .agg(
                quantity_sold=("quantity", "sum"),
                total_revenue=("revenue", "sum"),
            )
            .sort_values("total_revenue", ascending=False)
        ),

        "monthly_sales.csv": (
            df.groupby("month", as_index=False)
            .agg(
                quantity_sold=("quantity", "sum"),
                total_revenue=("revenue", "sum"),
            )
            .sort_values("month")
        ),

        "sales_representatives.csv": (
            df.groupby("sales_rep", as_index=False)
            .agg(
                orders=("order_id", "nunique"),
                total_revenue=("revenue", "sum"),
            )
            .sort_values("total_revenue", ascending=False)
        ),
    }

    for filename, report in reports.items():
        report.to_csv(OUTPUT_DIR / filename, index=False)

    kpis_df = pd.DataFrame(
        list(kpis.items()),
        columns=["metric", "value"],
    )

    kpis_df.to_csv(OUTPUT_DIR / "kpis.csv", index=False)

    print("\n========== REPORTS GENERATED ==========")

    for filename in reports:
        print(f"Generated: {filename}")

    print("Generated: kpis.csv")

    return reports
