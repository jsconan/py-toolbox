"""A collection of formatting utilities.

Examples:
```python
from cerbernetix.toolbox.data import formatters

print(formatters.format_heading("Hello, World!"))
# ---------------------------------------- Hello, World! ------------------------------------------

formatters.print_heading("Hello, World!")
# ---------------------------------------- Hello, World! ------------------------------------------

print(formatters.format_columns([1, 2, 3, 4, 5, 6], 2))
# 1 4
# 2 5
# 3 6

formatters.print_columns([1, 2, 3, 4, 5, 6], 2)
# 1 4
# 2 5
# 3 6
```
"""

from typing import Any, Iterable

from cerbernetix.toolbox.iterators import iter_cells


def format_heading(
    title: str,
    length: int = 100,
    decorator: str = "-",
    justify: int = 0,
    margin: int | list[int] = 1,
    simple: bool = True,
) -> str:
    """Formats a heading.

    Args:
        title (str): The title of the heading.
        length (int, optional): The length of the heading. Defaults to 100.
        decorator (str, optional): The character used to decorate the heading. Defaults to "-".
        justify (int, optional): The justification of the title. -1 for left, 0 for center,
            1 for right. Defaults to 0.
        margin (int, list[int], optional): The margin of the heading. If a list, the first element
            is the top margin, the second is the bottom margin. Defaults to 1.
        simple (bool, optional): If True, the heading will be simplified to one single line.
            Defaults to True.

    Returns:
        str: The formatted heading.

    Examples:
    ```python
    from cerbernetix.toolbox.data import formatters

    print(formatters.format_heading("Hello, World!"))
    # -------------------------------------- Hello, World! ----------------------------------------
    ```
    """
    title_len = len(title)
    if length is None:
        length = title_len
    if not decorator:
        decorator = "-"

    if isinstance(margin, int):
        margin = [margin, margin]
    if len(margin) == 1:
        margin *= 2
    margin_before = "\n" * margin[0]
    margin_after = "\n" * margin[1]

    if justify == -1 and length > title_len:
        title = f"{title} ".ljust(length, decorator if simple else " ")
    elif justify == 0 and length >= title_len + 2:
        title = f" {title} ".center(length, decorator if simple else " ")
    elif justify == 1 and length > title_len:
        title = f" {title}".rjust(length, decorator if simple else " ")

    if simple:
        return f"{margin_before}{title}\n{margin_after}"

    line = (decorator * (length // len(decorator) + 1))[:length]
    return f"{margin_before}{line}\n{title}\n{line}\n{margin_after}"


def print_heading(
    title: str,
    length: int = 100,
    decorator: str = "-",
    justify: int = 0,
    margin: int | list[int] = 1,
    simple: bool = True,
) -> None:
    """Prints a formatted heading.

    Args:
        title (str): The title of the heading.
        length (int, optional): The length of the heading. Defaults to 100.
        decorator (str, optional): The character used to decorate the heading. Defaults to "-".
        justify (int, optional): The justification of the title. -1 for left, 0 for center,
            1 for right. Defaults to 0.
        margin (int, list[int], optional): The margin of the heading. If a list, the first element
            is the top margin, the second is the bottom margin. Defaults to 1.
        simple (bool, optional): If True, the heading will be simplified to one single line.
            Defaults to True.

    Examples:
    ```python
    from cerbernetix.toolbox.data import formatters

    formatters.print_heading("Hello, World!")
    # -------------------------------------- Hello, World! ----------------------------------------
    ```
    """
    print(format_heading(title, length, decorator, justify, margin, simple), end="")


def format_columns(
    cells: Iterable[Any],
    length: int = 100,
    separator: str = " ",
    col_dir: bool = True,
) -> str:
    """Formats a list of cells into columns.

    Args:
        cells (Iterable[Any]): The list of cells to format.
        length (int, optional): The length of the table. If the length is not enough to fit all the
            cells, they will be wrapped to the next line. Defaults to 100.
        separator (str, optional): The separator between the columns. Defaults to " ".
        col_dir (bool, optional): The direction of the columns. If True, the cells will be taken in
            column order, otherwise in row order. Defaults to True.

    Returns:
        str: The formatted columns.

    Examples:
    ```python
    from cerbernetix.toolbox.data import formatters

    print(formatters.format_columns([1, 2, 3, 4, 5, 6], 2))
    # 1 4
    # 2 5
    # 3 6

    print(formatters.format_columns([1, 2, 3, 4, 5, 6], 2, col_dir=False))
    # 1 2
    # 3 4
    # 5 6
    ```
    """
    cells = [str(cell) for cell in cells]
    nb_cells = len(cells)

    separator_len = len(separator)
    col_len = max((len(cell) for cell in cells))
    nb_cols = (length + separator_len) // (col_len + separator_len)
    col_len = (length - separator_len * (nb_cols - 1)) // nb_cols

    output = ""
    last = "\n"
    for string in iter_cells(cells, nb_cols, nb_cells, col_dir):
        if string != "\n":
            string = string.ljust(col_len)
            if last != "\n":
                string = f"{separator}{string}"
        output += string
        last = string
    return output


def print_columns(
    cells: Iterable[Any],
    length: int = 100,
    separator: str = " ",
    col_dir: bool = True,
) -> None:
    """Prints a list of cells into columns.

    Args:
        cells (Iterable[Any]): The list of cells to format.
        length (int, optional): The length of the table. If the length is not enough to fit all the
            cells, they will be wrapped to the next line. Defaults to 100.
        separator (str, optional): The separator between the columns. Defaults to " ".
        col_dir (bool, optional): The direction of the columns. If True, the cells will be taken in
            column order, otherwise in row order. Defaults to True.

    Examples:
    ```python
    from cerbernetix.toolbox.data import formatters

    formatters.print_columns([1, 2, 3, 4, 5, 6], 2)
    # 1 4
    # 2 5
    # 3 6

    formatters.print_columns([1, 2, 3, 4, 5, 6], 2, col_dir=False)
    # 1 2
    # 3 4
    # 5 6
    ```
    """
    print(format_columns(cells, length, separator, col_dir), end="")
