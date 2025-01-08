# Design Principles - Dependency Inversion Principle

## Which Problem To Solve?

Bad practice: outter dependent on inner

```cs
using innter;  // bad practice
public class Outter
{
    public Inner inner
    public void CallInner() { innter.Do() }
}
```

Better: inner dependent on outter

- `outter.cs`

```
public interface IDepency depency
public class Outter
{
    public IDepency depency
    public void CallDepency() { depency.Do() }
}
```

- `inner.cs`

```
inner.cs
using outter
public class Inner : IDepency
{
    public void Do() { }
}
```

## Thinking: Inversion with Interface Or Base Class

- Interface for flexibility
- Base Class for share code

