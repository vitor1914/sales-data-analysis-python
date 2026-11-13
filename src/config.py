from pathlib import Path


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

# Input dataset
DATA_FILE = DATA_DIR / "sales.csv"

# Required dataset columns
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

# Create directories if they do not exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
