"""An iterator for returning elements from a list.

Examples:
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
"""

import math
from typing import Any, Iterable, Iterator


def iter_cells(
    cells: Iterable[Any],
    nb_cols: int,
    nb_cells: int | None = None,
    col_dir: bool = True,
) -> Iterator[Any]:
    """Iterates over a list of cells in a table-like manner.

    Args:
        cells (Iterable[Any]): The list of cells to iterate over.
        nb_cols (int): The number of columns in the table.
        nb_cells (int | None, optional): The number of cells to cover. If omitted, all cells from
            the list will be taken. Defaults to None.
        col_dir (bool, optional): The direction of the columns. If True, the cells will be taken in
            column order, otherwise in row order. Defaults to True.

    Yields:
        Iterator[Any]: An iterator that returns the cells in the table-like manner.
            When a row is completed, a newline character is yielded.

    Examples:
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
    """
    cells = list(cells)

    if nb_cells is None:
        nb_cells = len(cells)

    nb_ln = math.ceil(nb_cells / nb_cols)

    for i in range(nb_cols * nb_ln):
        if i and i % nb_cols == 0:
            yield "\n"

        if col_dir:
            i = (i % nb_cols) * nb_ln + (i // nb_cols)

        if i >= nb_cells:
            continue

        yield cells[i]

    yield "\n"
