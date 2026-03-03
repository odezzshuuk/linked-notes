# Maven - Subelement of "Dependency" Element 

## groupId, artifactId, version

## scope

`<scope>compile</scope>`: default scope

- Can be import by `import`

`<scope>provided</scope>`: runtime dependency

- web application deploy to container, container provide dependency and related lib

```xml
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>4.0.1</version>
    <scope>provided<scope>
</dependency>
```

`<scope>runtime</scope>`: runtime dependency, won't appear in compiled class file

- Does not need to be available during compile time

```xml
<dependency>
    <groupId>mysql<groudId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.28</version>
    <scope>runtime</scope>
</dependency>
```

`<scope>test</scope>`: 

`<scope>system</scope>`:

- like provided, but requires explicit path to the jar file

```xml
<dependency>
    <groupId>com.baeldung</groupId>
    <artifactId>custom-dependency</artifactId>
    <version>1.3.2</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/libs/custom-dependency-1.3.2.jar</systemPath>
</dependency>
```

import

- important dependency
- will replaced with all effective dependencies
