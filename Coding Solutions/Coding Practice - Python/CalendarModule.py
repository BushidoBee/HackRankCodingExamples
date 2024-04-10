import calendar
weekday = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

input_date = input().split(" ")

print(weekday[calendar.weekday(int(input_date[2]), int(input_date[0]), int(input_date[1]))])
