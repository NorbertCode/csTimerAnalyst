import pandas as pd
from matplotlib import pyplot as plt
from datetime import timedelta, datetime as dt

import times as times
import overallStats as os

class Analyser:
    def __init__(self, fileName):
        self.df = pd.read_csv(fileName, delimiter=';')

        self.singles = times.TimesToFloats(self.df['Time'])
        self.pb = min(self.singles)    
        self.totalTimeSpent = os.SecondsToTime(sum(self.singles))
        self.allDays, self.totalTimeByDate, self.totalSolvesByDate = os.GetSessionStats(self.df)
        self.mostDaysInARow, mostDaysBreak = os.GetDaysInARow(self.df, self.allDays)

        print('Personal best:', os.SecondsToTime(self.pb))
        print('Total time spent:', self.totalTimeSpent)
        print('Most days in a row:', self.mostDaysInARow)
        print('Most days break:', mostDaysBreak)
        mostSolvesDate = self.allDays[self.totalSolvesByDate.index(max(self.totalSolvesByDate))]
        timeSpentOnMostSolves = os.SecondsToTime(self.totalTimeByDate[self.totalSolvesByDate.index(max(self.totalSolvesByDate))])
        print('The most solves (', max(self.totalSolvesByDate), ') were done on ', mostSolvesDate, '. The total time spent that day is ', timeSpentOnMostSolves, sep='')

    def ShowTimesGraph(self, aoTypes = [5, 12]):
        plt.plot(self.df['No.'], self.singles)

        for i in aoTypes:
            plt.plot(self.df['No.'][i - 1:], times.CalculateAO(self.singles, i))

        timeNumbers, personalbests = times.PersonalBestProgression(self.singles)
        plt.plot(timeNumbers, personalbests, 'o')

        legend = ['single', 'pb']
        for i in aoTypes:
            legend.insert(-1, 'ao' + str(i))
        plt.legend(legend)
        
        plt.show()

    def ShowSolvesByDayGraph(self):
        plt.plot(self.allDays, self.totalTimeByDate)
        plt.plot(self.allDays, self.totalSolvesByDate)

        plt.legend(['Time spent (s)', 'Solves'])
        plt.show()