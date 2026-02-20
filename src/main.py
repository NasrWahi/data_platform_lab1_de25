import pandas as pd

from data_cleaner import load_and_branch_data, separate_rejected_data, apply_flags
import os

def main():
    raw_path = "data/raw/products.csv"
    output_dir = "data/results"

    # Extracting
    df = load_and_branch_data(raw_path)

    # Branching
    df_valid, df_rejected = separate_rejected_data(df)

    # Transforming
    df_final = apply_flags(df_valid)

    # Loading
    summary = {
        "snittpris": [df_final["price_numeric"].mean()],
        "medianpris": [df_final["price_numeric"].median()],
        "antal_produkter": [len(df_final)],
        "antal_produkter_saknat_pris": [df_final["price_numeric"].isna().sum()]
    }
    pd.DataFrame(summary).to_csv(f"{output_dir}/analytics_summary.csv", index=False)

    # Rejected products
    df_rejected.to_csv(f"{output_dir}/rejected_products.csv", index=False)

    print("ETL-processen är klar. Kontrollera 'data/results' för resultatet.")

if __name__ == "__main__":
    main()