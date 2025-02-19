# CSharp - Delegate

* [What is Delegate](#what-is-delegate)
* [Declaring A Delegate](#declaring-a-delegate)
* [How To Use](#how-to-use)
* [Group Delegate](#group-delegate)
* [Delegate Return Value](#delegate-return-value)
* [Anonymous Delegate](#anonymous-delegate)
* [Predefined Delegate](#predefined-delegate)
* [Action](#action)
* [Func](#func)

## What is Delegate

> Delegate can be seen as a type-safe, object-oriented [function pointer](c++-function-pointer.md).

- A Delegate is a **type**
- Keyword `delegate` has the same usage level as `class` or `struct`
- A Delegate can be thought of as a type-safe, object-oriented function pointer.

## Declaring A Delegate

```cs
delegate void FooFunc(int x);
```

## How To Use

```c
public class Point 
{
    public int X { get; set; }
    public int Y { get; set; }
    public void MoveOnX(int x)
    {
        X += x;
    }

    public void MoveOnY(int y)
    {
        Y += y;
    }
}
Point p = new Point();
FooFunc func = new FooFunc(p.MoveOnX);  // "func" is a delegate instance
func(5);
```

- `p.MoveOnX` is a instance method
- Instance method can be called by delegate instance `func`

## Group Delegate

```c
FooFunc fa = pointA.MoveOnX;
FooFunc fb = pointB.MoveOnY;

fa += fb;  // Add Method
FooFunc fc = fa + fb; // Group Delegate
fc -= fa;  // Remove Method
```

- The order added is the order invoked.

## Delegate Return Value

- Return the value of last method

## Anonymous Delegate

- Lambda Expression
- Or `delegate(float f) { return f * 2;}`

```c
delegate int IntFunc(int InParam);  // Declare delegate type

IntFunc itfun = delegate(int x) {return x};  // Anonymous Delegate 1
itfun += (int x) => { return x };  // Anonymous Delegate 2

del(5);
```

## Predefined Delegate

[`Action`](#Action): Returnless Predefined Delegate 

- `Action`, `Action<T>`, `Action<T1, T2, ...>`

[`Func`](#Func): Returned Predefined Delegate

- `Func<TResult>`, `Func<T, TResult>`, `Func<T1, T2, ..., TResult>`

## Action

`Action`

- No return value
- No parameter

`Action<T>`

- No return value
- A Delegate with a **single parameter** of type `T`
- `T` is the parameter type

## Func

`Func<TResult>`

- A Delegate with `TResult` **return type**
- No parameter

`Func<T, TResult>`

- A Delegate with `T` **parameter type**
- With One parameter of type `T`


