# CSharp - Conversion

* [Explicit Conversion](#explicit-conversion)
* [Implicit Conversion](#implicit-conversion)
* [Overflow checking](#overflow-checking)
* [Operator as](#operator-as)
* [Operator is](#operator-is)
* [Boxing](#boxing)

## Explicit Conversion

- if a conversion may result in a loss of information, you must use an explicit conversion
- losing information will happenned, such as:
  - double to int
  - double to float
  - Base Type to Derived Type

```c#
short var1 = 5;
sbyte var2 = 10;

var = (sbyte)var1;
```

2 ways to explicit conversion

- Cast expression: `(T)E`
- [Operator `as`](#operator-as), 
- `as` vs `(T)E`: unlike cast expression, `as` operator will not throw an exception if the conversion is not possible

Cast expression may cause exception at runtime

```c
class Animal
{
    public void Eat() => System.Console.WriteLine("Eating.");
    public override string ToString() => "I am an animal."; 
}
class Reptile : Animal { }
class Mammal : Animal { }
class Program
{
    static void Main()
    {
        Test(new Mammal());
    }
    static void Test(Animal a)
    {
        // this line is ok to compile
        // but not ok at runtime, InvalidCastException thrown
        Reptile r = (Reptile)a;

    }
}
```

- if `a` is a `Reptile` definitely, this conversion is Ok both in runtime and compile time
- [`is`](#operator-is) operator enable to check whether a conversion is OK at runtime

## Implicit Conversion

- Inplicit conversion can be made when **source type** is a **subset** of the target type

```cs
int num = 2147483647;
long bigNum = num;
```

For [reference type](), implicit conversion is always exist from derived type to base type

```
Derived d = new Derived();
Base b = d;
```

## Overflow checking

- checked

```c#
int ten = 10;

checked(2137383647 + ten);
checked
{
    int i3 = 2137483647 + ten;
}
```

## Operator as

```c#
E as T
```

vs (T)E

- Unable to convert, return null
- Only consider reference, boxing, unboxing conversion
- Never throw an exception

## Operator is

- used to check whether an **object** is is of a **particular type** or inherits from a class or interface

## Boxing

[boxing](csharp-boxing.md)

