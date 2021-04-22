entur_journey_url = "https://api.entur.io/journey-planner/v3/graphql"

entur_autocomp_url = "https://api.entur.io/geocoder/v1/autocomplete"

entur_query = """query($from: String!, $to: String!, $fromDate: DateTime!){
  trip(
    modes: {
      accessMode: foot
      transportModes: [{transportMode: bus}, 
        {transportMode: water},
        {transportMode: rail},
      	{transportMode: metro}
      ]
    }
    
    from: {place: $frommann}
    to: {place : $tomann}
    dateTime: $startDate
    
    searchWindow: 400
    numTripPatterns: 1
  )

#### Requested fields
  {
    tripPatterns {
      expectedStartTime
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
