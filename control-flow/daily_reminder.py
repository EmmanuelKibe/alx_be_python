#Ask the user to input a task description
Task = input("Enter your task: ")

#Prompt for the task’s priority
Priority = input("Priority (high/medium/low): ")

#Ask if the task is time-bound
Time_bound = input("Is it time-bound? (yes/no): ")

match Priority, Time_bound:
    case ("high", "yes"):
        print(f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
    case ("high", "no"):
        print(f"Note: '{Task}' is high priority. Schedule it soon.")
    case ("medium", "yes"):
        print(f"Note: '{Task}' is medium priority and time-bound. Schedule it within the week.")
    case ("medium", "no"):
        print(f"Note: '{Task}' is medium priority and not time-bound. Schedule it when possible.")
    case ("low", "yes"):
        print(f"Note: '{Task}' is a low priority task. Try to complete it before the deadline.")
    case ("low", "no"):
        print(f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid input. Please check your priority and time-bound status.")

