# extract.py
import os
import pandas as pd

# Path to the raw CSV file
RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
CSV_PATH = os.path.join(RAW_DIR, 'sample_data.csv')

def extract():
    """Reads CSV from the raw folder and returns a DataFrame."""
    df = pd.read_csv(CSV_PATH)
    print("Extracted data:")
    print(df.head())
    return df

if __name__ == "__main__":
    extract()
