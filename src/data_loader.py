import numpy as np
import pandas as pd

from src.config import DATA_FILE


def create_sample_data():
    """Generate a reproducible fictional sales dataset."""

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

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_FILE, index=False)

    return df


def load_raw_data():
    """Load the original sales CSV or create a sample dataset."""

    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return create_sample_data()

    try:
        return pd.read_csv(DATA_FILE)
    except pd.errors.EmptyDataError:
        return create_sample_data()
