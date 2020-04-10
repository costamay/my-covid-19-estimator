import math


def infectionsByRequestedTime(data):
    if data['periodType'] == 'days':
        return math.floor((int(data['timeToElapse']))/3)
    elif data['periodType'] == 'weeks':
        return math.floor((int(data['timeToElapse']) * 7)/3)
    return math.floor((int(data['timeToElapse']) * 30)/3)