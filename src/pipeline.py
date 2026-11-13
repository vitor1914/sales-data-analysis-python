import logging

from src.data_loader import load_raw_data
from src.data_cleaning import clean_data
from src.analysis import calculate_kpis
from src.reports import generate_reports
from src.visualizations import generate_charts
from src.config import OUTPUT_DIR


logger = logging.getLogger(__name__)


def run_pipeline():
    """Execute the complete sales analysis pipeline."""

    logger.info("Starting sales analysis pipeline.")

    try:
        # Load data
        raw_data = load_raw_data()
        logger.info("Data loaded successfully.")

        # Clean data
        cleaned_data = clean_data(raw_data)
        logger.info("Data cleaning completed.")

        # Calculate KPIs
        kpis = calculate_kpis(cleaned_data)
        logger.info("KPIs calculated successfully.")

        # Generate reports
        generate_reports(cleaned_data, kpis)
        logger.info("Reports generated successfully.")

        # Generate charts
        generate_charts(cleaned_data)
        logger.info("Charts generated successfully.")

        # Save cleaned dataset
        cleaned_data.to_csv(
            OUTPUT_DIR / "cleaned_sales.csv",
            index=False,
        )
        logger.info("Cleaned dataset saved successfully.")

        logger.info("Sales analysis pipeline completed.")

        return {
            "data": cleaned_data,
            "kpis": kpis,
        }

    except (ValueError, OSError) as error:
        logger.exception("Pipeline execution failed: %s", error)
        raise
