# Write a function named add_time that takes in
# two required parameters and one optional parameter:

# * a start time in the 12-hour clock format (ending in AM or PM)
# * a duration time that indicates the number of hours and minutes
# * (optional) a starting day of the week, case insensitive

# The function should add the duration time to the start
# time and return the result.

# Do not import any Python libraries. Assume that the start times
# are valid times. The minutes in the duration time will be a whole
# number less than 60, but the hour can be any whole number.

def add_time(start, duration):
    # Initialize variables
    new_time = ''

    # Split the inputs
    start = start.split()
    duration = duration.split(':')
    # The structure of the time input obligues to divide it
    start_time = start[0].split(':')

    # I am going to divide the process: add minutes and hours
    # both functions results are going to be processed later
    result_hour = add_hours(start_time[0], duration[0])
    result_minutes = add_minutes(start_time[1], duration[1])

    # The variables contain 'raw' results
    # Functions return one list each one
    # process_minutes
    # 0: result in 60 minutes format
    # 1: hours to add
    result_minutes = process_minutes(result_minutes)

    # process_hours
    # 0: final time result
    # 1: how many cycles of 12 hours have the result
    result_time = process_hours(result_hour, result_minutes[1])

    # print(result_minutes)
    # print(result_time)
    # print(str(result_time[0]) + ':' + str(result_minutes[0]))

    # new_time = format_result(result_minutes[0], result_time, start[1])

    return new_time

# Add the hours of the parameters of the add_time function
def add_hours(start_hour, duration_hour):
    # Convert parameters to int
    start_hour = int(start_hour)
    duration_hour = int(duration_hour)

    # Retuns the addition of the parameters
    return start_hour + duration_hour

# Add the minutes of the parameters of the add_time function
def add_minutes(start_minutes, duration_minutes):
    # Convert parameters to int
    start_minutes = int(start_minutes)
    duration_minutes = int(duration_minutes)

    # Retuns the addition of the parameters
    return start_minutes + duration_minutes

# Process result of add_minutes function
def process_minutes(result_minutes):
    # Initialize variables
    # minutes has the real time in minutes
    # hours_add has the hours to add to the main hour
    minutes = 0
    hours_add = 0

    # Check how many hours we have to add to the final result
    hours_add = result_minutes // 60
    # Check the real minutes of the result
    minutes = result_minutes % 60

    return [minutes, hours_add]

# Process result of add_hours function
def process_hours(result_hour, hours_add):
    # Initialize variables
    # hours has the real time in hours
    # cycles has 12-hour cycle to add to the main result
    hours = 0
    cycles = 0

    # Add the hours got in process_minutes function
    result_hour += hours_add

    # Check how many cycles of 12 hours we have
    cycles = result_hour // 12
    # Check the real hours of the result
    hours = result_hour % 12
    # Zero does not exists in terms of hours
    if hours == 0:
        hours = 12

    return [hours, cycles]
