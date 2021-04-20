entur_journey_url = "https://api.entur.io/journey-planner/v3/graphql"

entur_autocomp_url = "https://api.entur.io/geocoder/v1/autocomplete"

entur_query = """{
  trip(
    from: {name: "Bjerkealleen 5A, Skedsmo"
    coordinates: {
      latitude: 59.96050414081307
      longitude:11.040338686322317
    }}

    to: {
      place:"NSR:StopPlace:5532"
      name:"Dyrløkke, Frogn"
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
