# Unit Test - Fake, Mock, Stub

## Fake

- Can be stub or mock

## Mock And Stub

- Mock: Assert against on it
- Stub: Dependency replacement; Maybe hard code

Misleading on mock

```c
var mockOrder = new MockOrder();
var purchase = new Purchase(mockOrder);

purchase.ValidateOrders();
Assert.True(purchase.CanBeShipped);
```

- Actually, `MockOrder` is not a mock, it is a stub

For preceding code, stub is better

- `FakeOrder` for more general purpose

```c
var stubOrder = new FakeOrder();
var purchase = new Purchase(stubOrder);

purchase.ValidateOrders();
Assert.True(purchase.CanBeShipped);
```

This is a mock

- check a property on the fake object
- so it is a mock

```c
var mockOrder = new FakeOrder();
var purchase = new Purchase(mockOrder);

purchase.ValidateOrders();
Assert.True(mockOrder.Validated);
```

## Use Mock<T>

`Mock<T>` wraps an interface and **focally** and **simply** simulate its method signatures and return values

Take A Look At Code `dateTimeProviderStub.Setup(dtp => dtp.DayOfWeek()).Returns(DayOfWeek.Monday);` which means:

- When `DayOfWeek` is called on `dateTimeProviderStub`, return `DayOfWeek.Monday`

```c
public interface IDateTimeProvider {
    DayOfWeek DayOfWeek();
}

public int GetDiscountedPrice(int price, IDateTimeProvider dateTimeProvider) {
    if (dateTimeProvider.DayOfWeek() == DayOfWeek.Tuesday) {
        return price / 2;
    } else {
        return price;
    }
}
public void GetDiscountedPrice_NotTuesday_ReturnsFullPrice() {
    var priceCalculator = new PriceCalculator();
    var dateTimeProviderStub = new Mock<IDateTimeProvider>();
    dateTimeProviderStub.Setup(dtp => dtp.DayOfWeek()).Returns(DayOfWeek.Monday);
    var actual = priceCalculator.GetDiscountedPrice(2, dateTimeProviderStub);
    Assert.Equals(2, actual);
}
```
