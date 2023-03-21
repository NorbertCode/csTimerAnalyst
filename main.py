from datetime import datetime as dt, timedelta as tDelta
import pandas as pd
from matplotlib import pyplot as plt

import times as times
import overallStats as os

if __name__ == '__main__':
    df = pd.read_csv('v_perm.csv', delimiter=';')

    # --- Solving times, averages ---
    plt.plot(df['No.'],df['Time'])

    plt.plot(df['No.'], times.CalculateAO(df['Time'].tolist()))
    plt.plot(df['No.'], times.CalculateAO(df['Time'].tolist(), 12))

    timeNumbers, personalbests = times.PersonalBestProgression(df['Time'].tolist())
    plt.plot(timeNumbers, personalbests, 'o')

    plt.legend(['single', 'ao5', 'ao12', 'pb'])
    plt.show()

    # --- Time spent solving ---
    totalTimeSpent = os.SecondsToTime(sum(df['Time']))
    mostDaysInARow = 0 # todo: show this
    mostDaysBreak = 0 # todo: show this

    firstDay = dt.strptime(df['Date'][0], '%Y-%m-%d %H:%M:%S')
    dateDelta =  dt.strptime(df['Date'][len(df['Date']) - 1], '%Y-%m-%d %H:%M:%S') - firstDay # Difference between last and first record's date

    allDays = []
    totalTimeByDate = []
    totalSolvesByDate = []
    daysInARow = 0
    daysBreak = 0
    for i in range(dateDelta.days + 1):
        day = (firstDay + tDelta(days = i)).date()

        recordsAtDate = df[df['Date'].str[0:10] == day.strftime('%Y-%m-%d')] # Get all records at the given date
        totalTimeByDate.append(sum(recordsAtDate['Time']))
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

    plt.legend(['Time spent (s)', 'Solves'])
    plt.show()