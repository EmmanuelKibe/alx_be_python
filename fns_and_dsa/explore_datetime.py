import datetime 

def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date_str}")




number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.datetime.now() + datetime.timedelta(days=number_of_days)
    future_date_str = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date_str}")

calculate_future_date()