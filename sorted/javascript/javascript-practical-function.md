# JavaScript Practical Function

* [debounce](#debounce)
* [throttle](#throttle)
* [partially applied function](#partially-applied-function)

## debounce

[simple implement debounce](javascript-debounce-function.md)

- group multiple sequential calls in a single one

## throttle

- limit the number of times a function can be called over time

[simple implement throttle](javascript-throttle-function.md)

```js
function throttle(fn, delay) {
  let last = 0,
    timer = null;

  return function() {
    let context = this;
    let args = arguments;
    let now = +new Date();

    if (now - last < delay) {
      if (timer) {
        cancelAnimationFrame(timer);
      }
      timer = requestAnimationFrame(function() {
        last = now;
        fn.apply(context, args);
      });
    } else {
      last = now;
      fn.apply(context, args);
    }
  };
}
```

## partially applied function

- an application of [closure](javascript-closure.md)
- useful when working with callback, for example create a new function to handle paritcular use case

what it looks like

```js
function add(a) {
  return function(b) {
    return a + b;
  }
}

const add5 = add(5);
console.log(add5(3));
```

real-world use case

- higher-order function

```ts
type NumberPredicate = (x: number) => boolean;
function filter(numbers: number[], predicate: NumberPredicate): number[] {
  return numbers.filter(predicate);
}
function isGreaterThan(threshold: number): boolean {
  return (n: number) => n > threshold;
}
const numbers = [1, 2, 3, 4, 5];
const filterednumbers = fileter(nbumbers, isGreaterThan(3));
```

- search with price range

```ts
function searchProductsbyPriceRange(
  minPrice: number,
  maxPrices: number
): (query: string) => Product[]
{
  const pricerangeFilter: (product: Product) => boolean = (product: Product) => {
    return product.price >= minPrice && product.price <= maxPrice;
  }
  return (query: string) => {
    const allProducts: Product[] = searchProducts(query);
    return allProducts.filter(priceRangeFilter);
  }

}
```






