import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    df['heart_rate'] = df['heart_rate'].fillna(df['heart_rate'].mean())
    df['temperature'] = df['temperature'].fillna(df['temperature'].mean())

    return df