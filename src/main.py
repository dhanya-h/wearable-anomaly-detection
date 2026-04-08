from preprocess import load_and_clean_data
from model import detect_anomalies
import matplotlib.pyplot as plt

df = load_and_clean_data('../data/sample_data.csv')
df = detect_anomalies(df)
from model import detect_anomalies, evaluate, add_rule_based_flags

df = add_rule_based_flags(df)

print(df)

colors = df['anomaly'].map({0: 'blue', 1: 'red'})

plt.scatter(df['time'], df['heart_rate'], c=colors)
plt.xlabel("Time")
plt.ylabel("Heart Rate")
plt.title("Anomaly Detection (Red = Anomaly)")
plt.show()
plt.savefig('../output.png')