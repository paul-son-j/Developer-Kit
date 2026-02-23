# Why?
In old days to create any web application, we have to
- write Servlets
- create xml web page
- deploy the war files into the external server (Tomcat)
- manage dependency.

With the introduction of spring it reduced the boilerplate code and reduce the time for production ready code.

# Web application
Any system that provided response by doing some bussiness logic in behind scene for the request.

1. browser send request
2. server receives request
3. server perform bussiness logic
4. server gives response

In java something listens to the http request.
That is Servlet container (Tomcat).

# Spring
- Create objects and manages object for us.
- Manage dependencies
- handles request 
- manages Database connection
- provides Security

With spring manages everything we can focus on bussiness logic.

# SpringBoot
Spring + AutoConfiguration + Embeded Servlet + Other opiniated defaults

i.e: no external servelet, web xml, or configuration
Just run.
