from pydantic import BaseModel, field_validator
from typing import Optional

class Product(BaseModel):
    id: str
    name: str
    price: float
    currency: Optional[str] = None

    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Negativt eller noll pris är omöjligt att hantera")
        return v

import pandas as pd
import numpy as np

def load_and_brand_data(file_path):
    df = pd.read_csv(file_path, sep=';')

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    df["price_numeric"] = pd.to_numeric(df["price"], errors='coerce')

    return df

def separate_rejected_data(df):
    rejected_condition = (
        (df["id"].isna() | 
        (df["id"] == "")) |
        (df["price_numeric"] <= 0) 
    )

    df_rejected = df[rejected_condition].copy()
    df_valid = df[~rejected_condition].copy()

    return df_valid, df_rejected

def apply_flags(df):
    
    df["flag_missing_currency"] = df["currency"].isna() 

    df["flag_suspicious_price"] = df["price_numeric"] > 5000

    df["flag_zero_price"] = df["price_numeric"] == 0

    return df






import pandas as pd

def klassificera_rad(row: pd.Series) -> tuple[str, str]:
    """
    Detta ska klassificera en rad som 'godkänd', 'flagga' eller 'avvisad'.

    Args:
        row: En rad från DataFrame

    Returns:
        tuple[str, str]: (status, anledning)
        - status: 'godkänd', 'flagga' eller 'avvisad'
        - anledning: Beskrivning av problem (eller godkönd)
    """

anledningar = []

# Hantera ID
if pd.isna(row['id']) or str(row['id']).strip() == '':
    return ('avvisad', 'Saknar ID')

# Hantera pris
price_val = row['price']
if pd.isna(price_val):
    anledningar.append('Saknar pris')
else:
    price_str = str(price_val).strip().lower()

    #
    if price_str in ['free', 'not available', '']:
        return ('avvisad', f'Ogiltigt pris: {price_val}')