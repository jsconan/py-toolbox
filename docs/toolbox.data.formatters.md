<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/data/formatters.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.data.formatters`
A collection of formatting utilities. 



**Examples:**
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


---

<a href="../src/cerbernetix/toolbox/data/formatters.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `format_heading`

```python
format_heading(
    title: str,
    length: int = 100,
    decorator: str = '-',
    justify: int = 0,
    margin: int | list[int] = 1,
    border: int | list[int] = 0
) → str
```

Formats a heading. 



**Args:**
 
 - <b>`title`</b> (str):  The title of the heading. 
 - <b>`length`</b> (int, optional):  The length of the heading. Defaults to 100. 
 - <b>`decorator`</b> (str, optional):  The character used to decorate the heading. Defaults to "-". 
 - <b>`justify`</b> (int, optional):  The justification of the title. -1 for left, 0 for center,  1 for right. Defaults to 0. 
 - <b>`margin`</b> (int, list[int], optional):  The margin of the heading. If a list, the first element  is the top margin, the second is the bottom margin. Defaults to 1. 
 - <b>`border`</b> (int, list[int], optional):  The border of the heading. If a list, the first element  is the top border, the second is the bottom border. If no border is defined, the heading  will be simplified to one single line. Defaults to 0. 



**Returns:**
 
 - <b>`str`</b>:  The formatted heading. 



**Examples:**
 ```python
from cerbernetix.toolbox.data import formatters

print(formatters.format_heading("Hello, World!"))
# -------------------------------------- Hello, World! ----------------------------------------
``` 


---

<a href="../src/cerbernetix/toolbox/data/formatters.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `print_heading`

```python
print_heading(
    title: str,
    length: int = 100,
    decorator: str = '-',
    justify: int = 0,
    margin: int | list[int] = 1,
    border: int | list[int] = 0
) → None
```

Prints a formatted heading. 



**Args:**
 
 - <b>`title`</b> (str):  The title of the heading. 
 - <b>`length`</b> (int, optional):  The length of the heading. Defaults to 100. 
 - <b>`decorator`</b> (str, optional):  The character used to decorate the heading. Defaults to "-". 
 - <b>`justify`</b> (int, optional):  The justification of the title. -1 for left, 0 for center,  1 for right. Defaults to 0. 
 - <b>`margin`</b> (int, list[int], optional):  The margin of the heading. If a list, the first element  is the top margin, the second is the bottom margin. Defaults to 1. 
 - <b>`border`</b> (int, list[int], optional):  The border of the heading. If a list, the first element  is the top border, the second is the bottom border. If no border is defined, the heading  will be simplified to one single line. Defaults to 0. 



**Examples:**
 ```python
from cerbernetix.toolbox.data import formatters

formatters.print_heading("Hello, World!")
# -------------------------------------- Hello, World! ----------------------------------------
``` 


---

<a href="../src/cerbernetix/toolbox/data/formatters.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `format_columns`

```python
format_columns(
    cells: Iterable[Any],
    length: int = 100,
    separator: str = ' ',
    col_dir: bool = True
) → str
```

Formats a list of cells into columns. 



**Args:**
 
 - <b>`cells`</b> (Iterable[Any]):  The list of cells to format. 
 - <b>`length`</b> (int, optional):  The length of the table. If the length is not enough to fit all the  cells, they will be wrapped to the next line. Defaults to 100. 
 - <b>`separator`</b> (str, optional):  The separator between the columns. Defaults to " ". 
 - <b>`col_dir`</b> (bool, optional):  The direction of the columns. If True, the cells will be taken in  column order, otherwise in row order. Defaults to True. 



**Returns:**
 
 - <b>`str`</b>:  The formatted columns. 



**Examples:**
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


---

<a href="../src/cerbernetix/toolbox/data/formatters.py#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `print_columns`

```python
print_columns(
    cells: Iterable[Any],
    length: int = 100,
    separator: str = ' ',
    col_dir: bool = True
) → None
```

Prints a list of cells into columns. 



**Args:**
 
 - <b>`cells`</b> (Iterable[Any]):  The list of cells to format. 
 - <b>`length`</b> (int, optional):  The length of the table. If the length is not enough to fit all the  cells, they will be wrapped to the next line. Defaults to 100. 
 - <b>`separator`</b> (str, optional):  The separator between the columns. Defaults to " ". 
 - <b>`col_dir`</b> (bool, optional):  The direction of the columns. If True, the cells will be taken in  column order, otherwise in row order. Defaults to True. 



**Examples:**
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




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
