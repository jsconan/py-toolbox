"""A collection of data utilities.

It contains:
- Formatters:
    - `format_columns(cells, length, separator, col_dir)` - Formats a list of cells into columns.
    - `format_heading(title, length, decorator, justify, margin, simple)` - Formats a heading.
    - `print_columns(cells, length, separator, col_dir)` - Prints a list of cells into columns.
    - `print_heading(title, length, decorator, justify, margin, simple)` - Prints a heading.
- Value mappers:
    - `passthrough(value)` - A passthrough mapper. It returns the value as it is.
    - `boolean(value)` - Converts a value to a boolean value.
    - `decimal(separator, thousands)` - Creates a mapper for casting decimal values to floats.
    - `default(value, default_value)` - Returns the value if not None, or the default value.
- `ValueExtractor(entries, mapper)` - A tool for extracting values from a set of possible entries.

Examples:
```python
from cerbernetix.toolbox.data import formatters, mappers, ValueExtractor

# Passthrough a value
print(mappers.passthrough("foo")) # "foo"
print(mappers.passthrough(42)) # 42

# Gets a boolean value
print(mappers.boolean("True")) # True
print(mappers.boolean("On")) # True
print(mappers.boolean("1")) # True
print(mappers.boolean("False")) # False
print(mappers.boolean("Off")) # False
print(mappers.boolean("0")) # False

# Gets a float
mapper = mappers.decimal(",")
print(mapper("3,14")) # 3.14

mapper = mappers.decimal(",", ".")
print(mapper("3.753.323,184")) # 3753323.184

# Extracts a date from various possible entries
extractor = ValueExtractor(["date", "time", "day"])
data = [{"date": "2023-10-06"}, {"day": "2023-02-20"}, {"time": "2023-06-12"}]
print([extractor.extract(row) for row in data]) # ["2023-10-06", "2023-02-20", "2023-06-12"]

# Extracts a number from various possible entries, casting it to an integer
extractor = ValueExtractor(["value", "val", "number"], int)
data = [{"val": "42"}, {"value": 12, {"number": 100}]
print([extractor.extract(row) for row in data]) # [42, 12, 100]

# Build full names from multiple entries
extractor = ValueExtractor(["firstname", "lastname"], " ".join)
data = [
    {"firstname": "John", "lastname": "Smith"},
    {"firstname": "Jane", "lastname": "Doe"},
]
print([extractor.aggregate(row) for row in data]) # ["John Smith", "Jane Doe"]

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

from cerbernetix.toolbox.data.formatters import (
    format_columns,
    format_heading,
    print_columns,
    print_heading,
)
from cerbernetix.toolbox.data.mappers import ValueMapper, boolean, decimal, default, passthrough
from cerbernetix.toolbox.data.value_extractor import ValueExtractor
