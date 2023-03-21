# Converts the amount of seconds to a string in a format like 1:15.2
def secondsToTime(seconds):
    minutes = round(seconds // 60)
    seconds -= minutes * 60

    time = str(round(seconds, 2))
    if (minutes > 0):
        time = str(minutes) + ":" + time

    return time