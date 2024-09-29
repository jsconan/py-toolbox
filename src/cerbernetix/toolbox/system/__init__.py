"""The `system` package provides several utilities for low level management.

It contains:
- `concurrent_tasks(callback, tasks)`: Calls the given callback concurrently with the given tasks.
- `full_type(value)`: Returns with the fully qualified type of the given value.
- `import_property(ns)`: Imports a property from the given namespace.
- `import_and_call(ns)`: Imports a function from the given namespace and call it with parameters.

Examples:
```python
from cerbernetix.toolbox.system import full_type

print(full_type("foo")) # builtins.str
print(full_type(full_type)) # cerbernetix.toolbox.system.type.full_type
```

```python
from cerbernetix.toolbox.system import import_property

try:
    update = import_property("lib.utils.update")
    update("foo")
except ImportError as e:
    print(f"An error occurred while importing the update helper: {e}")
```

```python
from cerbernetix.toolbox.system import import_and_call

try:
    import_and_call("lib.utils.update", "foo")
except ImportError as e:
    print(f"An error occurred while importing the update helper: {e}")
except TypeError as e:
    print(f"Unable to call the update helper: {e}")
```

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

from cerbernetix.toolbox.system.module import import_and_call, import_property
from cerbernetix.toolbox.system.parallel import concurrent_tasks
from cerbernetix.toolbox.system.type import full_type
