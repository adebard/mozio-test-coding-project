# Mozio

### API documentation:

#### Providers:
 - Provider list:
   - Endpoint: /providers/
   - Example URL:
   - Method: GET
 - Provider detail:
   - Endpoint: /providers/&lt;id&gt;/
   - Example URL:
   - Method: GET
 - Provider update:
   - Endpoint: /providers/&lt;id&gt;/
   - Example URL:
   - Method: POST
   - Example payload:
     ```{
      "name": "Test",
      "email": "test@mail.com",
      "phone_number": "2450319",
      "language": "EN",
      "currency": "USD"}

#### Service Areas:
 - Service areas list:
   - Endpoint: /service-areas/
   - Example URL:
   - Method: GET
 - Service area detail:
   - Endpoint: /service-areas/&lt;id&gt;/
   - Example URL:
   - Example:
   - Method: GET
 - Service area update:
   - Endpoint: /service-areas/&lt;id&gt;/
   - Example URL:
   - Method: POST
   - Example payload:
     ```{
     "provider_name": "Test",
     "name": "Area for test",
     "price": "25.00",
     "area": {
        "type": "Polygon",
        "coordinates": [
            [
                [
                    135.0,
                    45.0
                ],
                [
                    140.0,
                    50.0
                ],
                [
                    145.0,
                    55.0
                ],
                [
                    135.0,
                    45.0
                ]
            ]
        ]
     },
     "provider": 1
     }
     ```
- Search service area:
   - Endpoint: /service-areas/?lat=&lt;lat&gt;&long=&lt;long&gt;
   - Example URL:
   - Method: GET
