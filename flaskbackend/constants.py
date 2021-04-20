entur_journey_url = "https://api.entur.io/journey-planner/v3/graphql"

entur_autocomp_url = "https://api.entur.io/geocoder/v1/autocomplete"

entur_query = """query($from: String!, $to: String!){
  trip(
    from: {
        place: $from 
    }

    to: {
      place: $to
    }
    
    
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
  }
}"""
