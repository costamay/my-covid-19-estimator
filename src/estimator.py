import math
from .infectionsByRequestedTime import infectionsByRequestedTime
from .impact import impactdata
from .servereImpact import severe



def estimator(data):
      
      return {
        "data": data,
        "impact": {
          'currentlyInfected':  impactdata(),
          'infectionsByRequestedTime': impactdata() * (2 ** infectionsByRequestedTime())
            }, 
        "severeImpact": {
          'currentlyInfected': severe(),
          'infectionsByRequestedTime': severe() * (2 ** infectionsByRequestedTime())
          }
       }

