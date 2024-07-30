# Spring - Components

- [Introduction](#introduction)
- [Component created by Spring](#component-created-by-spring)

## Introduction

- Component default scope is singleton
- 配置类上添加`@ComponentScan`注解用于扫描组件所在的package, 多个package用逗号分隔

```java
@Configuration
@ComponentScan('org.example.packageof.component', 'org.example.packageof.othercomponent')
```

## Component created by Spring

- `@Component`注解的类用于创建自定义组件
  - `@Repository`注解的类用于创建持久层组件
  - `@Service`注解的类用于创建业务层组件
  - `@Controller`注解的类用于创建控制层组件
- 配置类`@Bean`注解的方法中将非自定义类创建为spring组件

`@Component`注解类用来标记Spring组件

```java
@Component
public class Component {
    // ...
}
```

`@Bean`注解在方法上, 表示该方法返回的对象会注册为Spring应用上下文中的bean

```java
@Configuration
public class BeanFactory {

    @Bean
    public LocalDateTime now() {
        return LocalDateTime.now();
    }

    @Bean
    public MyBean createBean() {
        return new MyBean();  // 可用于任何类
    }
}
```

## Component Scope

- Scope supported by Spring: singleton, prototype, request, session, global session

