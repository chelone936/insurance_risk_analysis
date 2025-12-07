import pandas as pd
import numpy as np

def clean_data(df):
    """
    Performs basic data cleaning on the insurance dataframe.
    
    Args:
        df (pd.DataFrame): Raw dataframe.
        
    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    if df is None:
        return None
    
    df_clean = df.copy()
    
    # Example cleaning steps (expand based on EDA findings)
    
    # 1. Handle missing values (Placeholder strategy: drop rows with all missing, or fill specific columns)
    # For now, we will just checking duplicates
    df_clean.drop_duplicates(inplace=True)
    
    # 2. Convert Date columns
    # Identifying potential date columns based on names
    date_cols = ['TransactionMonth', 'VehicleIntroDate']
    for col in date_cols:
        if col in df_clean.columns:
            df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')
            
    # 3. Ensure numeric columns are numeric
    numeric_cols = ['TotalPremium', 'TotalClaims']
    for col in numeric_cols:
         if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

    return df_clean
