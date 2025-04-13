rollback_actions = []
for idx, row in df.iterrows():
    action = severity_check(row["Module"], row)
    rollback_actions.append(action)

df["Rollback_Action"] = rollback_actions

# 6. Notify DevOps and take action
def rollback_decision(module, action):
    if action == "full":
        print(f" Critical issue detected in {module}! Full rollback triggered. Notify DevOps immediately.")
        # Placeholder for actual notification logic (e.g., email, Slack, etc.)
    else:
        print(f" {module} issue detected. Partial rollback to previous state.")
        # Placeholder for partial rollback logic

# 7. Execute rollback actions
for idx, row in df.iterrows():
    rollback_decision(row["Module"], row["Rollback_Action"])
