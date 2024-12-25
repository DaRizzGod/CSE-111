# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
print(day_of_week) # print 4


total = float(input("what is your total bill: "))


if (day_of_week == 2 or day_of_week == 3) and total >= 50:
    new_total = total * .90
    tax = new_total * .06
    sub_total = new_total + tax
    print(f'The overall cost will be ${sub_total:.2f}, the tax was ${tax:.2f}.')
  
else:
  tax = total * .06
  sub_total = total + tax
  
  print(f"Your total bill is {sub_total:.2f}, the tax was ${tax:.2f}. ")