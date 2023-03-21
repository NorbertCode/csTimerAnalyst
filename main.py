import pandas as pd
from matplotlib import pyplot as plt

import timesFunctions as tf

if __name__ == "__main__":
    df = pd.read_csv('v_perm.csv', delimiter=';')

    # --- Solving times ---
    plt.plot(df['No.'],df['Time'])

    plt.plot(df['No.'], tf.CalculateAO(df['Time'].tolist()))
    plt.plot(df['No.'], tf.CalculateAO(df['Time'].tolist(), 12))

    timeNumbers, personalbests = tf.PersonalBestProgression(df['Time'].tolist())
    plt.plot(timeNumbers, personalbests)

    plt.legend(["single", "ao5", "ao12", "pb"])
    plt.show()

    # --- Time spent solving ---
