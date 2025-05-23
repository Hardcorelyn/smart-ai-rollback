import pandas as pd
import os
print("📁 Current working directory:", os.getcwd())  # Add this to see where you are running from

# Load CSV
df = pd.read_csv("deployment_logs.csv")

# Use only numerical features for the model
features = ['ResponseTime', 'ErrorRate', 'CPU', 'Memory']
X = df[features]
print("📊 First few rows:")
print(df.head())

from sklearn.ensemble import IsolationForest

model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
model.fit(X)

df['Anomaly'] = model.predict(X)

print("📌 Anomaly counts:")
print(df['Anomaly'].value_counts())

print("\n🔍 Sample anomalies:")
print(df[df['Anomaly'] == -1].head())

import joblib
print("💾 Saving model...")
joblib.dump(model, 'smart_model.pkl')
print("✅ Model saved as smart_model.pkl")  # If you don't see this, something failed before it