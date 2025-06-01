# Prompt user for task description
task = input("Enter your task: ")

# Prompt for priority (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# Prompt if the task is time-bound (yes or no)
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case to respond based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unknown priority level"

# Modify reminder if the task is time-bound
if time_bound == "yes":
    if priority in ["high", "medium"]:
        reminder += " that requires immediate attention today!"
    elif priority == "low":
        reminder += ". Try to complete it soon!"
else:
    if priority in ["high", "medium"]:
        reminder += ". Try to schedule it soon."
    elif priority == "low":
        reminder += ". Consider completing it when you have free time."

# Print the final reminder
print(reminder)
