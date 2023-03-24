import pandas as pd
from matplotlib import pyplot as plt

import times as times
import overallStats as os
import gui

if __name__ == '__main__':
    gui.GUI()

'''
    file = ''
    df = pd.read_csv('4x4.csv', delimiter=';')
    singles = times.TimesToFloats(df['Time'])

    # --- Solving times, averages ---
    

    plt.plot(df['No.'], singles)
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

    allDays, totalTimeByDate, totalSolvesByDate, mostDaysInARow, mostDaysBreak = os.CalculateSolvesPerDate(df)

    plt.plot(allDays, totalTimeByDate)
    plt.plot(allDays, totalSolvesByDate)

    # todo: show this visually
    print(mostDaysInARow)
    print(mostDaysBreak)
    print('The most solves (', max(totalSolvesByDate), ') were done on ', allDays[totalSolvesByDate.index(max(totalSolvesByDate))], '. The total time spent that day is ', os.SecondsToTime(totalTimeByDate[totalSolvesByDate.index(max(totalSolvesByDate))]), sep='')

    plt.legend(['Time spent (s)', 'Solves'])
    plt.show()
'''