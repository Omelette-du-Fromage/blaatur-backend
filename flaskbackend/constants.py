
entur_journey_url = "https://api.entur.io/journey-planner/v2/graphql"

entur_autocomp_url = "https://api.entur.io/geocoder/v1/autocomplete"

entur_query = """query JarleMann($tomann: String!, $frommann: String!){
  trip(
    from: {place: $frommann}
    to: {place : $tomann}
    numTripPatterns: 1
  )

#### Requested fields
  {
    tripPatterns {
      startTime
      duration
      walkDistance

          legs {
            mode
            distance
            line {
              id
              publicCode
              authority{
                name
              }
            }
          }
    }
    debugOutput{totalTime}
  }
}"""