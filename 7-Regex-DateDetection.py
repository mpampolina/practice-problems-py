#! python3
# 7-Regex-Date-Detection.py - Extracts correct dates in the DD/MM/YYYY format from clipboard

import pyperclip
import re


def checkLeap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    return False


monthsDic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Create a Regex for date
dateRegex = re.compile(r'''(
(\d{2})     # Day
(/|-|\.)    # First Separator
(\d{2})     # Month
(/|-|\.)    # Second Separator
(\d{4})   # Year
)''', re.VERBOSE)

# Get the text off of the clipboard
text = pyperclip.paste()

# Extract the dates from the clipboard
extractedDates = dateRegex.findall(text)
# For testing: print(extractedDates)

# Check if dates are valid
allDates = []
for dates in extractedDates:
    FebCond = 0
    if checkLeap(int(dates[5])):                                # Alter the max date of Feb if leap year
        monthsDic[2] = 29
        FebCond = 1
    if not 0 < int(dates[3]) <= 12:                             # Check if the month is within range
        continue
    elif not 0 < int(dates[1]) <= (monthsDic[int(dates[3])]):   # Check if the date is within range
        continue
    elif not 1000 < int(dates[5]) < 2999:                       # Check if the year is within range
        continue
    if FebCond == 1:                                            # Revert the max date of Feb
        monthsDic[2] = 28
    allDates.append(dates[0])

# Export
results = '\n'.join(allDates)
results = results.replace('.', '/').replace('-', '/')
pyperclip.copy(results)
