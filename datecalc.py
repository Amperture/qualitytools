#!/usr/bin/python2
from datetime import date, timedelta
import string

# Assume at minimum 28 days per month, 12 months per year.
# (((12 * 3) + 3) * 28)
THREE_YEARS_THREE_MONTHS = (((12 * 3 ) + 3) * 28)

def addYears(dateIn, years):
    """ Returns a date object that is the supplied `date` with `years` added
    """
    try:
        return dateIn.replace(year = dateIn.year + years)
    except ValueError:
        # The above could return an error if February 29th is involved. This is
        # a fix for that.
        return dateIn + (date(dateIn.year + years, 1, 1)) - \
                (date(dateIn.year + years, 1, 1))


def inputEndDate():
    """ Returns a date as recorded from user input. """
    try:
        monRaw, dayRaw, yrRaw = raw_input("Please input the Expiry " +
                "Date (Format: mm/dd/yyyy): ").split('/')
        yr = string.atoi(yrRaw, 10)
        mon = string.atoi(monRaw, 10)
        day = string.atoi(dayRaw, 10)
        dateIn = date(year=yr, month=mon, day=day)

    except ValueError:
        print "Please use valid format: yyyy/mm/dd"
        return -1

    return dateIn

def inputRenewalLength(dateIn):
    """ Returns a date for system renewal. """
    yrs = input("How many years will we be waiting until renewal?: ")
    dateOut = addYears(dateIn, yrs)
    return dateOut

def adjustForWeekdays(dateIn):
    """ Returns a date based on whether or not the input date
    is on a weekend. If the input date falls on a Saturday or
    Sunday, the return is the date on the following Monday. If
    not, it returns the original date. """ 

    #If Saturday, return the following Monday.
    if dateIn.weekday() == 5:
        print "Projected End Date falls on a Saturday, correcting "\
        + "to fall on a Monday."
        return dateIn + timedelta(days = 2)

    #If Sunday, return the following Monday
    elif dateIn.weekday() == 6:
        print "Projected End Date falls on a Sunday, correcting "\
        + "to fall on a Monday."
        return dateIn + timedelta(days = 1)

    #On any other weekday, return the date
    else:
        return dateIn
    

if __name__ == "__main__":
    base = inputEndDate()
    renew = inputRenewalLength(base)
    mondayCheck = adjustForWeekdays(renew)
    print renew
    print renew.weekday()
    print mondayCheck
    print mondayCheck.weekday()
    finalAmount = (mondayCheck - date.today()).days
    if  finalAmount > THREE_YEARS_THREE_MONTHS:
        print "WARNING! This amount could technically be longer than "\
        + "Three Years, Three Months"
    print finalAmount
