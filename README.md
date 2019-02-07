# Mozio test coding project.

### API documentation:

#### Providers:
 - **Provider list**:
   - Endpoint: /providers/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/providers/
   - Method: GET
   - Success 200
   - Example response:
     ```
     [
         {
             "id": 1,
             "name": "Test",
             "email": "test@mail.com",
             "phone_number": "12345",
             "language": "EN",
             "currency": "USD"
          }
     ]
- **Provider detail**:
   - Endpoint: /providers/&lt;ID&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/providers/1/
   - Method: GET
   - Success 200
   - Example response:
     ```
     {
         "id": 1,
         "name": "Test",
         "email": "test@mail.com",
         "phone_number": "12345",
         "language": "EN",
         "currency": "USD"
     }
 - **Provider delete**:
   - Endpoint: /providers/&lt;ID&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/providers/1/
   - Method: DELETE
   - Success 204
 - **Provider create**:
   - Endpoint: /providers/&lt;ID&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/providers/1/
   - Method: POST
   - Success 201
   - payload:
     ```
     {
         "name": <string>,
         "email": <string>,
         "phone_number": <string>,
         "language": <string> (optional) default="EN",
         "currency": <string> (optional) default="USD"
     }
 - **Provider update**:
   - Endpoint: /providers/&lt;ID&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/providers/1/
   - Method: PUT
   - Success 200
   - Example payload:
     ```
      {
          "name": "Test",
          "email": "test@mail.com",
          "phone_number": "2450319",
          "language": "EN",
          "currency": "USD"
      }

#### Service Areas:
**Note**: The polygon area accept WKT and GeoJSON as input
 - **Service areas list**:
   - Endpoint: /service-areas/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/
   - Method: GET
   - Success 200
   - Example response:
   ```
   [
       {
           "id": 1,
           "provider_name": "Test",
           "name": "Area for test",
           "price": "200.00",
           "area": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        30.0,
                        10.0
                    ],
                    [
                        40.0,
                        40.0
                    ],
                    [
                        20.0,
                        40.0
                    ],
                    [
                        10.0,
                        20.0
                    ],
                    [
                        30.0,
                        10.0
                    ]
                ]
            ]
        },
        "provider": 1
       }
   ]
 - **Service area detail**:
   - Endpoint: /service-areas/&lt;ID&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/1/
   - Method: GET
   - Success 200
   - Example response:
   ```
    {
         "id": 1,
         "provider_name": "Test",
         "name": "Area for test",
         "price": "200.00",
         "area": {
          "type": "Polygon",
          "coordinates": [
              [
                  [
                      30.0,
                      10.0
                  ],
                  [
                        40.0,
                        40.0
                  ],
                  [
                      20.0,
                      40.0
                  ],
                  [
                      10.0,
                      20.0
                  ],
                  [
                      30.0,
                      10.0
                  ]
              ]
          ]
      }
 - **Service area delete**:
   - Endpoint: /service-areas/&lt;ID&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/1/
   - Method: DELETE
   - Success 204
 - **Service area create**:
   - Endpoint: /service-areas/&lt;ID&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/1/
   - Method: POST
   - Success 201
   - Payload:
     ```
      {
          "provider_name": <string>,
          "name": <string>,
          "price": <decimal>,
          "area": <WKT|GeoJSON>
      }
 - **Service area update**:
   - Endpoint: /service-areas/&lt;ID&gt;/
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/1/
   - Method: PUT
   - Success 200
   - Example payload:
     ```
      {
          "provider_name": "Test",
          "name": "Area for test",
          "price": "200.00",
          "area": {
          "type": "Polygon",
          "coordinates": [
              [
                  [
                      30.0,
                      10.0
                  ],
                  [
                        40.0,
                        40.0
                  ],
                  [
                      20.0,
                      40.0
                  ],
                  [
                      10.0,
                      20.0
                  ],
                  [
                      30.0,
                      10.0
                  ]
              ]
          ]
      }
- **Search service area given lat/long pair**:
   - Endpoint: /service-areas/?lat=&lt;LAT&gt;&long=&lt;LONG&gt;
   - Example URL: http://ec2-54-210-228-174.compute-1.amazonaws.com/service-areas/?lat=35&long=30
   - Method: GET
   - Success 200
   - Example response:
   ```
   [
       {
           "id": 1,
           "provider_name": "Test",
           "name": "Area for test",
           "price": "200.00",
           "area": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        30.0,
                        10.0
                    ],
                    [
                        40.0,
                        40.0
                    ],
                    [
                        20.0,
                        40.0
                    ],
                    [
                        10.0,
                        20.0
                    ],
                    [
                        30.0,
                        10.0
                    ]
                ]
            ]
        },
        "provider": 1
       }
   ]
   
   
### Infrastructure and details:
  - AWS EC2
  - PostgreSQL (PostGIS)
  - Nginx
  - Gunicorn
  
### Tests:
```python manage.py test```
