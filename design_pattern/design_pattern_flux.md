# Flux Pattern
Design pattern that controls unidirectional data flow
Made to solve the complexity of MVC pattern

```
Action -> Dispatcher -> Store -> View
```
1. Action: user scrolls or clicks which create events and passes it to dispatcher
2. Dispatcher: According to type of action, decides what to do (switch) and runs it. Pass it to store.
3. Store: Manage and saves status (user or application domain)
4. View: Interface that users see


Example: Redux