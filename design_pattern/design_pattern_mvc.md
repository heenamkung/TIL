# MVC
Design pattern consists of model, view and controller.

```
    ==> (User Action)         ==> (Update)
View                Controller              Model       
        <== (Update)          <== (Notify)
```
1 to n relation between controller and view


## Model
- Handles data storage and retrieval
- Application's data including database, constants and variables
1. Add/edit data in view
2. Controller creates or updates model

## View 
- Responsible for displaying data and capturing user input (frontend: html, css, js in web applications)
- Views are UIs such as Inputbox, checkbox, textarea that users get to see depending on the model
- Views cannot save info about the model's data and must report changes in view to the controller 

## Controller
- Processes data, interacts with model to save it in a database
- A bridge that connects the model and view
- Handles events and all the main business logics
- Manages lifecycle of model and views

## Pros and Cons
Pros
- Developers can focus on each element (m, v, c) of the design pattern
- Reusable and scalable

Cons
- MVC becomes complicated as application grows in size

Example:
Spring WEB MVC


# MVP
Design pattern consists of model, view and presenter. Similar to MVC but with presenter instead of controller and 1:1 relation between view and presenter.

```
    ==> (User Action)         ==> (Update)
View                Presenter            Model       
        <== (Update)          <== (Notify)
```

# MVVM
Design pattern consists of model, view and view model. Similar to MVC but with view model instead of controller and 1:n relation between view model and view.

Example: 
Vue.js