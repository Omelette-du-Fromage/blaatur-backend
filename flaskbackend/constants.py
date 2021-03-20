entur_journey_url = "https://api.entur.io/journey-planner/v3/graphql"

entur_autocomp_url = "https://api.entur.io/geocoder/v1/autocomplete"

entur_query = """query JarleMann($tomann: String!, $frommann: String!){
  trip(
    from: {place: $frommann}
    to: {place : $tomann}
    numTripPatterns: 1
    searchWindow: 1440
  )

#### Requested fields
  {
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
