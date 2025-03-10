# CSharp - Observer Design Pattern

* [Essential Elements](#essential-elements)
* [Observable/Provider](#observable/provider)
* [Observer](#observer)
* [Subscribe() Method](#subscribe()-method)
* [IDisposable Object](#idisposable-object)
* [Data](#data)

## Essential Elements

1. [Provider/Subject/Event Publisher](#observable/provider)
2. [Observer/Listener/Subscriber](#observer)
3. [Subscribe() Method](#subscribe()-method)
4. [IDisposable Object](#idisposable-object)
5. [Data](#data)

## Observable/Provider

> Also Provider/Subject/Event Publisher

- [Subscribe()](#subscribe()-method) method to add observers
- Hold a container to store observers

Subscribe() Method

`IDisposable IObservable.Subscribe(IObserver<T> observer)`

Parameter

- `observer`: `IObserver<T>`, object to receive notifications

Return

- `IDisposable`, **A reference** to an interface that allows the **observer** to stop receiving notifications before the provider has finished sending them.
- Corresponding observer's unsubscribe operation can be performed by calling the `Dispose()` method on this returned object.

How to Implementate

1. Stores a reference to the observer in a collection object
2. Return a reference to an [IDisposable](csharp-idisposable.md) interface

## Observer

> Also Listener/Subscriber

- Must implement three methods **triggered by [provider](#provider)**
  - `IObserver<T>.OnNext()`: receive a new value
  - `IObserver<T>.OnError()`: receive an error notification
  - `IObserver<T>.OnCompleted()`: receive a completion notification
- receive a reference [IDisposible]() reference from the provider

## IDisposable Object

- An IDisposable implementation enable the [provider]() to remove observers when complete
- [Observers]() receive an IDisposable reference from the [Subcribe() method](#subscribe()-method)
- Observers can call the `IDisposable.Dispose()` on this reference to unsubscribe before provider has finished sending notifications

## Data

- Refering to the generic type parameter of `IObserveable<T>`
- Linq query can be used to filter, transform, or combine data before sending to observers

