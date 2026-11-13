def calculate_kpis(df):
    """Calculate key performance indicators for sales."""

    total_records = len(df)
    total_orders = df["order_id"].nunique()
    units_sold = int(df["quantity"].sum())
    total_revenue = float(df["revenue"].sum())

    average_order_value = (
        total_revenue / total_orders if total_orders else 0
    )

    average_revenue_per_unit = (
        total_revenue / units_sold if units_sold else 0
    )

    return {
        "total_records": total_records,
        "total_orders": total_orders,
        "units_sold": units_sold,
        "total_revenue": round(total_revenue, 2),
        "average_order_value": round(average_order_value, 2),
        "average_revenue_per_unit": round(
            average_revenue_per_unit, 2
        ),
    }
