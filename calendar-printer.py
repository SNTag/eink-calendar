
#!/usr/bin/env python3

# SNTag
# 31/10/2019
# Written to assemble a calendar list from my org-files.

import subprocess
from exchangelib.folders import Calendar
from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC
import pytz

with open("./input/example-calendar.ics", 'rb') as my_calendar:
    read_my_calendar = Calendar.from_ical(my_calendar.read())
    for i in read_my_calendar.walk():
#        print(i)
        if i.name == 'VEVENT':
            for item in i.items():

                if item[0] == 'RECURRENCE-ID':
                    reoccur_item = item[1]
                    print(reoccur_item.params)
                    print(reoccur_item.dt)
                    continue
                if item[0] == 'DTSTART':
                    print('DSTART', item[1].dt)
                    continue
                if item[0] == 'DTEND':
                    print('DTEND', item[1].dt)
                    continue
                if item[0] == 'DTSTAMP':
                    print('DTSTAMP', item[1].dt)
                    continue
                print(item)

print('why')
# print(i.get('summary'))
# date = i.get('dtstart')
# print(date.to_ical())
# print(i.get('description'))
# print(i.get('dtstart'))
# print(i.get('dtend'))
# print(i.get('dtstamp'))


def calendar_setup():
    """ Will setup calendar paths
    """

    global toStore
    toStore = []
    indiciesWanted = {5, 8}
    for i,row in enumerate(open("./setup_file.txt")):
        if i in indiciesWanted:
            toStore.append(row.strip())


            
def calendar_cleaner():
    """ This function will clean up the calendar org file to make it human readable
    warning:: will probably not work with GUI set up as it is
    """

    # this is a really lazy approach.  its possible in python, should switch it to that when possible
    subprocess.call("./calendar_cleaner.sh")  # ensure correct permission: chmod u+xr


    
def print_items():
    """ main function.  Controls the output and everything else
    """

    # setting up the calendar locations
    calendar_setup()

    


if __name__=='__main__':
    print_items()
