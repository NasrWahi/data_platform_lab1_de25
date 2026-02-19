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