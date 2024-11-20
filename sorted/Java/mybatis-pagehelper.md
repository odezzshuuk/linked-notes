# PageHelper

-  MyBatis

## Import

```xml
<dependency>
    <groupId>com.github.pagehelper</groupId>
    <artifactId>pagehelper-spring-boot-starter</artifactId>
    <version>1.2.13</version>
</dependency>
```

## Configuration xml

**mybatis-config.xml**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <plugins>
        <plugin interceptor="com.github.pagehelper.PageInterceptor"></plugin>
    </plugins>
</configuration>
```

## Usage

```java
public PageInfo<T> selectAll(int pageNum, int pageSize) {
    PageHelper.startPage(pageNum, pageSize);  // 1
    List<T> list = mapper.selectAll();        // 2
    return new PageInfo<>(list);              // 3
```

