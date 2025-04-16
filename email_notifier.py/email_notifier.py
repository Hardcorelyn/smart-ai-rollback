def send_email(subject, body, to_email):
    from_email = "nnebaby12345@gmail.com"
    password = "Nne@mka12345"  # Replace with your email password (use app password for Gmail)
    smtp_server = "smtp.gmail.com"  # Gmail's SMTP server
    smtp_port = 587  # Port for sending emails

    # Create message
    message = MIMEMultipart()
    message['From'] = from_email = "nnebaby12345@gmail.com"
    message['To'] = to_email = "nneamakachikwesiri16@gmail.com"
    message['Subject'] = "Partial rollback triggered in Login Module"
    message.attach(
        MIMEText(body, 'A partial rollback has been triggered for the Login module due to a non-critical issue.'))

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