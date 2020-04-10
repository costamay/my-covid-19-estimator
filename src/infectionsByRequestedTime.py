import math


def infectionsByRequestedTime(data):
    if data['periodType'] == 'days':
        return ((int(data['timeToElapse']))/3)
    elif data['periodType'] == 'weeks':
        return ((int(data['timeToElapse']) * 7)/3)
    return ((int(data['timeToElapse']) * 30)/3)