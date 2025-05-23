import pandas as pd

# Simulated deployment data for new modules
new_data = [
    {'Module': 'Login', 'ResponseTime': 120.5, 'ErrorRate': 0.3, 'CPU': 22.5, 'Memory': 50.1},
    {'Module': 'Payments', 'ResponseTime': 700.0, 'ErrorRate': 4.2, 'CPU': 78.0, 'Memory': 300.2},  # likely anomaly
    {'Module': 'Dashboard', 'ResponseTime': 150.2, 'ErrorRate': 0.4, 'CPU': 30.0, 'Memory': 60.0},
    {'Module': 'Transfer', 'ResponseTime': 860.1, 'ErrorRate': 6.7, 'CPU': 80.0, 'Memory': 410.3},  # likely anomaly
    {'Module': 'Settings', 'ResponseTime': 130.0, 'ErrorRate': 0.2, 'CPU': 25.0, 'Memory': 45.0}
]

df_new = pd.DataFrame(new_data)
df_new.to_csv("latest_deployment.csv", index=False)
print(" latest_deployment.csv created")
