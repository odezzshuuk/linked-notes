# WebDev - Data Object

## What It Is

- Object that carries data between processes 
- transform data between
  - layers of application
  - different applications

## DTO

- Data Transfer Object
- object that carries data between processes
- no business login

```java
interface PersonDTO {

    String getName();

    void setName(String name);
}
```

## DAO

- Data Access Object
- use to access data from database

```java
interface PersonDAO {

    PersonDTO findById(int id);

    void save(PersonDTO person);

    void delete(PersonDTO person);
}
```
