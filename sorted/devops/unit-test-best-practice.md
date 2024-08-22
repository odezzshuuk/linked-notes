# Unit Test - Best Practice

* [Avoid Infrastructure dependencies](#avoid-infrastructure-dependencies)
* [Name The Test](#name-the-test)
* [Arrange/Act/Assert Pattern](#arrange/act/assert-pattern)
* [Write Minimally Passing Tests](#write-minimally-passing-tests)
* [Avoid Magic Strings](#avoid-magic-strings)
* [Avoid Logic In Tests](#avoid-logic-in-tests)
* [Prefer helper methods to setup and teardown](#prefer-helper-methods-to-setup-and-teardown)
* [Avoid Multiple Acts](#avoid-multiple-acts)
* [Stub Static References](#stub-static-references)
* [Validate Private Methods By Unit Testing Public Methods](#validate-private-methods-by-unit-testing-public-methods)

## Avoid Infrastructure dependencies

## Name The Test

1. name of the method under test
2. scenario being tested
3. expected behavior

- For example: `GetDiscountedPrice_OnTuesday_ReturnsHalfPrice`

## Arrange/Act/Assert Pattern

- Arrange: setup necessary to execute the test
- Act: execute the method under test
- Assert: verify the method under test produced the expected result

## Write Minimally Passing Tests

## Avoid Magic Strings

## Avoid Logic In Tests

## Prefer helper methods to setup and teardown

[setup](unit-test-terms.md#setup)

## Avoid Multiple Acts

## Stub Static References

- for example, `DateTime.Now`

```c
public int GetDiscountedPrice(int price) {
    if (DateTime.Now.DayOfWeek == DayOfWeek.Tuesday) {
        return price / 2;
    }
    else {
        return price;
    }
}
// test not Tuesday
public void GetDiscountedPrice_NotTuesday_ReturnsFullPrice() {
    var priceCalculator = new PriceCalculator();
    var actual = priceCalculator.GetDiscountedPrice(2);
    Assert.Equals(2, actual)
}
// test Tuesday
public void GetDiscountedPrice_OnTuesday_ReturnsHalfPrice() {
    var priceCalculator = new PriceCalculator();
    var actual = priceCalculator.GetDiscountedPrice(2);
    Assert.Equals(1, actual);
}
```

- wrap interface with `Mock<T>` class which focus on simulating method signatures and return values

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

public void GetDiscountedPrice_OnTuesday_ReturnsHalfPrice() {
    var priceCalculator = new PriceCalculator();
    var dateTimeProviderStub = new Mock<IDateTimeProvider>();
    dateTimeProviderStub.Setup(dtp => dtp.DayOfWeek()).Returns(DayOfWeek.Tuesday);
    var actual = priceCalculator.GetDiscountedPrice(2, dateTimeProviderStub);
    Assert.Equals(1, actual);
}
```

## Validate Private Methods By Unit Testing Public Methods

```c
public string ParseLogLine(string input)
{
    var sanitizedInput = TrimInput(input);
    return sanitizedInput;
}

private string TrimInput(string input)
{
    return input.Trim();
}
```

