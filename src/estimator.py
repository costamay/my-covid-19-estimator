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
      
      
      
      
