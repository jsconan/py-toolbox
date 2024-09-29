<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/iterators/iter_cells.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.iterators.iter_cells`
An iterator for returning elements from a list. 



**Examples:**
 ```python
from cerbernetix.toolbox.iterators import iter_cells

for cell in iter_cells([1, 2, 3, 4, 5, 6], 2):
     print(f"{cell} ", end="")
# 1 4
# 2 5
# 3 6

for cell in iter_cells([1, 2, 3, 4, 5, 6], 2, col_dir=False):
     print(f"{cell} ", end="")
# 1 2
# 3 4
# 5 6
``` 


---

<a href="../src/cerbernetix/toolbox/iterators/iter_cells.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `iter_cells`

```python
iter_cells(
    cells: Iterable[Any],
    nb_cols: int,
    nb_cells: int | None = None,
    col_dir: bool = True
) → Iterator[Any]
```

Iterates over a list of cells in a table-like manner. 



**Args:**
 
 - <b>`cells`</b> (Iterable[Any]):  The list of cells to iterate over. 
 - <b>`nb_cols`</b> (int):  The number of columns in the table. 
 - <b>`nb_cells`</b> (int | None, optional):  The number of cells to cover. If omitted, all cells from  the list will be taken. Defaults to None. 
 - <b>`col_dir`</b> (bool, optional):  The direction of the columns. If True, the cells will be taken in  column order, otherwise in row order. Defaults to True. 



**Yields:**
 
 - <b>`Iterator[Any]`</b>:  An iterator that returns the cells in the table-like manner.  When a row is completed, a newline character is yielded. 



**Examples:**
 ```python
from cerbernetix.toolbox.iterators import iter_cells

for cell in iter_cells([1, 2, 3, 4, 5, 6], 2):
    print(f"{cell} ", end="")
# 1 4
# 2 5
# 3 6

for cell in iter_cells([1, 2, 3, 4, 5, 6], 2, col_dir=False):
    print(f"{cell} ", end="")
# 1 2
# 3 4
# 5 6
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
