def CalculateAverage(times):
    # Cubing average is calculated by removing the worst and best time, and calculating the mean of the rest
    times.remove(min(times))
    times.remove(max(times))

    return round(sum(times) / len(times), 2)

def CalculateAO(times, ao = 5):
    averages = []

    for i in range(0, len(times)):
        if i >= ao - 1:
            averages.append(CalculateAverage(times[i - (ao - 1):i + 1])) # Get the newest and (ao-1) previous times

            # todo: debug only - remove this later
            if i < 10:
                print(times[i - (ao - 1):i + 1], CalculateAverage(times[i - (ao - 1):i + 1]), "\n")
        else:
            averages.append(times[0])

    return averages

def PersonalBestProgression(times):
    timeNumbers = [] # The number of the solves, so you can see after how many solves a pb was beaten
    personalbests = []

    for i in range(len(times)):
        if (len(personalbests) == 0 or times[i] < personalbests[len(personalbests) - 1]):
            timeNumbers.append(i)
            personalbests.append(times[i])

    return timeNumbers, personalbests