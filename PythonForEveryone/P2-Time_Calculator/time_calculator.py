# Write a function named add_time that takes in
# two required parameters and one optional parameter:

# * a start time in the 12-hour clock format (ending in AM or PM)
# * a duration time that indicates the number of hours and minutes
# * (optional) a starting day of the week, case insensitive

# The function should add the duration time to the start
# time and return the result.

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
    # Functions return one list
    # process_minutes
    # 0: result in 60 minutes format
    # 1: hours to add
    result_minutes = process_minutes(result_minutes)

    print(result_hour)
    print(result_minutes)

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

# def process_minutes(result_minutes):
