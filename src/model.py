from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.2, random_state=42)

    features = df[['heart_rate', 'temperature']]
    df['anomaly'] = model.fit_predict(features)

    return df
   
def add_rule_based_flags(df):
    df['rule_flag'] = 0

    # Simple medical thresholds
    df.loc[df['heart_rate'] > 120, 'rule_flag'] = 1
    df.loc[df['temperature'] > 38, 'rule_flag'] = 1

    return df