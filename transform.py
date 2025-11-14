# transform.py
import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Trim whitespace only for string columns
    for col in df.select_dtypes(include='object').columns:
        df.loc[:, col] = df[col].str.strip()

    # Remove duplicate rows and make an explicit copy
    df = df.drop_duplicates().copy()

    # Convert age to integer (nullable) safely
    if 'age' in df.columns:
        df.loc[:, 'age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')

    # Robust salary normalization:
    if 'salary' in df.columns:
        # turn things into strings, strip, replace known tokens with NaN
        s = df['salary'].astype(str).str.strip().replace(
            {'not_available': None, '': None, 'nan': None, 'None': None}
        )

        # coerce to numeric (float), store in local var
        salary_num = pd.to_numeric(s, errors='coerce')

        # assign numeric nullable float dtype back to dataframe
        df.loc[:, 'salary'] = salary_num.astype('Float64')

        # compute salary_k from numeric series (safe)
        df.loc[:, 'salary_k'] = (salary_num / 1000).round(2)

    # Reorder columns if present
    cols = ['id', 'name', 'age', 'salary', 'salary_k']
    cols_present = [c for c in cols if c in df.columns]

    # -- debug: print dtypes (you can remove these prints later) --
    print("\nDEBUG: column dtypes after transform:")
    print(df.dtypes)
    print("\nTransformed head:")
    print(df.head())

    return df.loc[:, cols_present]
