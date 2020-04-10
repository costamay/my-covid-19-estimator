from .infectionsByRequestedTime import infectionsByRequestedTime
from .impact import impactdata
from .servereImpact import severe
import math


def estimator(data):
      
      return {
        "data": data,
        "impact": {
          'currentlyInfected':  impactdata(data),
          'infectionsByRequestedTime': impactdata(data) * (2 ** infectionsByRequestedTime(data)),
          'severeCasesByRequestedTime': 15/100(impactdata(data) * (2 ** infectionsByRequestedTime(data))),
          'hospitalBedsByRequestedTime' : math.floor((35/100(data['totalHospitalBeds'])) -((15/100(impactdata(data))) * (2 ** infectionsByRequestedTime(data))))
            }, 
        "severeImpact": {
          'currentlyInfected': severe(data),
          'infectionsByRequestedTime': severe(data) * (2 ** infectionsByRequestedTime(data)),
          'severeCasesByRequestedTime': 15/100(severe(data) * (2 ** infectionsByRequestedTime(data))),
          'hospitalBedsByRequestedTime': math.floor((35/100(data['totalHospitalBeds'])) -((15/100(severe(data))) * (2 ** infectionsByRequestedTime(data))))
          }
       }

