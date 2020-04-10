from .infectionsByRequestedTime import infectionsByRequestedTime
from .impact import impactdata
from .servereImpact import severe


def estimator(data):
      
      return {
        "data": data,
        "impact": {
          'currentlyInfected':  impactdata(data),
          'infectionsByRequestedTime': impactdata() * (2 ** infectionsByRequestedTime(data))
            }, 
        "severeImpact": {
          'currentlyInfected': severe(),
          'infectionsByRequestedTime': severe() * (2 ** infectionsByRequestedTime(data))
          }
       }

