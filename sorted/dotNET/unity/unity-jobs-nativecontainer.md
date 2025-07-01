# Unity Jobs - NativeContainer

## What's For

- A thread-safe for native memory
- Allow [job](unity-jobs) to access data shared with main thread **rather than working with a copy**

## Features

- Value type
- When assigned to a variable, unity create a copy, which contains pointers to original data

## How to Create

Must specify the memory allocation type.

3 memory allocation types:

- `Allocator.Temp`: one frame or fewer. 
  - Can't assign to job member
- `Allocator.TempJob`:
  - Must be `Dispose` within 4 frames
- `Allocator.Persistent`:

```cs
NativeArray<float> result = new nativeArray<float>(10, Allocator.TempJob);
```

If a job does not need to write to a NativeContainer, it can be marked as `ReadOnly`

```cs
[ReadOnly]
public NativeArray<int> myData;
```

To add Elements after instantiate, Use`NativeList<T>`

## How To Change Elements Value

which is not work

- Cause `NativeContainer` not implement [ref return](csharp-method#ref-return)

```cs
// Not work
nativeArray[0] = 10; 
```

That will work

```cs
// Work
flat temp = nativeArray[5];
temp = 10;
nativeArray[5] = temp; 
```

- `ExampleStruct` is a struct type

## Disposing NativeContainer

When To

- [ ]

How To

1. call `Dispose()` method to release the memory allocated for the NativeContainer

```cs
nativeArray.Dispose();
```

2. call `JobHandle Dispose(JobHandle inputDeps)`

- return a jobhandle of the job which
  - dispose the native container 
  - `inputDeps` is the [dependency](unity-jobs#job-dependency) of the job

