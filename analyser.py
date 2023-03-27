import pandas as pd
from matplotlib import pyplot as plt
from datetime import timedelta, datetime as dt

import times as times
import overallStats as os

class Analyser:
    def __init__(self, fileName):
        self.df = pd.read_csv(fileName, delimiter=';')

        self.singles = times.TimesToFloats(self.df['Time'])
        self.mean = sum(self.singles) / len(self.singles)
        self.pb = min(self.singles)    
        self.totalTimeSpent = os.SecondsToTime(sum(self.singles))
        self.allDays, self.totalTimeByDate, self.totalSolvesByDate = os.GetSessionStats(self.df)
        self.mostDaysInARow, self.mostDaysBreak = os.GetDaysInARow(self.df, self.allDays)

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

    def ShowSubChart(self):
        subs = []
        values = []
        for i in range(0, 60, 5):
            subSolves = [time for time in self.singles if time < i + 5 and time >= i]
            if len(subSolves) > 0:
                values.append(len(subSolves))
                subs.append('sub' + str(i + 5))

        # Since the loop only takes solves between two sub levels (e.g. sub15 are solves between 10 and 15)
        # and over60 solves don't have an upper ceiling they have to be handled differently
        overSixty = [time for time in self.singles if time >= 60]
        if len(overSixty) > 0:
            subs.append('over 60')
            values.append(len(overSixty))

        plt.pie(values, labels=subs)
        plt.show()
