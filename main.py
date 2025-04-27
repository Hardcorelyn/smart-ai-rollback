import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# 1. Simulate deployment data for modules
print("Simulating deployment data...")

# Simulated data for modules - login, dashboard, and payment
# Format: [latency, error_rate]
normal_data = np.random.normal(loc=[100, 2], scale=[10, 1], size=(100, 2))
anomalous_data = np.array([[500, 15], [200, 10]])  # High latency, high error

# Combine normal and anomalous data
data = np.vstack([normal_data, anomalous_data])
df = pd.DataFrame(data, columns=["Latency", "Error_Rate"])

# Simulated module names for easier reference
modules = ["login", "dashboard", "payment"]
df["Module"] = np.random.choice(modules, len(df))

print("Sample of generated data:\n", df.head())

# 2. Train anomaly detection model (Isolation Forest)
model = IsolationForest(contamination=0.05)
model.fit(df[["Latency", "Error_Rate"]])

# 3. Predict anomalies
df["Anomaly"] = model.predict(df[["Latency", "Error_Rate"]])

# 4. Add severity check: If anomaly is severe enough, trigger a full rollback
def severity_check(module, df_row):
    # If error rate is too high or latency exceeds certain thresholds, it's critical
    if module == "login" and df_row["Error_Rate"] > 10:
        return "full"
    elif df_row["Latency"] > 400:
        return "full"
    else:
        return "partial"

# 5. Apply severity logic for each module
rollback_actions = []
for idx, row in df.iterrows():
    action = severity_check(row["Module"], row)
    rollback_actions.append(action)

df["Rollback_Action"] = rollback_actions

# 6. Notify DevOps and take action

# 7. Execute rollback actions
for idx, row in df.iterrows():
    rollback_decision(row["Module"], row["Rollback_Action"])

# 8. Visualization of anomalies and decisions
plt.scatter(df.index, df["Latency"], c=df["Anomaly"], cmap='coolwarm')
plt.title("Deployment Anomaly Detection with Rollback Actions")
plt.xlabel("Deployment Index")
plt.ylabel("Latency")
plt.show()
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    from_email = "nnebaby12345@gmail.com"
    password = password = "<your-email-password>"
  # Replace with your email password (use app password for Gmail)
    smtp_server = "smtp.gmail.com"  # Gmail's SMTP server
    smtp_port = 587  # Port for sending emails

    # Create message
    message = MIMEMultipart()
    message['From'] = from_email = "nnebaby12345@gmail.com"
    message['To'] = to_email = "nneamakachikwesiri16@gmail.com"
    message['Subject'] =  "Partial rollback triggered in Login Module"
    message.attach(MIMEText("a partial rollback has been triggered for login module", "plain")
)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Encrypt the connection
        server.login(from_email, password)
        text = message.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f" Failed to send email: {str(e)}")

# Send Email for Partial Rollback
def send_partial_rollback_email(module):
    send_email(
        f"Partial rollback triggered in {module}",
        f"A partial rollback has been triggered for the {module} module due to a non-critical issue.",
        "nnebaby12345@gmail.com"  # DevOps team's email
    )
def rollback_decision(module, action):
    if action == "full":
        print(f"Critical issue detected in {module}! Full rollback triggered. Notify DevOps immediately.")
        
        # Full rollback: Email, Slack, and SMS notifications (just for understanding, but not needed here)
        send_email(
            f"Critical issue detected in {module}!",
            f"A full rollback has been triggered for the {module} module.",
            "nnebabay12345@gmail.com"
        )
    else:
        print(f" Partial rollback triggered for {module}.")
        
        # Only partial rollback: Email notification
        send_partial_rollback_email(module)






