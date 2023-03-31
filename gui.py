import tkinter as tk
from tkinter import filedialog

import analyser as an
import overallStats as os

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('400x400')
        self.window.title('csTimer Analyst')

        # --- Frames ---
        header = tk.Frame(self.window)
        stats = tk.Frame(self.window)
        graphs = tk.Frame(self.window)

        header.pack(side='top', padx=50)
        stats.pack(side='top', pady=10)
        stats.columnconfigure(0, minsize=200)
        graphs.pack(side='bottom', pady=50)

        # --- Header ---
        logo = tk.Label(header, text='csTimer Analyst', font=('Bahnschrift', 28))
        logo.pack(pady=10)

        self.fileLabel = tk.Label(header, text='Choose your session file')
        self.fileLabel.pack(side='left')
        browseButton = tk.Button(header, text='Browse', command=self.BrowseFiles)
        browseButton.pack(side='right')

        # --- Stats ---
        meanText = tk.Label(stats, text='Total mean:')
        meanText.grid(row=0, column=0, sticky='w')
        self.mean = tk.Label(stats, text='0')
        self.mean.grid(row=0, column=1, sticky='w')

        pbText = tk.Label(stats, text='PB:')
        pbText.grid(row=1, column=0, sticky='w')
        self.pb = tk.Label(stats, text='0')
        self.pb.grid(row=1, column=1, sticky='w')
        
        timeSpentText = tk.Label(stats, text='Total time spent:')
        timeSpentText.grid(row=2, column=0, sticky='w')
        self.timeSpent = tk.Label(stats, text='0')
        self.timeSpent.grid(row=2, column=1, sticky='w')

        daysInARowText = tk.Label(stats, text='Most days in a row:')
        daysInARowText.grid(row=3, column=0, sticky='w')
        self.daysInARow = tk.Label(stats, text='0')
        self.daysInARow.grid(row=3, column=1, sticky='w')

        daysBreakText = tk.Label(stats, text='Most days break:')
        daysBreakText.grid(row=4, column=0, sticky='w')
        self.daysBreak = tk.Label(stats, text='0')
        self.daysBreak.grid(row=4, column=1, sticky='w')

        self.mostSolves = tk.Label(stats, text='', justify='left')
        self.mostSolves.grid(row=5, column=0, sticky='w')

        # --- Graph buttons ---
        # todo: implement arguments like in the cli version
        self.timesGraph = tk.Button(graphs, text='Times graph', width=12)
        self.timesGraph.grid(row=0, column=0, padx=5)
        self.solvesByDateGraph = tk.Button(graphs, text='Solves by date', width=12)
        self.solvesByDateGraph.grid(row=0, column=1, padx=5)
        self.subchart = tk.Button(graphs, text='Sub chart', width=12)
        self.subchart.grid(row=0, column=2, padx=5)
        #! Since analyser is initialized after loading a file commands are set in ConfigureGraphButtons()

        self.window.mainloop()

    def BrowseFiles(self):
        fileName = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV files", "*.csv"),))
        if fileName != '' and fileName.split('.')[-1] == 'csv':
            self.fileLabel.configure(text=fileName.split('/')[-1]) #? will this work on linux?
            self.ShowValues(fileName)
            self.ConfigureGraphButtons()

    def ConfigureGraphButtons(self):
        self.timesGraph.configure(command=self.analyser.ShowTimesGraph)
        self.solvesByDateGraph.configure(command=self.analyser.ShowSolvesByDayGraph)
        self.subchart.configure(command=self.analyser.ShowSubChart)

    def ShowValues(self, fileName):
        self.analyser = an.Analyser(fileName)

        self.mean.configure(text=os.SecondsToTime(self.analyser.mean))
        self.pb.configure(text=os.SecondsToTime(self.analyser.pb))
        self.timeSpent.configure(text=self.analyser.totalTimeSpent)
        self.daysInARow.configure(text=self.analyser.mostDaysInARow)
        self.daysBreak.configure(text=self.analyser.mostDaysBreak)
        mostSolvesDate = self.analyser.allDays[self.analyser.totalSolvesByDate.index(max(self.analyser.totalSolvesByDate))]
        timeSpentOnMostSolves = os.SecondsToTime(self.analyser.totalTimeByDate[self.analyser.totalSolvesByDate.index(max(self.analyser.totalSolvesByDate))])
        self.mostSolves.configure(text='The most solves (' + str(max(self.analyser.totalSolvesByDate)) + ') were done on ' + str(mostSolvesDate) + '.\n The total time spent that day is ' + timeSpentOnMostSolves)

if __name__ == '__main__':
    GUI()