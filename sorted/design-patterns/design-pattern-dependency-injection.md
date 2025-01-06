# Design Pattern - Dependency Injection

## What Is Definition of Dependency Injection

- Is a design pattern that mostly used in [**inversion of control**]() **framework**

## Features

There are 3 commonly used ways to implement dependency injection

- Constructor injection
- Property injection(Setter injection)
- Method injection

Advantages

- Decouple, Testability, Extensibility
- Provide a way to break down different component

2 major ways to implement dependency injecttion

1. Constructor injection
2. Setter injection

which ways to use depends on the situation

1. when the dependency is required, use constructor injection
2. when the dependency is optional, use setter injection

## What Problem to Solve

[Illustrate With Code](design-pattern-dependency-injection-code.md)

## Structure of Dependency Injection

- [Service Container/Injector](#Injector): Control part of IoC(inversion of control)
- [Service Interface(Abstract Service)](#service-interface)
- [Concrete Service](#concrete-service)
- [Consumer](#consumer): Where Dependencies is injected

## Injector

> may be a class or a method

1. Instantiate concrete service instance
2. **resolve** and **configure** service's dependencies)
3. inject concrete service instance into [consumer](#consumer)

> some framework can complete this work, like spring

## Service Interface

declare a method that

- implemented by [concrete service](#concrete-service) for actual task
- Used by [consumer](#consumer)

## Concrete Service

- Implement Method Performing the actual task
- Same task can be performed by different service, for example

Assume a requirement of data service

1. Data service may be provide by different database
2. And consumer just want the json data
3. So actual task is get data from database and convert it to json
4. those concrete services should implement convert their data to json

## Consumer

- Consist of Consumer class
  - declare a variable of type [service interface](#service-interface)
  - inject point for [injector](#injector) to inject the service, this is what talking about in [features](#features)
    - constructor
    - or method
  - method to call
- Use the service
- **does not** know which concrete service it will use

```ts
class Consumer {
  private service: ServiceInterface;

  constructor(service: ServiceInterface) {
    this.service = service;
  }

  public doSomething(): json {
    return this.service.doSomething();
  }
}
```


## Code

- ...
