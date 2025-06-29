from datetime import date
year = int(input("Enter your birth year (e.g. 2000): "))
month = int(input("Enter your birth month (1-12): "))
day = int(input("Enter your birth day (1-31): "))
today = date.today()
age = today.year - year
if (today.month, today.day) < (month, day):
    age -= 1
print("You are", age, "years old.")
