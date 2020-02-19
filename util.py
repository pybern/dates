import calendar
import datetime
import os
import time

import dateparser

today = datetime.datetime.now()
MONTH = today.month
DAY = today.day
YEAR = today.year

MONTHS_ALPHA_FULL = calendar.month_name[1::]
MONTHS_ALPHA_ABBR = calendar.month_abbr[1::]

MONTHS_DIGIT_FULL =  [f'{i}' for i in range(1,13)]
MONTHS_DIGIT_ABBR = [f'{n:0>2}' for n in MONTHS_DIGIT_FULL]

YEAR_DIGIT_FULL = [f'{i}' for i in range(0,)]
YEAR_DIGIT_ABBR = [f'{n:0>2}' for n in YEAR_DIGIT_FULL]

ACTUAL_DATE = datetime.datetime(2020, 12, 1)
TEST_LINE = '2nd of Januay'
TEST_RESULT = dateparser.parse(TEST_LINE)

if __name__ == "__main__":
    pass


#TODO

