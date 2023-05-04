# This function to check whether the year is leapyear or not
def is_Leap_Year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
        return True
#the Gregorian calendar, three conditions that are used to identify leap years
    else :
        return False

#Taking the year from the user
year = int(input("Please Enter the year you want to check = "))
#calling the function to ccheck the year that the user entered
result = is_Leap_Year(year)
print(result)
if (result == False):
    print(str(year)+" is not a multiple of 4 hence it's not a leap year.")
