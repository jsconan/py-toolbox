"""A collection of formatting utilities.

Examples:
```python
from cerbernetix.toolbox.data import formatters

print(formatters.format_heading("Hello, World!"))

formatters.print_heading("Hello, World!")
```
"""


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
    ```
    """
    print(format_heading(title, length, decorator, justify, margin, simple), end="")
