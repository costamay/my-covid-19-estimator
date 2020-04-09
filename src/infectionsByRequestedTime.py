import math
def infectionsByRequestedTime(data):
    if data.periodType is 'days':
        return math.floor((data.timeToElapse)/3)
    elif data.periodType is 'weeks':
        return math.floor((data.timeToElapse * 7)/3)
    return math.floor((data.timeToElapse * 30)/3)