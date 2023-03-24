import pandas as pd
from matplotlib import pyplot as plt
from datetime import timedelta, datetime as dt

import times as times
import overallStats as os

if __name__ == '__main__':
    df = pd.read_csv('4x4.csv', delimiter=';')

    # --- Solving times, averages ---
    singles = times.TimesToFloats(df['Time'])

    plt.plot(df['No.'],singles)
    plt.plot(df['No.'], times.CalculateAO(singles))
    plt.plot(df['No.'], times.CalculateAO(singles, 12))

    timeNumbers, personalbests = times.PersonalBestProgression(singles)
    plt.plot(timeNumbers, personalbests, 'o')

    plt.legend(['single', 'ao5', 'ao12', 'pb'])
    plt.show()

    # --- Time spent solving ---
    totalTimeSpent = os.SecondsToTime(sum(singles))
    mostDaysInARow = 0
    mostDaysBreak = 0

    firstDay = dt.strptime(df['Date'][0], '%Y-%m-%d %H:%M:%S')
    dateDelta =  dt.strptime(df['Date'][len(df['Date']) - 1], '%Y-%m-%d %H:%M:%S') - firstDay # Difference between last and first record's date
    # For some reason if I just set the index here ^ to -1 it returns an error

    allDays = []
    totalTimeByDate = []
    totalSolvesByDate = []
    daysInARow = 0
    daysBreak = 0
    for i in range(dateDelta.days + 1):
        day = (firstDay + timedelta(days = i)).date()

        recordsAtDate = df[df['Date'].str[0:10] == day.strftime('%Y-%m-%d')] # Get all records at the given date
        totalTimeByDate.append(sum(times.TimesToFloats(recordsAtDate['Time'])))
        totalSolvesByDate.append(len(recordsAtDate['Time']))

        if len(recordsAtDate) > 0:
            daysInARow += 1
            daysBreak = 0
        else:
            daysInARow = 0
            daysBreak += 1

        if daysInARow > mostDaysInARow: mostDaysInARow = daysInARow
        if daysBreak > mostDaysBreak: mostDaysBreak = daysBreak

        allDays.append(day)

    plt.plot(allDays, totalTimeByDate)
    plt.plot(allDays, totalSolvesByDate)

    print(mostDaysInARow)
    print(mostDaysBreak)
    print('The most solves (', max(totalSolvesByDate), ') were done on ', allDays[totalSolvesByDate.index(max(totalSolvesByDate))], '. The total time spent that day is ', os.SecondsToTime(totalTimeByDate[totalSolvesByDate.index(max(totalSolvesByDate))]), sep='')

    plt.legend(['Time spent (s)', 'Solves'])
    plt.show()