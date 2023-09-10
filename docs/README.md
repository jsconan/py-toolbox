<!-- markdownlint-disable -->

# API Overview

## Modules

- [`toolbox`](./toolbox.md#module-toolbox): `py-toolbox` is a collection of utilities offering solutions to a set of common problems.
- [`toolbox.files`](./toolbox.files.md#module-toolboxfiles): The `files` package provides several utilities for handling files.
- [`toolbox.files.csv_file`](./toolbox.files.csv_file.md#module-toolboxfilescsv_file): A simple API for reading and writing CSV files.
- [`toolbox.files.file`](./toolbox.files.file.md#module-toolboxfilesfile): A collection of utilities for accessing files.
- [`toolbox.files.file_manager`](./toolbox.files.file_manager.md#module-toolboxfilesfile_manager): A simple class for reading and writing files.
- [`toolbox.files.json_file`](./toolbox.files.json_file.md#module-toolboxfilesjson_file): A simple API for reading and writing JSON files.
- [`toolbox.files.path`](./toolbox.files.path.md#module-toolboxfilespath): A collection of utilities around file paths.
- [`toolbox.files.pickle_file`](./toolbox.files.pickle_file.md#module-toolboxfilespickle_file): A simple API for reading and writing pickle files.

## Classes

- [`csv_file.CSVFile`](./toolbox.files.csv_file.md#class-csvfile): Offers a simple API for reading and writing CSV files.
- [`file_manager.FileManager`](./toolbox.files.file_manager.md#class-filemanager): Offers a simple API for reading and writing files.
- [`json_file.JSONFile`](./toolbox.files.json_file.md#class-jsonfile): Offers a simple API for reading and writing JSON files.
- [`pickle_file.PickleFile`](./toolbox.files.pickle_file.md#class-picklefile): Offers a simple API for reading and writing pickle files.

## Functions

- [`csv_file.read_csv_file`](./toolbox.files.csv_file.md#function-read_csv_file): Reads a CSV content from a file.
- [`csv_file.write_csv_file`](./toolbox.files.csv_file.md#function-write_csv_file): Writes a CSV content to a file.
- [`file.get_file_mode`](./toolbox.files.file.md#function-get_file_mode): Gets the file access mode given the expectations.
- [`file.read_file`](./toolbox.files.file.md#function-read_file): Reads a content from a file.
- [`file.write_file`](./toolbox.files.file.md#function-write_file): Writes a content to a file.
- [`json_file.read_json_file`](./toolbox.files.json_file.md#function-read_json_file): Reads a JSON content from a file.
- [`json_file.write_json_file`](./toolbox.files.json_file.md#function-write_json_file): Writes a JSON content to a file.
- [`path.create_file_path`](./toolbox.files.path.md#function-create_file_path): Creates the parent path for a file.
- [`path.delete_path`](./toolbox.files.path.md#function-delete_path): Deletes the file or the folder at the given path.
- [`path.get_application_name`](./toolbox.files.path.md#function-get_application_name): Gets the name of the application, based on the root folder.
- [`path.get_application_path`](./toolbox.files.path.md#function-get_application_path): Gets the path to the application's root.
- [`path.get_file_path`](./toolbox.files.path.md#function-get_file_path): Gets a full path for a file inside the application.
- [`path.get_module_folder_path`](./toolbox.files.path.md#function-get_module_folder_path): Gets the path to the folder containing the given module.
- [`path.get_module_path`](./toolbox.files.path.md#function-get_module_path): Gets the path to the given module.
- [`pickle_file.read_pickle_file`](./toolbox.files.pickle_file.md#function-read_pickle_file): Loads a list of objects from a file.
- [`pickle_file.write_pickle_file`](./toolbox.files.pickle_file.md#function-write_pickle_file): Writes a list of objects to a file.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._