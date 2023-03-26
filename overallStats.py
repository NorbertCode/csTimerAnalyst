from datetime import timedelta, datetime as dt
import times

# Converts the amount of seconds to a string in a format like 1:15.2
def SecondsToTime(seconds):
    timeUnits = [seconds, 0, 0] # Seconds, minutes, hours

    # Set up timeUnits to make it have correct values
    for i in range(1, len(timeUnits)):
        timeUnits[i] = round(timeUnits[i - 1] // 60)
        timeUnits[i - 1] -= timeUnits[i] * 60

    # Format it to a string
    time = ''
    for i in timeUnits:
        if i > 0:
            time = str(round(i, 2)) + time
            if len(str(i).split('.')[0]) < 2:
                time = ':0' + time
            else:
                time = ':' + time

    return time[1:] # The loop above adds an additional : at index 0

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
