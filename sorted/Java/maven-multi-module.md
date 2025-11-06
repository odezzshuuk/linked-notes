# Organizing Multi-Module Projects

## Creating Multi-Module Projects

1. Generate Parent POM

```bash
mvn archetype:generate -DgroupId=com.baeldung -DartifactId=parent-project
```

Open pom.xml and add the following content

```xml
<packaging>pom</packaging>
```

2. Generate sub-modules

```bash
cd parent-project
mvn archetype:generate -DgroupId=com.baeldung -DartifactId=core
mvn archetype:generate -DgroupId=com.baeldung -DartifactId=service
mvn archetype:generate -DgroupId=com.baeldung -DartifactId=webapp
```

3. Add the modules section to parent pom.xml

```xml
<modules>
    <module>core</module>
    <module>service</module>
    <module>webapp</module>
</modules>
```

4. Add the parent section to the sub-module's pom.xml

```xml
<parent>
    <artifactId>parent-project</artifactId>
    <groupId>com.example</groupId>
    <version>1.0-SNAPSHOT</version>
</parent>
```

## Build

```bash
mvn package
```

## Add Dependency Management to Parent Project

- Used to unify dependencies

pom.xml

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>5.3.16</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## The Role of `<relativepath>`

```
super
  │
  ├─module1
  │
  └─module2
```

super pom.xml

```xml
<groupId>com.baeldung.maven-parent-pom-resolution</groupId>
<artifactId>aggregator</artifactId>
<version>1.0.0-SNAPSHOT</version>
```

submodule pom.xml

```xml
<artifactId>module1</artifactId>
<parent>
    <groupId>com.baeldung.maven-parent-pom-resolution</groupId>
    <artifactId>aggregator</artifactId>
    <version>1.0.0-SNAPSHOT</version>
</parent>
```

Child pom.xml without <relativepath>

- No need to install super POM in repository
- Don't even need to declare module1 in super POM

***

```xml
<artifactId>module2</artifactId>
<parent>
    <groupId>com.baeldung.maven-parent-pom-resolution</groupId>
    <artifactId>module1</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <relativePath>../module1/pom.xml</relativePath>
</parent>
```

This sets module2's parent to module1

***

Skip directory search, search maven repository

```xml
<parent>
    <groupId>com.baeldung</groupId>
    <artifactId>external-project</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <relativePath/>
</parent>
```


