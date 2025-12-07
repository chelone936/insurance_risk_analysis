import pandas as pd
import os

def load_data(filepath):
    """
    Loads the insurance data from a pipe-delimited text file.

    Args:
        filepath (str): Path to the dataset file.

    Returns:
        pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} was not found.")

    try:
        # The data is separated by '|', ensuring low_memory=False to handle mixed types warning initially
        df = pd.read_csv(filepath, sep='|', low_memory=False)
        print(f"Successfully loaded data from {filepath} with shape {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
