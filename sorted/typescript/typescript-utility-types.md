# Typescript - Utility Types

* [Awaited](#awaited)
* [Partial](#partial)
* [Required](#required)
* [Readonly](#readonly)
* [Record](#record)
* [Pick<Type, Keys>](#pick<type,-keys>)
* [Omit](#omit)
* [Exclude](#exclude)
* [`Extract<Type, Union>`](#`extract<type,-union>`)
* [NonNullable](#nonnullable)
* [Parameters](#parameters)
* [ConstructorParameters](#constructorparameters)
* [ReturnType](#returntype)
* [InstanceType](#instancetype)
* [ThisParameterType](#thisparametertype)
* [OmitThisParameter](#omitthisparameter)
* [ThisType](#thistype)
* [Intrinsic String Manipulation Types](#intrinsic-string-manipulation-types)

## Awaited

## Partial

`Partial<Type>`

- construct a type with all properties of T set to optional

```ts
interface Todo {
  title: string;
  description: string;
}

type TodoPreview = Partial<Todo>;
// equivalent to
interface TodoPreview {
  title?: string;
  description?: string;
}
```

## Required

`Required<Type>`

- construct a type with all properties of T set to required

> contrast to [Partial](#partial)

## Readonly

`Readonly<Type>`

- construct a type with all properties of T set to readonly

```ts
interface Todo {
  title: string;
}

type ReadonlyTodo = Readonly<Todo>;
const todo: ReadonlyTodo = {
  title: "Delete inactive users"
};
todo.title = "Hello"  // Error: cannot reassign a readonly property
```

## Record

`Record<Keys, Type>`

- An clean alternative to mapped types
- construct an object type whose property keys are `Keys`, property value are `Type`
- used to map the properties of a type to another type

```ts
interface CatInfo {
  age: number;
  breed: string;
}
type CatName = "miffy" | "boris" | "mordred";

const cats: Record<CatName, CatInfo> = {
  miffy: { age: 10, breed: "Persian" },
  boris: { age: 5, breed: "Maine Coon" },
  mordered: { age: 16, breed: "British Shorthair"},
};
```

## Pick<Type, Keys>

- Build a type by picking the set of properties `Keys` from `Type`

```ts
interface Todo {
  title: string;
  description: string;
  completed: boolean;
}
type TodoPreview = Pick<Todo, "title" | "completed">;
// equilavent type is
type TodoPreviewEql = {
  title: string;
  description: string;
}
```

## Omit

`Omit<Type, Keys>`

- constructs a type by picking all properties from `Type` and then removing `Keys`

> contrasts to [`Pick<Type, Keys>`](#picktype-keys)

```ts
interface Todo {
  title: string;
  description: string;
  completed: boolean;
}
type TodoPreview = Omit<Todo, "description">;
```

## Exclude

`Exclude<unionType, ExcludeMembers>`

- constructs a type by excluding `Excludedmembers` from [`UnionType`](typescript-type.md#union-types)

```ts
type T0 = Exclude<"a" | "b" | "c", "a">
// T0 is "b" | "c"
```

## `Extract<Type, Union>`

`Extract<Type, Union>`

- constructs a type by extracting from `Type` all [union members](typescript-type.md#union-types) that are assingable to `Union`

```ts
type t0 = Extract<"a" | "b" | "c" |, "a" | "f">
// t0 is "a"
```

## NonNullable

`nonNullable<Type>`

- constructs a type by excluding `null` and undefined from `Type`

```ts
type T0 = NoonNullable<string | number | undefined>;
// T0 is string | number
```

## Parameters

`Parameters<Type>`

- constructs a [tuple type](typescript-object-types.md#tuple) from the types used in the **parameters** of a function type `Type`

```ts
type T0 = parameters<() => string>;
// T0 is []
type T1 = Parameters<(s: string) => void>;
// T1 is [s: string]

declare function f1(arg; {a: number, b: string}): void;
type T2 = Parameter<typeof f1>
// T2 is [arg: {a: number, b: string}]
```

## ConstructorParameters

`ConstructorParameters<Type>`

- Constructs a [tuple type](typescript-object-types.md#tuple) from the types used in the **parameters** of a **constructor function** type `Type`

```ts
class C {
  constructor(a: number, b: string) {}
}
type T0 = ConstructorParameters<typeof C>;
// T0 is [a: number, b: string]
```

## ReturnType

`ReturnType<Type>`

- constructs a type consisting of the return type of function `Type`

```ts
declare function f1(): {a: number, b: string};
type T0 = ReturnType<typeof f1>;
// T0 is {a: number, b: string}
```

## InstanceType

`InstanceType<Type>`

- Constructs a type consisting of the instance type of a constructor function in `Type`

```ts
class C {
  x = 0;
  y = 0;
}

type T0 = InstanceType<typeof C>;
type T1 = C;
```

- `T0` is equivalent to `T1


## ThisParameterType

`ThisParameterType<Type>`

- Extracts the type of the `this` parameter of a function type
- or `unknown` if the function type has no `this` parameter

```ts
function toHex(this: number) {
  return this.toString(16);
}
function numberToString(n: ThisParameterType<typeof toHex>) {
  return toHex.apply(n);
}
```

## OmitThisParameter

## ThisType

`ThisType<Type>`

- dose not return a solid transformed type
- instead, it as a marker for a **contextual** `this` type

## Intrinsic String Manipulation Types

- to help with string manipulation arround template string literals

4 string maniplation types:

- `Uppercase<StringType>`
- `Lowercase<StringType>`
- `Capitalize<StringType>`
- `Uncapitailize<StringType>`

