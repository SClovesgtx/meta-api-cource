

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

# REST 

Is an architectural style for design APIs. It is very popular for its simplicity:

- Easy to learn
- Quick to develop

To an API be RESTfull it must satisfy:

- **Client-server**
- **Stateless**: do not depend of previous states.
- **Cacheable**: possibility to chace response on the browser.
- **Layered**: you application could be split into layers and each layer could be chance (firewall, load balancer, web server, database server, etc).
- **Uniform interface** 
- **Optional code on demand**: Business logic, code that can improve results.

# Naming conventions

Naming your API properly is the first step in designing a good API. When the API name follows a convention, it provides lots of information about the API and its purpose. To create a meaningful API endpoint, you need to follow some simple guidelines and rules. 

**Vocabulary**: Uniform Resource Identifier (URI) = Endpoint = URL path.

There are some conventions:

- endpoint names must be in lowercase (```/orders``` and not ```/Orders```)
- Hyphens in between words (ex: ```/menu-items```)
- if your endpoint except parameters, you can represent them in Camel case (ex: ```orders/{orderId}/menu-items```).

Use forward slash (```/```) to indicate hierarchical relationships between related objects.

For example, a library has books, and books has authors:

```/library/books/{bookID}/author```

To get all books by an author:

```/library/authors/{authorName}/books```

You must use nouns instead of verbs. The following are some bad examples:

- ```/getAllBooks```
- ```/getUser/{userId}```
- ```users/{userId}/delete```
- ```/orders/{orderId}/save```

Do not specify the response format as part of the name endpoint like ```orders/{orderId}.json```, instead you could expect a query string that specify the data format response like ```/orders/{orderId}?format=json```.

For minified version of a JavaScript file you could use ```assets/js/jquery/3.6.0/min``` or ```assets/js/moment/2.29.4/original```.

Do not end your endpoint name with a forward slash (ex: ```/orders/{orderId}/```).

# REST best practices

- Principle KISS (keep it simple stupid): the idea is that your API need to do one specific simple job. 
- Always provide a way to filter, order and paginate. 
    - Pagination: your API will be able to send results in small chunks.
- Versioning your API
- Caching: your API must be able to cache results, in this way, you save resources in case to provide same answer.
- Rate limiting and monitoring: to prevent abuse of use.
    - limits call: number of calls per minute, or day. 
    - monitoring 
        - response time
        - status code