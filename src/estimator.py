# from .infectionsByRequestedTime import infectionsByRequestedTime
# from .impact import impactdata
# from .servereImpact import severe
# import math

def timeEstimate(data):
      if data['periodType'] == 'days':
            days = data['timeToElapse']
            
      if data['periodType'] == 'weeks':
            days = data['timeToElapse'] * 7
            
      if data['periodType'] == 'months':
            days = data['timeToElapse'] * 30
      return days
    
def estimator(data):
      currentlyInfectedImpact = int(data['reportedCases']) * 10
      currentlyInfectedSevereImpact = int(data['reportedCases']) * 50
      days = timeEstimate(data)
      
      return {
        "data": data,
        "estimate":{
          "impact":{
            "currentlyInfected": currentlyInfectedImpact
            "infectionsByRequestedTime": currentlyInfectedImpact * (2 ** (days // 3 )
            
            },
          "severeImpact":{
            "currentlyInfected":currentlyInfectedSevereImpact
            "infectionsByRequestedTime": currentlyInfectedSevereImpact * (2 ** (days // 3)
          }
        }
      }
      
      
      
      
# def estimator(data):
#       return {
#         "data": data,
#         "impact": {
#           'currentlyInfected':  impactdata(data),
#           'infectionsByRequestedTime': impactdata(data) * (2 ** infectionsByRequestedTime(data)),
#           'severeCasesByRequestedTime': (15/100 * (impactdata(data) * (2 ** infectionsByRequestedTime(data)))),
#           'hospitalBedsByRequestedTime': math.floor((35/100 * ((data['totalHospitalBeds']))) -((15/100 * (impactdata(data))) * (2 ** infectionsByRequestedTime(data))))
#             }, 
#         "severeImpact": {
#           'currentlyInfected': severe(data),
#           'infectionsByRequestedTime': severe(data) * (2 ** infectionsByRequestedTime(data)),
#           'severeCasesByRequestedTime': 15/100 * (severe(data) * (2 ** infectionsByRequestedTime(data))),
#           'hospitalBedsByRequestedTime': math.floor((35/100 * ((data['totalHospitalBeds']))) -((15/100 * (severe(data))) * (2 ** infectionsByRequestedTime(data))))
#           }
#        }

