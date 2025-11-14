# dag.py
from extract import extract
from transform import transform
from load import load

def run_pipeline():
    print("Running ETL Pipeline...\n")

    df_raw = extract()
    df_clean = transform(df_raw)
    load(df_clean)

    print("\nPipeline Completed Successfully!")

if __name__ == "__main__":
    run_pipeline()
