import tkinter as tk
from tkinter import filedialog

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('400x400')
        self.window.title('csTimer Analyst')

        # --- Frames ---
        header = tk.Frame(self.window)
        analysis = tk.Frame(self.window)
        stats = tk.Frame(self.window)
        graphs = tk.Frame(self.window)
        header.pack(side='top', padx=50)
        analysis.pack(side='top', padx=50)
        stats.pack(side='left', padx=50)
        graphs.pack(side='bottom')

        # --- Header ---
        logo = tk.Label(self.window, text='csTimer Analyst', font=('Bahnschrift', 28))
        logo.pack(in_=header, pady=10)

        self.fileLabel = tk.Label(self.window, text='Choose your session file')
        self.browseButton = tk.Button(self.window, text='Browse', command=self.BrowseFiles)
        self.fileLabel.pack(in_=header, side='left')
        self.browseButton.pack(in_=header, side='right')

        analyseButton = tk.Button(self.window, text='Analyse', width=40)
        analyseButton.pack(in_=analysis, pady=10)

        # --- Stats ---
        self.pb = tk.Label(self.window, text='PB:')
        self.pb.pack(in_=stats)
        self.timeSpent = tk.Label(self.window, text='Total time spent:')
        self.timeSpent.pack(in_=stats)
        self.daysInARow = tk.Label(self.window, text='Most days in a row:')
        self.daysInARow.pack(in_=stats)
        self.daysBreak = tk.Label(self.window, text='Most days break:')
        self.daysBreak.pack(in_=stats)

        self.window.mainloop()

    def BrowseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV files", "*.csv"),))
        if filename != '':
            self.fileLabel.configure(text=filename)

GUI()