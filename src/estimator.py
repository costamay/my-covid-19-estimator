from .infectionsByRequestedTime import infectionsByRequestedTime
from .impact import impactdata
from .servereImpact import severe


def estimator(data):
      
      return {
        "data": data,
        "impact": {
          'currentlyInfected':  impactdata(data),
          'infectionsByRequestedTime': impactdata(data) * (2 ** infectionsByRequestedTime(data))
            }, 
        "severeImpact": {
          'currentlyInfected': severe(data),
          'infectionsByRequestedTime': severe(data) * (2 ** infectionsByRequestedTime(data))
          }
       }

