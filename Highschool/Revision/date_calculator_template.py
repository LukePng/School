#######################################
# Mission 1: Date Calculator Template #
#######################################

#############################
# Task 1 - Helper Functions #
#############################

###########
# Task 1a #
###########
def is_leap_year(year):
    """
    is_leap_year (year) -> boolean
    Function takes in a specific year.
    Returns True if it is a leap year, False otherwise.
    """
    ## Your Code Here ##
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
    
# print (is_leap_year(2000)) # True
# print (is_leap_year(1900)) # False
# print (is_leap_year(1984)) # True
# print (is_leap_year(2015)) # False

###########
# Task 1b #
###########
def days_in_month(month):
    """
    days_in_month (month) -> int
    Function takes in a specific month.
    Returns number of days in that month for a normal year.
    
    Note: This function needs not to consider leap year.
    """
    ## Your Code Here ##
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 28

##Print out number of days in each month:
# for i in range(1, 13):
#     print(i, days_in_month(i))

###########
# Task 1c #
###########
def num_of_leap_years (start_year, end_year):
    """
    num_of_leap_years (start_year, end_year) -> int
    Function takes in 2 years: start_year (inclusive) and end_year (exclusive).
    Returns number of leap years in between the 2 years.
    """
    ## Define num_of_leap_years using iterative loop ##
    ## Your Code Here ##
    leap_year = 0
    for i in range(start_year, end_year):
        if is_leap_year(i):
            leap_year += 1
    return leap_year

##print (num_of_leap_years(2010, 2016)) # 1
##print (num_of_leap_years(2008, 2013)) # 2
##print (num_of_leap_years(1900, 2016)) # 28

###########
# Task 1d #
###########
def is_valid_date (date):
    """
    is_valid_date (date) -> boolean
    Function checks if the date entered is a valid date.
    Returns True if it's valid, False otherwise.
    """
    ## Your Code Here ##
    month = date[2:4]
    day = date[:2]
    year = date[4:]
    if int(month) < 12:
        if int(day) <= days_in_month(int(month)) and int(day) > 0:
            return True
        elif is_leap_year(int(year)):
            if int(month) == 2 and int(day) == 29:
                return True
    return False

# print (is_valid_date("29022016")) # True
# print (is_valid_date("31042015")) # False
# print (is_valid_date("29022015")) # False

###########################
# Task 2 - Main Functions #
###########################

###########
# Task 2a #
###########
def num_of_days_from_1900 (date):
    """
    num_of_days_from_1900 (date) -> int
    Function takes in a date.
    Returns the number of days of the input date after "01011900".
    """
    ## Your Code Here ##
    if is_valid_date(date) == False:
        return 'Invalid date entered. Please try again'
    month = date[2:4]
    day = date[:2]
    year = date[4:]

    num_days = 365 * (int(year) - 1900) + num_of_leap_years(1900, int(year))
    for i in range(1, int(month)):
            num_days += days_in_month(i)

    num_days += int(day) - 1
    if is_leap_year(int(year)) and int(month) > 2:
        num_days += 1

    return num_days

# print (num_of_days_from_1900("30011900")) # 29
# print (num_of_days_from_1900("28021900")) # 58
# print (num_of_days_from_1900("01031904")) # 1520
# print (num_of_days_from_1900("31012016")) # 42398

###########
# Task 2b #
###########
def days_between_2_dates (date1, date2):
    if is_valid_date(date1) == False  or is_valid_date(date2) == False:
        return 'Invalid date entered. Please try again'
    """
    days_between_2_dates (date1, date2) -> int
    Function takes in 2 dates.
    Returns the number of days in between the 2 dates.
    """
    ## Your Code Here ##
    return abs(num_of_days_from_1900(date1) - num_of_days_from_1900(date2))

#print (days_between_2_dates("15041984", "26102000")) # 6038
#print (days_between_2_dates("26102000", "15041984")) # 6038
#print (days_between_2_dates("26102000", "31012016")) # 5575

###########
# Task 2c #
###########
def add_n_days_after_1900 (days):
    """
    add_n_days_after_1900 (days) -> date
    Function takes in a specific number of days.
    Returns the date after adding the input number of days to "01011900".
    """
    ## Your Code Here ##
    year = 1900 + days // 365
    days -= (days // 365 * 365 + num_of_leap_years(1900, year))
    
    
    month = 1
    for i in range(1, 13):
        if is_leap_year(year) and i == 2:
            if days >= 29:
                days -= 29
                month += 1
            else:
                break
        elif days >= days_in_month(i):
            days -= days_in_month(i)
            month += 1
        else:
            break
    day = days + 1
    
    return str(day).zfill(2) + str(month).zfill(2) + str(year)
    
# print (add_n_days_after_1900(30)) # "31011900"
# print (add_n_days_after_1900(31)) # "01021900"
# print (add_n_days_after_1900(59)) # "01031900"
# print (add_n_days_after_1900(1519)) # "29021904"
# print (add_n_days_after_1900(1520)) # "01031904"



###########
# Task 2d #
###########
def add_n_days_from_a_date (date, days):
    if is_valid_date(date) == False:
        return 'Invalid date entered. Please try again'
    """
    add_n_days_from_a_date (date, days) -> date
    Function takes in a date and a specific number of days.
    Returns the date after adding the input number of days to the input date.
    """
    ## Your Code Here ##
    return add_n_days_after_1900(num_of_days_from_1900(date) + days)

# print (add_n_days_from_a_date ("15041984", 6038)) # 26102000
# print (add_n_days_from_a_date ("26102000", 6038)) # 08052017

###########
# Task 2e #
###########
def weekday_of_date (date):
    """
    weekday_of_date (date) -> str
    Function takes in a date.
    Returns the weekday of the input date.
    """
    ## Your Code Here ##
    weekday = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    return weekday[num_of_days_from_1900(date) % 7]

# print (weekday_of_date("01011900")) # "Monday"
# print (weekday_of_date("02011900")) # "Tuesday"
# print (weekday_of_date("31012016")) # "Sunday"

############################
# Task 3 - Date Calculator #
############################
def date_calculator():
    """
    date_calculator ()
    Function takes in an input from user and performs the functions accordingly.
    """
    done = False
    while done:
        # Prepare Menu
        print ("-----------------------------------------")
        print ("Welcome to date calculator")
        print ("  1. Calculate number of days between 2 dates.")
        print ("  2. Add n days from a date.")
        print ("  3. Find weekday of a date.")
        print ("  4. Exit the programme.\n")
        print ("**Please note the format of date should follow the format of 'DDMMYYYY'\n")
        
        # Get Input
        option = int(input ("Select a function: "))
        
        ## Your Code Here ##
        if option == 1:
            print('Days between = ' + days_between_2_dates(input("Enter the first date: "), input("Enter the second date: ")))
        if option == 2:
            print('New date' + add_n_days_from_a_date(input("Enter the date: "), int(input("Enter the number of days: "))))
        if option == 3:
            print('Weekday:' + weekday_of_date(input("Enter the date: ")))
        if option == 4:
            done = False
            print('bai bai')
        

date_calculator()
