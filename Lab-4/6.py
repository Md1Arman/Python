# 6)	Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.

def print_24_hours():
    for hour in range(24):
        if hour == 0:
            print("12 Midnight",end=",")
        elif hour == 12:
            print("12 Noon",end=",")
        elif hour < 12:
            print(f"{hour} AM",end=",")
        else:
            print(f"{hour - 12} PM",end=",")

print_24_hours()
