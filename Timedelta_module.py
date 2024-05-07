from datetime import datetime, timedelta

# Create a timedelta object representing 1 day
one_day = timedelta(days=1)
print(one_day)
# Get today's date
today = datetime.today()

# Calculate the date one week from today
one_week_later = today + timedelta(weeks=1)

# Calculate the difference between two dates
difference = one_week_later - today

print("Today:", today)
print("One week later:", one_week_later)
print("Difference:", difference)
