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
    totalTimeSpent = os.secondsToTime(sum(df['Time']))
    print(totalTimeSpent)