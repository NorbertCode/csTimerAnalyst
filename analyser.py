import pandas as pd
from matplotlib import pyplot as plt

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

    def ShowSubChart(self, intervals = 5):
        maxValue = int(round(max(self.singles), 0)) + intervals # intervals is added to make sure all singles are taken into account

        subs = []
        values = []
        for i in range(0, maxValue, intervals):
            subSolves = [time for time in self.singles if time < i + intervals and time >= i]
            if len(subSolves) > 0:
                values.append(len(subSolves))
                subs.append('sub' + str(i + intervals))

        plt.pie(values, labels=subs, autopct=lambda x: '{:.0f}'.format(x * sum(values) / 100), startangle=90)
        plt.show()
