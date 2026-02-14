# API Gateway
- is a bridge to connenct a client and server.
- helps to mask the server details (backend).
- Since it act as an intermediate, we can add the authentication and other securitys.

### Custom Domain Name:
 A custom name to call the api in the gateways. We have to provide a mapping to the apis. So that invoking the custom domain with the appropriate path will route to the right api

 ### Resources
 1. It is where the methods of an api is defined.
 2. Each method can have its own integration.

### Stages
It is for testing the apis in the right environment.
It helps to avoid creating multiple same apis for different environment.

### Authorizer
An api can have its own authorizer. the authorizer can be none, AWS IAM auth or an auth lambda.
These helps to authorize or thransform the incomming request. and block any invalid request.

