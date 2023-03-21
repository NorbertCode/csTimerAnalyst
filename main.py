import pandas as pd
from matplotlib import pyplot as plt

def CalculateAverage(list):
    # Cubing average is calculated by removing the worst and best time, and calculating the mean of the rest
    list.remove(min(list))
    list.remove(max(list))

    return round(sum(list) / len(list), 2)

def CalculateAO(list, n = 5):
    ao = []

    for i in range(0, len(list)):
        if i >= n - 1:
            ao.append(CalculateAverage(list[i - (n - 1):i + 1]))

            # todo: debug only - remove this later
            if i < 10:
                print(list[i - (n - 1):i + 1], CalculateAverage(list[i - (n - 1):i + 1]), "\n")
        else:
            ao.append(list[0])

    return ao

def PersonalBestProgression(list):
    timeNumbers = [] # The number of the solves, so you can see after how many solves a pb was beaten
    personalbests = []

    for i in range(len(list)):
        if (len(personalbests) == 0 or list[i] < personalbests[len(personalbests) - 1]):
            timeNumbers.append(i)
            personalbests.append(list[i])

    return timeNumbers, personalbests

df = pd.read_csv('v_perm.csv', delimiter=';')

plt.plot(df['No.'],df['Time'])

plt.plot(df['No.'],CalculateAO(df['Time'].tolist()))
plt.plot(df['No.'],CalculateAO(df['Time'].tolist(), 12))

timeNumbers, personalbests = PersonalBestProgression(df['Time'].tolist())
plt.plot(timeNumbers, personalbests)

plt.legend(["single", "ao5", "ao12", "pb"])
plt.show()