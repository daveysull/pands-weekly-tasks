import datetime

current_date = datetime.date.today()

# Monday is 0, Sunday is 6
day_of_the_week = current_date.weekday()

if day_of_the_week > 5:
    print("It's the weekend, YAY!")
elif day_of_the_week == 4:
    print("Nearly there!")
else:
    print("Yes, unfortunately today is a weekday")
