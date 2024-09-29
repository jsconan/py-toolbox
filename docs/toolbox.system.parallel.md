<!-- markdownlint-disable -->

<a href="../src/cerbernetix/toolbox/system/parallel.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.system.parallel`
A set of helpers for working with concurrent programming. 



**Examples:**
 ```python
from cerbernetix.toolbox.system import concurrent_tasks

def add(a, b):
     return a + b

task_args = [
     {"a": 1, "b": 2},
     {"a": 3, "b": 4},
     {"a": 5, "b": 6},
]

for result in concurrent_tasks(add, task_args):
     print(result)
# Output: 3 7 11
``` 


---

<a href="../src/cerbernetix/toolbox/system/parallel.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `concurrent_tasks`

```python
concurrent_tasks(callback: Callable, tasks: list[dict | list]) → Iterator
```

Calls the given callback function concurrently with the given tasks. 



**Args:**
 
 - <b>`callback`</b> (Callable):  The callback function to call. 
 - <b>`tasks`</b> (list[dict | list]):  A list of parameters representing each task. The callback will be  called in parallel with each. 



**Returns:**
 
 - <b>`Iterator`</b>:  An iterator with the results of each task. 



**Examples:**
 ```python
from cerbernetix.toolbox.system import concurrent_tasks

def add(a, b):
    return a + b

task_args = [
    {"a": 1, "b": 2},
    {"a": 3, "b": 4},
    {"a": 5, "b": 6},
]

for result in concurrent_tasks(add, task_args):
    print(result)
# Output: 3 7 11
``` 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
