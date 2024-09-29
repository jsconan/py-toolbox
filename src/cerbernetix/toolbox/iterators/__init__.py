"""A collection of iterators.

It contains:
- `iter_cells(cells, nb_cols, nb_cells, col_dir)` - Iterator for returning elements from a list.
- `iter_deep(*iterables)` - Iterator that returns elements from each iterable including nested ones.

Examples:
```python
from cerbernetix.toolbox.iterators import iter_deep, iter_cells

for v in iter_deep(1, 2, [[3], [4, [5]]], 6):
    print(v)

for cell in iter_cells([1, 2, 3, 4, 5, 6], 2):
    print(f"{cell} ", end="")
# 1 4
# 2 5
# 3 6
```
"""

from cerbernetix.toolbox.iterators.iter_cells import iter_cells
from cerbernetix.toolbox.iterators.iter_deep import iter_deep
