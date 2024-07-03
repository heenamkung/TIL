# Design Pattern - Creational Pattern

## Types of Design Patterns
- Creational (생성패턴)
- *Structural (구조패턴)
- Behavioral (행동패턴)

## Structural
Deal with object composition or the way to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

Example: Proxy, Adapter

## Proxy Pattern
The Proxy Pattern is a structural design pattern that provides an object that acts as a substitute or placeholder for another object. 

A proxy controls access to the original object, allowing you to add a layer of control over the original object's functionality. 

This pattern is useful for various purposes, such as access control, logging, or caching.

E.g. Client accessing server
- Server is http server
- Put https proxy server between client and server.

E.g. Lots of traffic (or ddos)
- Traffic can increase drastically but it might not all be users
- Lots of them might be bots. Need a proxy server (cloudflare) to filter out the bots and block them.
