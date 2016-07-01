#!/usr/bin/python
from datetime import date
import string

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
        yrRaw, monRaw, dayRaw = raw_input("Please input the Expiry " +
                "Date (Format: yyyy/mm/dd): ").split('/')
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


if __name__ == "__main__":
    base = inputEndDate()
    renew = inputRenewalLength(base)
    print renew
