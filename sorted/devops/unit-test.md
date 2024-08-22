# Unit Test

## What It Is

- usually test  a class or a function
- usually written by single developer

## Terms

[Terms](unit-test-terms.md)

## Best Practice

[Best Practice](unit-test-best-practice.md)

## Fake, Mock, Stub

[Fake, Mock, Stub](unit-test-fake-mock-stub.md)

## Code Coverage

[Code Coverage](unit-test-code-coverage.md)

## Best Principle

- Follow Arrange/Act/Assert Pattern
  - Arrange: setup the test, such as create object, preparing input data
  - Act: Execute the function or method
  - Assert: Verify the result

```py
def add(a, b):
    return a + b

def test_foo():
    # Arrange
    a = 1
    b = 2

    # Act
    result = add(a, b)

    # Assert
    assert result == 3
```

- use [test fixtures](#test-fixtures)
- test normal cases, condition edge cases, boundary cases(min, max, empty, etc)
- avoid logic in test, like if, switch, while, for

## test fixtures

- the preparation environment and cleanup operation for each test cases
- the purpose of test fixtures is to ensure that there is a well known and fixed environment in which tests are run so that results are repeatable
- like data setup, network connection, configuration

[test fixtures in pytest](python-pytest.md#define-test-fixtures)

[test fixtures in javascript]()

## They Are Unit Test

- python

```py
import pytest

def test_foo():
    assert 1 == 1
```

- java

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestJunit {
   @Test
   public void testAdd() {
      String str = "Junit is working fine";
      assertEquals("Junit is working fine",str);
   }
}
```

- javascript

