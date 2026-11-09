import pandas as pd
import main


def sample_data():
    return pd.DataFrame([
        {
            "order_id": "ORD-001",
            "date": "2025-01-10",
            "product": "Mouse",
            "category": "Accessories",
            "quantity": 2,
            "unit_price": 10.0,
            "region": "North",
            "sales_rep": "Alice",
        },
        {
            "order_id": "ORD-002",
            "date": "2025-02-10",
            "product": "Laptop",
            "category": "Electronics",
            "quantity": 1,
            "unit_price": 100.0,
            "region": "South",
            "sales_rep": "Bruno",
        },
        {
            "order_id": "ORD-001",
            "date": "2025-01-10",
            "product": "Mouse",
            "category": "Accessories",
            "quantity": 2,
            "unit_price": 10.0,
            "region": "North",
            "sales_rep": "Alice",
        },
        {
            "order_id": "ORD-003",
            "date": "invalid-date",
            "product": "Keyboard",
            "category": "Accessories",
            "quantity": 1,
            "unit_price": 20.0,
            "region": "East",
            "sales_rep": "Carla",
        },
        {
            "order_id": "ORD-004",
            "date": "2025-03-10",
            "product": "Monitor",
            "category": "Electronics",
            "quantity": 0,
            "unit_price": 200.0,
            "region": "West",
            "sales_rep": "Daniel",
        },
    ])


def test_load_data_removes_duplicates_and_invalid_records(
    tmp_path, monkeypatch
):
    data_file = tmp_path / "sales.csv"
    output_dir = tmp_path / "outputs"
    output_dir.mkdir()

    sample_data().to_csv(data_file, index=False)

    monkeypatch.setattr(main, "DATA_FILE", data_file)
    monkeypatch.setattr(main, "OUTPUT_DIR", output_dir)

    df = main.load_data()

    assert len(df) == 2
    assert df["order_id"].nunique() == 2
    assert "revenue" in df.columns
    assert "month" in df.columns
    assert df["revenue"].sum() == 120


def test_calculate_kpis(tmp_path, monkeypatch):
    output_dir = tmp_path / "outputs"
    output_dir.mkdir()

    monkeypatch.setattr(main, "OUTPUT_DIR", output_dir)

    df = sample_data().iloc[:2].copy()
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["month"] = df["date"].dt.to_period("M").astype(str)

    kpis = main.calculate_kpis(df)

    assert kpis["total_records"] == 2
    assert kpis["total_orders"] == 2
    assert kpis["units_sold"] == 3
    assert kpis["total_revenue"] == 120.0
    assert kpis["average_order_value"] == 60.0

    assert (output_dir / "kpis.csv").exists()


def test_generate_reports(tmp_path, monkeypatch):
    output_dir = tmp_path / "outputs"
    output_dir.mkdir()

    monkeypatch.setattr(main, "OUTPUT_DIR", output_dir)

    df = sample_data().iloc[:2].copy()
    df["date"] = pd.to_datetime(df["date"])
    df["revenue"] = df["quantity"] * df["unit_price"]
    df["month"] = df["date"].dt.to_period("M").astype(str)

    reports = main.generate_reports(df)

    assert len(reports) == 5

    product_report = reports[0]
    assert len(product_report) == 2
    assert product_report["total_revenue"].sum() == 120

    expected_files = [
        "product_sales.csv",
        "category_sales.csv",
        "regional_sales.csv",
        "monthly_sales.csv",
        "sales_representatives.csv",
    ]

    for filename in expected_files:
        assert (output_dir / filename).exists()
