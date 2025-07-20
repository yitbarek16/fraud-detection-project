"""
src/data_loader.py

This module provides utility functions for loading datasets used in the fraud detection project.
"""

import pandas as pd

def load_data(path):
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    path : str
        The file path to the CSV file.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the loaded data.
    """
    return pd.read_csv(path)