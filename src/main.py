from preprocess import load_and_clean_data
from model import detect_anomalies
import matplotlib.pyplot as plt

df = load_and_clean_data('../data/sample_data.csv')
df = detect_anomalies(df)

print(df)

plt.scatter(df['time'], df['heart_rate'], c=df['anomaly'])
plt.xlabel("Time")
plt.ylabel("Heart Rate")
plt.title("Anomaly Detection")
plt.show()