# Algorithm Function Instances

## equal

> Read-only elements, no changes, no reordering

```cpp
equal(roster1.cbegin(), roster1.cend(), roster2.cbegin())
```

- Compares whether two **sequences** hold the same values.
- Accepts three **iterators** as parameters.
  - The first two represent the range of the first sequence.
  - The third represents the first element of the second sequence.
- The second sequence cannot be shorter than the first sequence (all algorithm functions that accept only one iterator for the second sequence have the same requirement).

## fill

> Write-only elements, no reading, no reordering

- Writes data to a sequence.
- Accepts three parameters.
  - Two iterator parameters represent the range.
  - One value parameter assigns a value to the sequence elements.

## copy

- Accepts the same parameters as `equal`.
- Many algorithms have a `copy` version to preserve the original sequence.

## replace

- Replaces a specified value with a specific value.
- `replace(b, e, search_val, replace_val)`
- `replace_copy(b, e, new_lst_b, search_val, replace_val)`
  - `arg new_lst_b`: Stores the sequence after replacement.
  - `arg search_val`: The value to be replaced.
  - `arg replace_val`: The replacement value.

## unique

- Eliminates duplicate elements.
  - First sort, then eliminate adjacent duplicate elements.
- Accepts two iterator parameters as the sequence range.
- Returns an iterator to the element following the last unique element.
- Implements deduplication by overwriting duplicate elements, without changing the sequence size.
- To truly delete duplicate elements, you must use container operations, such as `erase`.

## sort

- `sort` uses the `<` operator by default.
- The overloaded version of `sort` accepts a third parameter to customize the sorting method.
