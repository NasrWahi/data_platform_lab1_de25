## Data Platform: Data Ingestion, manipulation & workflow

# Product Data ETL Pipeline

# Overview
This project implements a professional ETL (Extract, Transform, Load) pipeline using Python, Pandas, and Pydantic. Which is designed, so that we can be able to process raw product data, enforce certain strict data schemas, and also generate analytical reports. By utilizing Pydantic for data validation, the pipeline would ensure high data integrity before performing statistical analysis.

# Objetives
- Identification and use of typical components in a data platform, specifically Pydantic for data contracts and Pandas for transformation.

- Implementation of an ETL pipeline flow.

- Python to read, validate with schemas and export data in various formats.

# ETL Process
This project's pipeline follows a structured flow to ensure that only "clean" and validated data reaches the final analysis, by:

1. Ingest/Extract: 
- That the Raw data is extracted from data/raw/products.csv. The ingestion layer handles initial file reading and prepares the data for structural validation.

2. Transform & Validation:
The transformation layer is reinforced with a Pydantic-based validation engine:

- Every row is validated against a Pydantic model to ensure correct data types.

    - Records that fail the structural check (TypeErrors) are caught early in the process.

- Data that violates business logic (negative prices or missing Primary Keys) is diverted to rejected_products.csv.

- Valid but anomalous data (prices > 5000). A flag_suspicious_price metadata column rather than being deleted, preserving valuable outlier information.

- Data Cleaning. Normalization of numeric values and handling of missing currency strings.

3. Acess (Load):
This generates three distinct output files in the data/results/ directory:

- analytics_summary.csv: A high-level report containing the mean price, median price, total product count, and data health metrics.

- price_analysis.csv: A detailed report of the top 10 most expensive products for manual outlier review.

- rejected_products.csv: All rows that were excluded from the main analysis due to structural or logical failures.

# Installation & Usage

## Essential Requirements
- Python 3.8 or higher
- Virtual Environment (.venv)

# 1. Setup Environment 
As follows:

## Activate the virtual environment (for Windows Git Bash):
source .venv/Scripts/activate

## Install dependencies:
uv pip install -r requirements.txt
[or] pip install -r requirements.txt

# 2. Execution
Once the dependencies are installed, you can run the ETL pipeline with: python src/main.py

# 3. Verification
After execution, verify the output files in the data/results/ directory, examples include:
- Check Summary: cat data/results/analytics_summary.csv
- Check Top 10 Expensive Products: cat data/results/price_analysis.csv
- Check Errors: cat data/results/rejected_products.csv
