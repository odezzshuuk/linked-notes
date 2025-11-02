# Enum Type

## Feature

- Contains a limited number of named values
- Defines a type with a finite set of instances
- You can add constructors, **methods**, and **properties** to an enum
- The constructor modifier can only be private

## Declare An Enum Type

```java
public enum Size
{
    SMALL("S"), MEDIUM("M"), LARGE("L"), EXTRA_LARGE("XL");
    private String abbreviation;
    private Size(String abbreviation) {this.abbreviation = abbreviation;}
    public String getAbbreviation() {return abbreviation;}
}
```

- All enum types are subclasses of the Enum class
- toString()
  - For example, `Size.SMALL.toString()` returns the string `"SMALL"`
- valueOf()
  - For example, `Size s = Enum.valueOf(Size.class, "SMALL");` sets s to Size.SMALL
- values()

## Usage

```java
enum Size {SMALL, MEDIUM, LARGE, EXTRA;}
Size s = Size.MEDIUM;
```
