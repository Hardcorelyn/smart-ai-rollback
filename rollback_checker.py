import pandas as pd
import joblib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email sending function
def send_email(subject, body, to_email):
    from_email = "nnebaby12345@gmail.com"
    password = "<your-email-password>"  # Use app password for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())
        server.quit()
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Severity check logic
def severity_check(module, row):
    # Example: if error rate > 10 or latency > 400 => full rollback needed
    if row['ErrorRate'] > 10 or row['ResponseTime'] > 400:
        return "full"
    else:
        return "partial"

# Main rollback checker
def rollback_checker():
    df = pd.read_csv("latest_deployment.csv")
    features = ['ResponseTime', 'ErrorRate', 'CPU', 'Memory']
    X = df[features]

    model = joblib.load("smart_model.pkl")
    df['Anomaly'] = model.predict(X)

    devops_email = "nnebaby12345@gmail.com"

    print("\n📊 Deployment Check Results:")
    for idx, row in df.iterrows():
        module = row['Module']
        if row['Anomaly'] == -1:  # anomaly detected
            action = severity_check(module, row)
            subject = f"{action.capitalize()} rollback triggered for {module} module"
            body = (f"An anomaly was detected in the {module} module.\n"
                    f"Recommended rollback action: {action} rollback.\n"
                    f"Rollback is pending DevOps approval before execution.")
            
            send_email(subject, body, devops_email)
            
            print(f"⚠️ Anomaly detected in '{module}'. {action.capitalize()} rollback is pending approval.")
        else:
            print(f"✅ '{module}' is healthy — no rollback needed.")

if __name__ == "__main__":
    rollback_checker()
