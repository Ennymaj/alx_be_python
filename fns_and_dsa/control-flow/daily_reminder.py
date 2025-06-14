task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

if time_bound == "yes":
    if priority in ("high", "medium"):
        print(f"Reminder: {reminder} that requires immediate attention today!")
    elif priority == "low":
        print(f"Reminder: {reminder}. Try to complete it soon!")
    else:
        print(f"Reminder: {reminder}")
else:
    if priority in ("high", "medium"):
        print(f"Reminder: {reminder}. Try to schedule it soon.")
    elif priority == "low":
        print(f"Reminder: {reminder}. Consider completing it when you have free time.")
    else:
        print(f"Reminder: {reminder}")

