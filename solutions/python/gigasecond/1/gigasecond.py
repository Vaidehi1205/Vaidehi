from datetime import datetime, timedelta

def add(moment):
    gigasecond_later = moment + timedelta(seconds=10**9)

    return gigasecond_later

