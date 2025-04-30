from datetime import date

# Define two date tuples: (day, month, year)
date1 = (22, 4, 2025)
date2 = (1, 1, 2025)

# Convert tuples to datetime.date objects
d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

# Calculate the difference in days
difference = abs((d1 - d2).days)

print(f"Number of days between {date1} and {date2} is {difference} days.")
