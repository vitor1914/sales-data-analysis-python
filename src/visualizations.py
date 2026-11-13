import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

from src.config import OUTPUT_DIR


def generate_charts(df):
    """Generate sales analysis charts."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sns.set_theme(style="whitegrid")

    # Monthly revenue
    monthly = (
        df.groupby("month")["revenue"]
        .sum()
        .reset_index()
        .sort_values("month")
    )

    plt.figure(figsize=(12, 6))
    sns.lineplot(
        data=monthly,
        x="month",
        y="revenue",
        marker="o",
    )
    plt.title("Monthly Revenue")
    plt.xlabel("Month")
    plt.ylabel("Revenue (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=300)
    plt.close()

    # Top 10 products
    top_products = (
        df.groupby("product")["revenue"]
        .sum()
        .nlargest(10)
        .sort_values()
        .reset_index()
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=top_products,
        x="revenue",
        y="product",
    )
    plt.title("Top 10 Products by Revenue")
    plt.xlabel("Revenue (R$)")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top_products.png", dpi=300)
    plt.close()

    # Revenue by category
    category = (
        df.groupby("category")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    plt.figure(figsize=(9, 6))
    sns.barplot(
        data=category,
        x="category",
        y="revenue",
    )
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue (R$)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "category_revenue.png", dpi=300)
    plt.close()

    # Revenue by region
    regional = (
        df.groupby("region")["revenue"]
        .sum()
        .reset_index()
        .sort_values("revenue", ascending=False)
    )

    plt.figure(figsize=(9, 6))
    sns.barplot(
        data=regional,
        x="region",
        y="revenue",
    )
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue (R$)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "regional_revenue.png", dpi=300)
    plt.close()

    # Revenue distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(
        data=df,
        x="revenue",
        bins=30,
        kde=True,
    )
    plt.title("Revenue Distribution")
    plt.xlabel("Revenue (R$)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "revenue_distribution.png", dpi=300)
    plt.close()

    print("\n========== CHARTS GENERATED ==========")
    print("Generated: 5 charts in outputs/")
