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

    