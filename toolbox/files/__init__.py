"""The `files` package provides several utilities for handling files.

It contains:
- File manager for various types:
    - `FileManager(filename, ...)` - Manages read and write for generic files.
    - `CSVFile(filename, ...)` - Manages read and write for CSV files.
    - `JSONFile(filename, ...)` - Manages read and write for JSON files.
    - `PickleFile(filename, ...)` - Manages read and write for pickle files.
- Read and Write helpers:
    - `read_file(filename, ...)` - Reads all the content from a file at once.
    - `write_file(filename, data, ...)` - Writes content to a file at once.
    - `read_csv_file(filename, ...)` - Reads all the content from a CSV file at once.
    - `write_csv_file(filename, data, ...)` - Writes content to a CSV file at once.
    - `read_json_file(filename, ...)` - Reads all the content from a JSON file at once.
    - `write_json_file(filename, data, ...)` - Writes content to a JSON file at once.
    - `read_pickle_file(filename, ...)` - Reads all the content from a pickle file at once.
    - `write_pickle_file(filename, data, ...)` - Writes content to a pickle file at once.
- File helpers:
    - `get_file_mode()` - Gets the file mode given the desired access type.
    - `create_file_path(filepath)` - Creates the path to the given filename.
    - `delete_path(filepath)` - Deletes the file or the folder at the given path.
- Path helpers:
    - `get_application_name(package)` - Gets the name of the application.
    - `get_application_path(package)` - Gets the path of the application.
    - `get_file_path(filename, package)` - Gets the path to a file inside the application.
    - `get_module_folder_path(module)` - Gets the path to a module's parent folder.
    - `get_module_path(module)` - Gets the path to a module.

Examples:
```python
from toolbox import files

# Get the path to a file below your application's root
filename = files.get_file_path('path/to/file', 'my_package')

# Create a text file
data = "Some content"
with files.FileManager(filename, create=True) as file:
    file.write_file(data)

# Show the file
print(files.read_file(filename))

# Delete the file
if files.delete_path(filename):
    print('The file has been deleted!')
else:
    print('Cannot delete the file!')
```
"""
from toolbox.files.csv_file import (
    CSV_DIALECT,
    CSV_ENCODING,
    CSVFile,
    read_csv_file,
    write_csv_file,
)
from toolbox.files.file import get_file_mode, read_file, write_file
from toolbox.files.file_manager import FileManager
from toolbox.files.json_file import (
    JSON_ENCODING,
    JSON_INDENT,
    JSONFile,
    read_json_file,
    write_json_file,
)
from toolbox.files.path import (
    create_file_path,
    delete_path,
    get_application_name,
    get_application_path,
    get_file_path,
    get_module_folder_path,
    get_module_path,
)
from toolbox.files.pickle_file import PickleFile, read_pickle_file, write_pickle_file
