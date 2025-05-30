#Ask the user to input a task description
Task = input("Enter your task: ")

#Prompt for the task’s priority
Priority = input("Priority (high/medium/low): ")

#Ask if the task is time-bound
Time_bound = input("Is it time-bound? (yes/no): ")

match Priority:
    case 'high':
        if Time_bound == 'yes':
            print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: {Task} is a high priority task that should be completed soon!")
    case 'medium':
        if Time_bound == 'yes':
            print(f"Reminder: {Task} is a medium priority task that should be completed before the deadline!")
        else:
            print(f"Reminder: {Task} is a medium priority task that can be done later")
    case 'low':
        if Time_bound == 'yes':
            print(f"Note: {Task} is a low priority task. But it should be completed before the deadline!")
        else:
            print(f"Note: {Task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Error: Make sure to enter a valid priority and time-bound status.")

