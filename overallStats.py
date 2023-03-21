# Converts the amount of seconds to a string in a format like 1:15.2
def SecondsToTime(seconds):
    minutes = round(seconds // 60)
    seconds -= minutes * 60

    time = str(round(seconds, 2))
    if (minutes > 0):
        time = str(minutes) + ":" + time

    return time

def GetUniqueDates(dates, removeYear = False):
    uniqueDates = []

    for i in dates:
        # Dates in csTimer csvs also contain the time at which it was completed so you need to remove that part
        date = i[5:10] if removeYear else i[0:10]

        if date not in uniqueDates:
            uniqueDates.append(date)

    return uniqueDates

def RemoveYears(listOfDates):
    newList = []
    for i in listOfDates:
        newList.append(i[5:10])

    return newList