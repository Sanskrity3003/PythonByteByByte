- To sort a list there are two ways:
	1. ``list.sort()
	2.`` new_lst= sorted(lst)
- To sort the list in reverse:
	1. ``list.sort(reverse=True)
	2. ``new_lst= sorted(lst,reverse=True)

Now that we know about the methods, it is important to know which method is useful in which situation.

- usually we use ``new_lst = sorted(lst)``  because of the following reasons:
	1. even after sorting the new list, the original string stays intact.
	2. when working with tuples ``.sort()`` dosen't work here.

- When using dictionary:
```python
s_di=sorted(di)
```
the above sorts and returns the keys in ascending.
- To sort the dictionary by values:
```python
di = {'a': 3, 'b': 1, 'c': 2} sorted_by_values = sorted(di.items(), key=lambda item: item[1])
```


----
## Additional Points

- **Stability of Sorting**: Both `sorted()` and `list.sort()` are stable sorts.

- **Custom Sorting with `key` Parameter**:
    ```python
    # Example: Sort a list of tuples by the second element
    lst = [(1, 3), (2, 2), (3, 1)]
    sorted_lst = sorted(lst, key=lambda x: x[1])
    # Output: [(3, 1), (2, 2), (1, 3)]
    ```

- **Sorting Dictionaries by Values**:
    ```python
    di = {'a': 3, 'b': 1, 'c': 2}
    sorted_by_values = sorted(di.items(), key=lambda item: item[1])
    # Output: [('b', 1), ('c', 2), ('a', 3)]
    ```

- **Using `operator.itemgetter` for Sorting**:
    ```python
    from operator import itemgetter
    lst = [(1, 3), (2, 2), (3, 1)]
    sorted_lst = sorted(lst, key=itemgetter(1))
    # Output: [(3, 1), (2, 2), (1, 3)]
    ```

- **Sorting with Multiple Criteria**:
   ```python
    lst = [(1, 3, 'a'), (2, 2, 'b'), (3, 1, 'c')]
    sorted_lst = sorted(lst, key=lambda x: (x[1], x[2]))
    # Output: [(3, 1, 'c'), (2, 2, 'b'), (1, 3, 'a')]
    ```
    
