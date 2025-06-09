import datetime as dt

current_date = dt.datetime.now()

string_date = current_date.strftime("%A, %B %d, %Y")

print(string_date)