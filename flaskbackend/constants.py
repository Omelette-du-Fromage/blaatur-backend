entur_journey_url = "https://api.entur.io/journey-planner/v3/graphql"

entur_autocomp_url = "https://api.entur.io/geocoder/v1/autocomplete"

entur_query = """query EnturQuery($from: String!, $to: String!, $startDate: DateTime!){
  trip(
    modes: {
      accessMode: foot
      transportModes: [{transportMode: bus}, 
        {transportMode: water},
        {transportMode: rail},
      	{transportMode: metro}
      ]
    }
    
    from: {place: $from}
    to: {place : $to}
    dateTime: $startDate
    searchWindow: 400
    numTripPatterns: 1
  )

#### Requested fields
{
    metadata{
        searchWindowUsed
        nextDateTime
    }
    
    tripPatterns {
      startTime
      duration
          legs {
            expectedStartTime
            expectedEndTime
            mode
            fromPlace {
              name
            }
            toPlace {
              name
            }
            line {
              authority{
                name
              }
            }
          }
    }
  }
}"""
