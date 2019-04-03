# RESTful API template

My own simple RESTful API structure implemented in Python.

## Usage

Simply change the `TODO` contents in [startserver.py](https://github.com/RainBoltz/RESTful-API-template/blob/master/startserver.py).

[index.html](https://github.com/RainBoltz/RESTful-API-template/blob/master/index.html) also shows how a website interact with python-based server with JavaScript ([jQuery](https://jquery.com/) Ajax was used).

## About RESTful

something you should know about RESTful structure...

### 1. Protocol

The protocol between the API server and client should always be the HTTPs protocol.

### 2. Domain Name

Usually we name the API as a dedicated domain name.

```diff
https://api.example.org/
```

If the API is simple and wouldn't scale up in the future, we can place it under the main domain name.

```
https://example.org/api/
```

### 3. Versioning

The version number of the API should be placed in the URL.

```
https://example.org/api/v1
```

### 4. Endpoint

In a RESTful structure, each URL represents a resource, so there should be no verbs in the URL, only nouns, and the nouns were often corresponded to the table names in the database.
In general, the tables in the database are "collections" of the same kind of records, so the nouns in the API should be using plurals.

```
https://example.org/api/v1/users
https://example.org/api/v1/items
...
```

### 5. HTTP methods

HTTP method shows us the operation type of a resource.

  * **GET (_SELECT_)**: Take the resource (one or more) from the server.
  * **POST (_CREATE_)**: Create a new resource on the server.
  * **PUT (_UPDATE_)**: Update the resource on the server (the client provides the full resource that have been changed).
  * **PATCH (_UPDATE_)**: Update the resources on the server (the client provides the properties that should be changed).
  * **DELETE (_DELETE_)**: Delete resources from the server.
  * **HEAD**: Get the metadata of the resource.
  * **OPTIONS**: Get information about which properties of a resource can be changed by the client.

### 6. Filtering

In most of the time, the server may not want to return all of the records to the client.
So the API should provide parameters, then filter the results back.

For example,

  * `?limit=10`: Specifies the amount of records returned
  * `?offset=10`: Specifies the starting position of the returned record.
  * `?page=2&per_page=100`: Specify the index of the pages and the amount of records per page.
  * `?item_name=name`: Specifies the name of the returned record.

Also, the design of the API paths and URL parameters should allow occasional duplications:

  * `GET /market/ID/items` has the same meaning as `GET /items?market_id=ID`

### 7. Status Codes

| Code | Status | Methods | description |
|:---:|:--------------------:|:-----:|------------------------------------------------------------------------------------------|
|200|OK|GET|The server successfully returns the data requested by the user, which is idempotent.|
|201|CREATED|POST PUT PATCH|The user successfully created or modified the data.|
|202|ACCEPTED|\*|Indicates that a request has entered the background queue (asynchronous task)|
|204|NO CONTENT|DELETE|The user deleted the data successfully.|
|400|INVALID REQUEST|POST PUT PATCH|The request sent by the user has an error. The server does not perform the operation of creating or modifying data. The operation is idempotent.|
|401|UNAUTHORIZED|\*|Indicates that the user does not have permission (token, username, password is incorrect).|
|403|FORBIDDEN|\*|indicates that the user is authorized (as opposed to 401 error), but access is prohibited.|
|404|NOT FOUND|\*|The request sent by the user is for a record that does not exist. The server does not operate, and the operation is idempotent.|
|406|NOT ACCEPTABLE|GET|The format requested by the user is not available (for example, the user requests the JSON format, but only the XML format).|
|410|GONE|GET|The resource requested by the user is permanently deleted and will not be retrieved.|
|422|UNPROCESSABLE ENTITY|POST PUT PATCH|A validation error occurred while creating an object.|
|500|INTERNAL SERVER ERROR|\*|An error occurred on the server and the user will not be able to determine if the request was successful.|

### 8. Error handling

Generally, in the returned information, "**error**" is used as the key name, and the error information is used as the key value.

```javascript
{
    error: "Invalid API key"
}
```

### 9. Returns

* `GET /collection`: Returns a list of resource objects (array).
* `GET /collection/resource`: Return a single resource object.
* `POST /collection`: Returns the newly generated resource object.
* `PUT /collection/resource`: Returns the full resource object.
* `PATCH /collection/resource`: Returns the full resource object.
* `DELETE /collection/resource`: Returns an empty document (null).

### 10. Hypermedia API

The RESTful API is best done in Hypermedia, which provides links to the results, and links to other API methods so that users don't have to check the documentation frequently as they know what to do next.

For example, when a user makes a request to the root of api.example.com, they get a document like this:

```
{"link": {
  "rel":   "collection https://www.example.com/collections",
  "href":  "https://api.example.com/collections",
  "title": "List of collections",
  "type":  "application/vnd.yourformat+json"
}}
```

The above code indicates that there is a link attribute in the document. The user reads the attributes and knows what API to call next. "**Rel**" indicates the relationship between the API and the current URL (collection relationship, and gives the URL of the collection), "**href**" indicates the path of the API, title indicates the title of the API, and type indicates the return type.

The design of the Hypermedia API is called **[HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)** . [Github's API](https://api.github.com/) is well designed inthe  HATEOAS structure, accessing it will get a list of URLs for all available APIs.



## Contributing

reference: http://www.ruanyifeng.com/blog/2014/05/restful_api.html



