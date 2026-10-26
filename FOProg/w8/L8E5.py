from datetime import datetime, timedelta

# Get today's date with a specific hour
today = datetime.now()
today_with_hour = today.replace(hour=9, minute=0)
print("Today at 9:00 AM:", today_with_hour)

# Manually create tomorrow's date with a specific hour
tomorrow_with_hour = datetime(today.year, today.month, today.day + 1, 9, 0, 0)
print("Tomorrow at 9:00 AM:", tomorrow_with_hour)

# Get today's date
today = datetime.now()

# Calculate the date 30 days from now
date_30_days_from_now = today + timedelta(days=30)
print("Date 30 days from now:", date_30_days_from_now)
