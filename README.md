# Wearable Health Anomaly Detection System

## Problem

Wearable devices generate continuous streams of health data, but detecting abnormal patterns is difficult due to noisy signals and missing values.

## Solution

This project builds a machine learning pipeline to detect anomalies in wearable health data such as heart rate and temperature using Isolation Forest.

## Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib

## Features

* Handles missing data using mean imputation
* Detects abnormal health patterns
* Visualizes anomalies in time-series data

## Real-World Relevance

This system can be used in wearable devices to flag early signs of health deterioration and assist in remote patient monitoring.

## Output Example

Anomalies are highlighted in the graph based on unusual spikes in heart rate and temperature.

## How to Run

```bash
pip install -r requirements.txt
cd src
python main.py
```

## Future Improvements

* Real-time data streaming from wearable devices
* Dashboard for monitoring patient vitals
* Integration with mobile alerts
