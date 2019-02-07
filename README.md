# Mozio

### API documentation:

#### Providers:
 - Provider list:
   - Endpoint: /providers/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/providers/
   - Method: GET
 - Provider detail:
   - Endpoint: /providers/&lt;id&gt;/
   - Example URL:
   - Method: GET
 - Provider update:
   - Endpoint: /providers/&lt;id&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/providers/1/
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
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/
   - Method: GET
 - Service area detail:
   - Endpoint: /service-areas/&lt;id&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/1/
   - Example:
   - Method: GET
 - Service area update:
   - Endpoint: /service-areas/&lt;id&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/1/
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
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/?lat=1.323423&long=1.2323123
   - Method: GET
   
   
### Infrastructure and details:
  - AWS EC2
  - PostgreSQL (PostGIS)
  - Nginx
  - Gunicorn

