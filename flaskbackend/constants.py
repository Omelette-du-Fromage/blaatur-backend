entur_journey_url = "https://api.entur.io/journey-planner/v3/graphql"

entur_autocomp_url = "https://api.entur.io/geocoder/v1/autocomplete"

entur_query = """query JarleMann($tomann: String!, $frommann: String!, $startDate: DateTime){
  trip(
    from: {place: $frommann}
    to: {place : $tomann}
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
      walkDistance
          legs {
            expectedStartTime
            expectedEndTime
            mode
            distance
            fromPlace {
              name
            }
            toPlace {
              name
            }
            line {
              id
              publicCode
              authority{
                name
              }
              presentation {
              colour
              textColour
          }
          description
            }
          }
    }
    debugOutput{totalTime}
  }
}"""
