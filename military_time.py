import math
import os
import random
import re
import sys

# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# Algorithm Steps
# AM: 0-11
# PM: 12- 23
# only the hour part needs to be checked.

def check_am_pm(time_string):
    output = time_string[-2:]
    # lowercase for prevent case mismatch
    if str(output).lower == 'am':
        return 'am'
    else:
        return 'pm'

def check_and_convert_hour(hour_string, output_time):
    # check and convert hour
    hour_int = int(hour_string)
    if output_time== 'am':
        if hour_int > 0 and hour_int < 12:
            return hour_int
        else:
            hour_int = hour_int - 12
    elif output_time== 'pm':
        if hour_int > 0 and hour_int < 12:
            return 12 + hour_int
        else:
            return hour_int

def convert_int_to_str(hour_int):
    hour_str = str(hour_int)
    # if single digit
    if len(hour_str) == 1:
        hour_str = '0'+hour_str
    else:
        hour_str
    return hour_str

def get_hour(s):

    match = re.search('\:', s)
    colon_at = match.start()
    hour_string = s[0:colon_at]
    string_without_hr = s[colon_at:]

    return hour_string, string_without_hr

def timeConversion(s):

    # check if it is AM or PM.
    am_pm = check_am_pm(s)
    hour_string, string_without_hour = get_hour(s)
    hour_int = check_and_convert_hour(hour_string, am_pm)
    hour_str = convert_int_to_str(hour_int)

    s_without_am_pm = string_without_hour[:-2]

    # add formatted hour
    new_s = hour_str + s_without_am_pm
    return new_s



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    # input: hh:mm:ssam

    result = timeConversion(s)
    print(result)
