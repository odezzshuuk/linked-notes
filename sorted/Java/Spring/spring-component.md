# Spring - Components

- [Introduction](#introduction)
- [Component created by Spring](#component-created-by-spring)

## Introduction

- Component default scope is singleton
- Add the `@ComponentScan` annotation to the configuration class to scan the package where the component is located; multiple packages are separated by commas

```java
@Configuration
@ComponentScan('org.example.packageof.component', 'org.example.packageof.othercomponent')
```

## Component created by Spring

- Classes annotated with `@Component` are used to create custom components
  - Classes annotated with `@Repository` are used to create persistence layer components
  - Classes annotated with `@Service` are used to create service layer components
  - Classes annotated with `@Controller` are used to create controller layer components
- In the configuration class, methods annotated with `@Bean` create non-custom classes as Spring components

Classes annotated with `@Component` are used to mark Spring components

```java
@Component
public class Component {
    // ...
}
```

The `@Bean` annotation on a method means the returned object will be registered as a bean in the Spring application context

```java
@Configuration
public class BeanFactory {

    @Bean
    public LocalDateTime now() {
        return LocalDateTime.now();
    }

    @Bean
    public MyBean createBean() {
        return new MyBean();  // Can be used for any class
    }
}
```

## Component Scope

- Scope supported by Spring: singleton, prototype, request, session, global session

