"""A set of helpers for working with concurrent programming.

Examples:
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
"""

from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterator


def concurrent_tasks(callback: Callable, tasks: list[dict | list]) -> Iterator:
    """Calls the given callback function concurrently with the given tasks.

    Args:
        callback (Callable): The callback function to call.
        tasks (list[dict | list]): A list of parameters representing each task. The callback will be
            called in parallel with each.

    Returns:
        Iterator: An iterator with the results of each task.

    Examples:
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
    """

    def do_task(args):
        if isinstance(args, dict):
            return callback(**args)
        return callback(*args)

    with ThreadPoolExecutor() as executor:
        return executor.map(do_task, tasks)
