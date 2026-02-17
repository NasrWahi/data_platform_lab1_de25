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