## Simple Feed API

A simple CRUD system which stores unicode text messages posted to the system and returns them with a paginated feed.

### Components used
1. Python FastAPI framework  
2. Redis (persistance) 
3. Poetry dependency management
4. Docker  
5. OpenAPI and Redoc  

### Current functionality
1. Run the services with a `docker-compose up`
2. POST messages to the system, one at a time
3. GET messages from the system, configurable pagination
4. List Retrieval is supported

### Possible upgrades
1. Support other data formats (json, xml, protobuf)
2. Add a proxy server `nginx` to enable production use cases
3. Add a `locust` script to performance test
4. Add `pytest` unit tests to validate the business logic
5. Add `hypothesis` to trial property-based testing

### Alternative solutions
1. Use `nginx` infront of `Elasticsearch` for similar functionlity
2. Explore `tarantool` with its embedded http client support