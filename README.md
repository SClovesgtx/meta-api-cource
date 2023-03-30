

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
        - 100-199: informational
        - 200-299: successful responses
        - 300-399: redirection information
        - 400-499: client error responses (ex: bad API request, resource that is not on the server)
        - 500-599: server error (ex: error checks issues, configuration mismatch, package dependencies issues)