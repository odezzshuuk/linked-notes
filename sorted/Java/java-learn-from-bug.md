# bug

## No.1

Can load library: libawt_xawt.so

## NO.2 

- Exception in thread "AWT-EventQueue-0" java.awt.HeadlessException

## No.3 

- LinkageError when loading main class...

`java.lang.UnsupportedClassVersionError: Preview features are not enabled for sample/Sample (class file version 62.65535). Try running with '--enable-preview'`

Possible causes

- JDK version used for compilation doesn't match JDK version used for runtime

## No.4

 `module java.base does not "opens java.util" to unnamed module @5305068a`

- Don't use reflection to escalate access permissions
- When you must use reflection, ensure the <font color="red">direct caller (method)</font> is isolated from malicious code
  - By declaring the caller as private or final

## No.5

`The import javax.servlet cannot be resolved`

- To use servlet, you need to download tomcat first

Solution 1:

- Use javac -cp to specify servlet-api.jar class file search path, link source files to complete compilation

```shell
javac -cp /usr/share/tomcat/lib/servlet-api.jar sample.java
```

## No.6

Reason for only reading one line

- BufferedReader has a buffer array, the readLine() method will

```java
public class Sample {
    public static void main(String[] args) {
        FileInputStream fin = new FileInputStream("demo.txt");
        InputStreamReader byteToChar = new InputStreamReader(fin);
        BufferedReader br = new BufferedReader(byteToChar);

        while (fin.read() != -1) {
            System.out.println(br.readLine());
        }
    }
}
```

## No.7

IllegalArgumentException thrown when calling varargs method via reflection

Bug occurrence conditions:

1. Object method parameter is varargs
2. When using [Method object](java-reflect-accessibleobject.md)'s invoke() method to call object method, when passing array arguments to the method, the array is of a specific type

```java
public class Application {
    public static void main(String[] args) throws IllegalAccessExceptoin, IllegalArgumentException, InvocationTargetException {

        Class cls = Student.class;
        Student stu = new Student();
        Method m = cls.getMethod("fx", String[].class);  // Can correctly get Method object

        String[] strs = {"a", "b", "c"};
        m.invoke(stu, new Object[]{"a", "b", "c"});  // Throws IllegalArgumentException
        m.invoke(stu, new String[]{"a", "b", "c"});  // Will throw IllegalArgumentException
        m.invoke(stu, (Object)strs)  // Normal call
    }

}

class Student {
    public void fx(String... args) {
        for (String arg : args) {
            System.out.println(arg);
        }
    }
}
```

## No.8

java.net.SocketException: Software caused connection abort: socket write error

## No.9

异常信息

```
org.springframework.data.redis.serializer.SerializationException: Could not write JSON: Java 8 date/time type `java.time.LocalDateTime` not supported by default: add Module "com.fasterxml.jackson.datatype:jackson-datatype-jsr310" to enable handling (through reference chain: Object["startTime"]); nested exception is com.fasterxml.jackson.databind.exc.InvalidDefinitionException: Java 8 date/time type `java.time.LocalDateTime` not supported by default: add Module "com.fasterxml.jackson.datatype:jackson-datatype-jsr310" to enable handling (through reference chain: Object["startTime"])
```

发生在Redis序列化Java 8 LocalDateTime对象时

解决方案: 1. 注解LocalDateTime字段

```java
@JsonFormat(pattern = "yyyy-MM-dd HH:mm:ss")
@JsonSerialize(using = LocalDateTimeSerializer.class)
@JsonDeserialize(using = LocalDateTimeDeserializer.class)
```

## No.10

IDE代码检查bug report

`references to interface static methods are allowed only at source level 1.8 or above`

解决办法

pom.xml

```xml
<properties>
    <maven.compiler.source>1.8</maven.compiler.source>
    <maven.compiler.target>1.8</maven.compiler.target>
</properties>
```