from matplotlib import pyplot as plt

def TimesToFloats(times):
    floatTimes = []
    for i in times:
        # Remove csTimer's special characters
        parsedString = str(i).replace('+', '')
        parsedString = parsedString.replace('*', '')

        parsedTimes = [float(x) for x in parsedString.split(':')] # If a time is less than a minute (so in a format like 12.45) it's automatically taken as a float
        for j in range(len(parsedTimes)):
            if j < len(parsedTimes) - 1:
                parsedTimes[j + 1] += parsedTimes[j] * 60

        floatTimes.append(parsedTimes[-1])

    return floatTimes

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