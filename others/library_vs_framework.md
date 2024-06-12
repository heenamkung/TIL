# Library vs Framework
Both are external code written by other people that are used to improve our project

## Differences: who is in control?
### Library
- User has complete control over the code. You call libraries as needed, and you have control over the flow of the application.
- Example: jQuery
- Easily replaceable. Can replace jQuery with some other library without breaking the project
### Framework
- Framework has control over user. Frameworks enforce a specific way of doing things, which can accelerate development but also impose restrictions. 
- It has guidelines on where to put the code, where to put the template, where to put the template, etc. Must follow these guidelines in order to work properly
- Example: django. To have an admin panel, it must be coded in admin.py. To change an URL, it must be edited in url.py.