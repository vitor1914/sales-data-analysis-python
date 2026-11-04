# Sales Data Analysis with Python

A Python project for analyzing sales data, cleaning datasets, calculating business performance indicators, and generating reports and visualizations.

## Project Overview

This project uses Python and data analysis libraries to process sales records and extract useful business insights.

The application validates and cleans the dataset, calculates key performance indicators (KPIs), generates analytical reports, and creates charts to support sales performance analysis.

If the input CSV file is missing or empty, the application generates a sample sales dataset to allow the analysis to run.

## Features

- Automatic sample dataset generation.
- Sales data loading and validation.
- Handling of missing and invalid records.
- Revenue calculation based on quantity and unit price.
- Monthly sales analysis.
- Key Performance Indicators (KPIs).
- Sales performance analysis by product.
- Sales performance analysis by sales representative.
- Automated report generation.
- Data visualizations using Matplotlib and Seaborn.
- Export of cleaned sales data and analytical results.

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```text
sales-data-analysis-python/
│
├── data/
│   └── sales.csv
│
├── outputs/
│   ├── Generated reports
│   ├── Charts
│   └── Cleaned dataset
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/vitor1914/sales-data-analysis-python.git
```

Navigate to the project directory:

```bash
cd sales-data-analysis-python
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the environment on Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Execute the main script:

```bash
python main.py
```

The application processes the sales dataset and saves the generated results in the `outputs/` directory.

## Key Performance Indicators

The analysis calculates indicators such as:

| KPI | Description |
|---|---|
| Total Records | Number of valid sales records |
| Unique Orders | Number of distinct orders |
| Units Sold | Total quantity of products sold |
| Total Revenue | Total sales revenue |
| Average Order Value | Revenue divided by unique orders |
| Revenue per Unit | Revenue divided by total units sold |

## Generated Analysis

The project generates reports and visualizations to explore:

- Revenue by product.
- Sales volume by product.
- Number of orders by product.
- Revenue by sales representative.
- Units sold by sales representative.
- Monthly sales performance.

## Data Cleaning

The data preparation process includes:

- Checking required columns.
- Removing records with missing required values.
- Filtering invalid quantities and unit prices.
- Calculating revenue from quantity and unit price.
- Preparing monthly information for analysis.

## Project Status

<escape>Completed — </escape> the application has been executed successfully, generating analytical reports, charts, and a cleaned dataset.

## Author

**Israel Vitor**

GitHub: [@vitor1914](https://github.com/vitor1914)