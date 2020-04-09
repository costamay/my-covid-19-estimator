import math
from .infectionsByRequestedTime import infectionsByRequestedTime
from .impact import impact
from .servereImpact import severeImpact


def estimator(data):
      
      impact = {
        'currentlyInfected': impact,
        'infectionsByRequestedTime': impact * (2 ** infectionsByRequestedTime)
      }
      
      severeImpact = {
        'currentlyInfected': severeImpact,
        'infectionsByRequestedTime': servereImpact * (2 ** infectionsByRequestedTime)
      }
      return {data, impact, severeImpact}

