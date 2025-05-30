#Ask the user to input a task description
Task = input("Enter a task description: ")

#Prompt for the task’s priority
Priority = input("Priority (high/medium/low): ")

#Ask if the task is time-bound
Time_bound = input("Is it time-bound? (yes/no): ")

match Priority, Time_bound:
    case ("high", "yes"):
        print(f"Note '{Task}' is high priority and time-bound. Schedule it immediately.")
    case ("high", "no"):
        print(f"Note '{Task}' is high priority but not time-bound. Schedule it soon.")
    case ("medium", "yes"):
        print(f"Note '{Task}' is medium priority and time-bound. Schedule it within the week.")
    case ("medium", "no"):
        print(f"Note '{Task}' is medium priority and not time-bound. Schedule it when possible.")
    case ("low", "yes"):
        print(f"Note '{Task}' is low priority but time-bound. Schedule it by the end of the month.")
    case ("low", "no"):
        print(f"Note '{Task}' is low priority and not time-bound. You can do it later.")
    case _:
        print("Invalid input. Please check your priority and time-bound status.")

