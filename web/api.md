# API
## API (Application Programming Interface)

It defines the methods and data formats that applications can use to communicate with each other. They provide a way for different software systems to interact in a standardized manner.
- An intermediary layer between computers. When two computers communicate, it is an intermediary layer where the communication protocol (HTTP/HTTPS), HTTP methods (GET/POST), and data types (JSON/XML) are defined.

## Interface

Interface is an intermediary layer between two different systems, devices that exchange data. Users can communicate with interfaces without knowing the logic behind the application

User Interface (UI)
- GUI - users interact with buttons and forms without understanding the code behind elements
- CLI - users input commands in a text-based interface, executing programs or scripts without knowing the internal logic

Application Programming Interface (API)
- RESTful API - Applications use HTTP methods (GET, POST, PUT, DELETE) to communcatie with web services, sending and receiving data in formats like JSON or XML
- Library API - Developers use APIs provided by libraries to perform specific functions such as mathematical computations, without needing to implement those functions from scratch

## Advantages
- API provider can hide unwatned parts of the service (DB architecture, DB table info)
- Users can retrieve data without having to know the logic behind the service
- Public APIs makes software development much faster (NAVER login api) 
- In case of internal update of an API, developers don't need to update the product (uploading updated version of an app)
- API provider can gather data in one place (gathering all users that click the best selling item and put it in a db. Use API to do it)

## Types of API
Public
- 
Private
- 