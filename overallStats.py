from matplotlib import pyplot as plt
from datetime import timedelta, datetime as dt

import times

# Converts the amount of seconds to a string in a format like 1:15.2
def SecondsToTime(seconds):
    minutes = round(seconds // 60)
    seconds -= minutes * 60

    hours = round(minutes // 60)
    minutes -= hours * 60

    time = str(round(seconds, 2))
    if (minutes > 0):
        time = str(minutes) + ":" + time

    if (hours > 0):
        time = str(hours) + ":" + time

    return time

def GetSessionStats(df):
    firstDay = dt.strptime(df['Date'][0], '%Y-%m-%d %H:%M:%S')
    dateDelta =  dt.strptime(df['Date'][len(df['Date']) - 1], '%Y-%m-%d %H:%M:%S') - firstDay # Difference between last and first record's date
    # For some reason if I just set the index here ^ to -1 it returns an error

    allDays = []
    totalTimeByDate = []
    totalSolvesByDate = []
    for i in range(dateDelta.days + 1):
        day = (firstDay + timedelta(days = i)).date()
        recordsAtDate = df[df['Date'].str[0:10] == day.strftime('%Y-%m-%d')] # Get all records at the given date

        totalTimeByDate.append(sum(times.TimesToFloats(recordsAtDate['Time'])))
        totalSolvesByDate.append(len(recordsAtDate['Time']))

        allDays.append(day)

    return allDays, totalTimeByDate, totalSolvesByDate

def GetDaysInARow(df, allDays):
    mostDaysInARow = 0
    mostDaysBreak = 0
    daysInARow = 0
    daysBreak = 0
    for i in allDays:
        recordsAtDate = len(df[df['Date'].str[0:10] == i.strftime('%Y-%m-%d')]) # Get all records at the given date

        if recordsAtDate > 0:
            daysInARow += 1
            daysBreak = 0
        else:
            daysInARow = 0
            daysBreak += 1

        if daysInARow > mostDaysInARow: mostDaysInARow = daysInARow
        if daysBreak > mostDaysBreak: mostDaysBreak = daysBreak

    return mostDaysInARow, mostDaysBreak