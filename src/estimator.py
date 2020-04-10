import math
from .infectionsByRequestedTime import infectionsByRequestedTime
from .impact import impact
from .servereImpact import severeImpact



def estimator(data):
      
      return {data,
               impact: {
                 'currentlyInfected':  impact(),
                 'infectionsByRequestedTime': impact() * (2 ** infectionsByRequestedTime())
                  }, 
               severeImpact: {
                 'currentlyInfected': severeImpact(),
                 'infectionsByRequestedTime': severeImpact() * (2 ** infectionsByRequestedTime())
                  }
               }

