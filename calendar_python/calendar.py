# Find the day of the week calendar
# 12/31/2021 = Friday


# Import Math for rounding feature
import math

# Import datetime module and set starting date
import datetime
from tracemalloc import start
start_date = datetime.date(2021, 12, 31)

# Get user input value
user_input = input("Enter a date (mm/dd/yyyy): ")

# Split user input value into month, day, year variables
input_split = user_input.split("/")
user_month = int(input_split[0])
user_day = int(input_split[1])
user_year = int(input_split[2])
user_value = datetime.date(int(input_split[2]), int(input_split[0]), int(input_split[1]))

# Use either leap year or non-leap year days
if user_year % 4 == 0:
    month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Adding or subtracting days to starting date
# As well as depending on if it is a leap year or not
if start_date < user_value and user_year % 4 == 0:
    days = sum(month_list[0:(user_month-1)]) + user_day - (user_year - start_date.year) - math.floor((start_date.year - user_year) / 4)
    years = (user_year - start_date.year - 1) * sum(month_list)
    add_days = datetime.timedelta(days + years)
    total_days = start_date + add_days

elif start_date < user_value:
    days = sum(month_list[0:(user_month-1)]) + user_day + ((user_year - start_date.year) / 4)
    years = (user_year - start_date.year - 1) * sum(month_list)
    add_days = datetime.timedelta(days + years)
    total_days = start_date + add_days

elif start_date > user_value and user_year % 4 == 0:
    days = sum(month_list) - (sum(month_list[0:(user_month-1)]) + user_day) - (start_date.year - user_year) + ((start_date.year - user_year) / 4)
    years = (start_date.year - user_year) * sum(month_list)
    add_days = datetime.timedelta(days + years)
    total_days = start_date - add_days
    
else: 
    days = sum(month_list) - (sum(month_list[0:(user_month-1)]) + user_day) + math.ceil((start_date.year - user_year) / 4)
    years = (start_date.year - user_year) * sum(month_list)
    add_days = datetime.timedelta(days + years)
    total_days = start_date - add_days

# Days of the week
week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

week_day = int((days + years) % 7)
day_of_the_week = week[week_day]


# print(add_days)
# print(f"{user_input} and {total_days} should match." )
# print(total_days.strftime("%A"))
print(f"The date you entered is on a {day_of_the_week}")
