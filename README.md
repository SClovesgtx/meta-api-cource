

# HTTP

- HTTP(S) = Hyper Text Transfer Protocol (security)
- In HTTPS the client computer encrypts the data before sending it to the server. The server decrypts the data request to process it and send back a encrypt response. The client browser decrypt the response to exhibit it to you.
- HTTP Methods (verbs):
    * **GET**: retrieve a resource
    * **POST**: create a resource
    * **PUT**: update all resource
    * **PATCH**: update part of resource
    * **DELETE**: delete the resource
- HTTP requests contain:
    * HTTP Version Type
    * URL (path)
    * Method (verb)
    * Headers: is part of all HTTP request and contain extra information thats helps the server how to present the content (ex: cookies, user-agents, referrers).
    * Body (optional): used to transfer data in json format or in the encoded URL.
- HTTP response contain:
    * Request resource
    * Content length
    * Content type
    * Headers
    * ETags
    * Time last modification
    * HTPP status code:
        - **100-199**: informational. This range is mainly used to pass on some information. For example, sometimes an API needs time to process the request and it can’t instantly deliver the result. In such a case, the API developer can set it to keep returning 102 – Processing until the result is ready. This way, the client understands that the result isn’t ready and should be checked again.
        - **200-299**: successful responses
        - **300-399**: redirection information. Suppose as an API developer, you changed the API endpoint from /api/items to api/menu-items. If the client makes an API call to /api/items, then you can redirect the client to this new endpoint /api/menu-items with a 301 – Permanently moved status code so that the client can make new calls to that endpoint next time.  
        - **400-499**: client error responses (ex: bad API request, resource that is not on the server)
            * **404 - Not Found** if the client requests something that doesn’t exist
            * **400 - Bad Request** if a client sends an invalid payload with insufficient data
            * **401 - Unauthorized**
            * **403 - Forbidden** if the client tries to perform an action it's not authorized for.
        - **500-599**: server error (ex: error checks issues, configuration mismatch, package dependencies issues). These alarming status codes are usually automatically generated on the server side if something goes wrong in the code, and the API developer doesn't write code to deal with those errors. For example, a client requests a non-existing resource, and the API developer tries to display that resource without adequately checking if that resource exists in the database. Or if the API developer didn't validate the incoming data and attempted to create a new resource with invalid or insufficient data. You, as an API developer, should always avoid 5xx errors.  

## Response types
These days, the most common response types involved with REST APIs are JSON, XML, plain text, and sometimes YAML. Frameworks like DRF come with built-in renderer classes that can convert the data into an appropriate format and display it correctly.

There are also third-party renderers available for this job. While making an API call, the client can specify its desired response format with the **Accept HTTP header**. And that header should be considered to deliver the result in that format using the render classes. Here’s a list of HTTP headers for different response types. 

| Response type   |                       Request header                           |
|-----------------|:--------------------------------------------------------------:|
| HTML            |                     Accept: text/html                          |
| XML             |          Accept: application/xml, Accept: text/xml             |
| YAML | Accept: application/yaml,   Accept: application/x-yaml, Accept: text/yaml |