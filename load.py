# load.py
import os
import pandas as pd
from sqlalchemy import create_engine

# Path to SQLite DB
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'data_projects.db')

def get_engine():
    """Create SQLite engine."""
    return create_engine(f"sqlite:///{DB_PATH}", echo=False)

def load(df: pd.DataFrame, table_name='cleaned_data'):
    """Load DataFrame into SQLite database."""
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Loaded {len(df)} rows into the database at: {DB_PATH}")

if __name__ == "__main__":
    import extract, transform
    raw_df = extract.extract()
    clean_df = transform.transform(raw_df)
    load(clean_df)
