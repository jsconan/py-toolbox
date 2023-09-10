<!-- markdownlint-disable -->

<a href="../toolbox/files/csv_file.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `toolbox.files.csv_file`
A simple API for reading and writing CSV files. 

**Global Variables**
---------------
- **CSV_ENCODING**
- **CSV_DIALECT**
- **CSV_SAMPLE_SIZE**
- **CSV_READER_PARAMS**
- **CSV_WRITER_PARAMS**
- **FILE_OPEN_PARAMS**

---

<a href="../toolbox/files/csv_file.py#L323"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_csv_file`

```python
read_csv_file(
    filename: 'str',
    encoding: 'str' = 'utf-8',
    dialect: 'str' = 'unix',
    **kwargs
) → list[dict | list]
```

Reads a CSV content from a file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to read. 
 - <b>`encoding`</b> (str, optional):  The file encoding. Defaults to CSV_ENCODING. 
 - <b>`dialect`</b> (str, optional):  The CSV dialect to use. If 'auto' is given, the reader will try detecting the CSV dialect by reading a sample at the head of the file. Defaults to CSV_DIALECT. 
 - <b>`delimiter`</b> (str, optional):  A one-character string used to separate fields. Defaults to ','. 
 - <b>`doublequote`</b> (bool, optional):  Controls how instances of quotechar appearing inside a field should themselves be quoted. When True, the character is doubled. When False, the escapechar is used as a prefix to the quotechar. Defaults to True. 
 - <b>`escapechar`</b> (str, optional):   A one-character string used to removes any special meaning from the following character. Defaults to None, which disables escaping. 
 - <b>`quotechar`</b> (str, optional):  A one-character string used to quote fields containing special characters, such as the delimiter or quotechar, or which contain new-line characters. Defaults to '"'. 
 - <b>`quoting`</b> (bool, optional):  Controls when quotes should be be recognized by the reader. It can take on any of the QUOTE_* constants. Defaults to QUOTE_MINIMAL. 
 - <b>`skipinitialspace`</b> (bool, optional):  When True, spaces immediately following the delimiter are ignored. The default is False. 
 - <b>`strict`</b> (bool, optional):   When True, raise exception Error on bad CSV input. Defaults to False. 
 - <b>`fieldnames`</b> (sequence, optional):  The name of each column in the CSV. If fieldnames is omitted, the values in the first row of the file will be used as the fieldnames. Regardless of how the fieldnames are determined, the dictionary preserves their original ordering. If a row has more fields than fieldnames, the remaining data is put in a list and stored with the fieldname specified by restkey (which defaults to None). If a non-blank row has fewer fields than fieldnames, the missing values are filled-in with the value of restval (which defaults to None). 

For reading headless CSV, set fieldnames to False. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`list[dict | list]`</b>:  The data read from the CSV file. 


---

<a href="../toolbox/files/csv_file.py#L378"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_csv_file`

```python
write_csv_file(
    filename: 'str',
    data: 'Iterable[dict | list]',
    encoding: 'str' = 'utf-8',
    dialect: 'str' = 'unix',
    **kwargs
) → int
```

Writes a CSV content to a file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to write. 
 - <b>`data`</b> (Iterable[dict | list]):  The content to write to the file. 
 - <b>`encoding`</b> (str, optional):  The file encoding. Defaults to CSV_ENCODING. 
 - <b>`dialect`</b> (str, optional):  The CSV dialect to use. Defaults to CSV_DIALECT. 
 - <b>`delimiter`</b> (str, optional):  A one-character string used to separate fields. Defaults to ','. 
 - <b>`doublequote`</b> (bool, optional):  Controls how instances of quotechar appearing inside a field should themselves be quoted. When True, the character is doubled. When False, the escapechar is used as a prefix to the quotechar. Defaults to True. 
 - <b>`escapechar`</b> (str, optional):   A one-character string used by the writer to escape the delimiter if quoting is set to QUOTE_NONE and the quotechar if doublequote is False. Defaults to None, which disables escaping. 
 - <b>`lineterminator`</b> (str, optional):  The string used to terminate lines produced by the writer. Defaults to "\r\n". 
 - <b>`quotechar`</b> (str, optional):  A one-character string used to quote fields containing special characters, such as the delimiter or quotechar, or which contain new-line characters. Defaults to '"'. 
 - <b>`quoting`</b> (bool, optional):  Controls when quotes should be be generated by the writer. It can take on any of the QUOTE_* constants. Defaults to QUOTE_MINIMAL. 
 - <b>`skipinitialspace`</b> (bool, optional):  When True, spaces immediately following the delimiter are ignored. The default is False. 
 - <b>`strict`</b> (bool, optional):   When True, raise exception Error on bad CSV input. Defaults to False. 
 - <b>`fieldnames`</b> (sequence, optional):  The name of each column in the CSV. If fieldnames is omitted and the first row is a dictionary, its keys will be used as fieldnames. Every subsequent row will need to be dictionaries as well. If the first row is a sequence, no header will be added, and all subsequent row will need to be sequences as well. 

The fieldnames sequence identify the order in which values from the rows are written to the file. The optional restval parameter specifies the value to be written if the dictionary is missing a key in fieldnames. If the current row contains a key not found in fieldnames, the optional extrasaction parameter indicates what action to take. If it is set to 'raise', the default value, a ValueError is raised. If it is set to 'ignore', extra values in the row are ignored. Any other optional or keyword arguments are passed to the underlying writer instance. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written to the file. 


---

<a href="../toolbox/files/csv_file.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CSVFile`
Offers a simple API for reading and writing CSV files. 

The class binds a filename with a set of properties so that it can be opened in a consistent way. 

The read API does not allow to size the data to read. However, it reads the file row by row. 



**Attributes:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`binary`</b> (bool):  The type of file, say text. It must always be False. 
 - <b>`encoding`</b> (str, optional):  The file encoding. 
 - <b>`dialect`</b> (str, optional):  The CSV dialect to use. If 'auto' is given, the reader will try detecting the CSV dialect by reading a sample at the head of the file. 



**Examples:**
 ```
file = CSVFile("path/to/the/file", dialect='excel', encoding="UTF-8")

# write rows to the file
file.write_file(csv)

# read the first row of the CSV
with file:
    first = file.read()

# gets the CSV in a list
csv = [row for row in file]

# write data to the file
with file(create=True):
    for row in csv:
         file.write(row)

# load the whole file, handling internally its opening
csv = file.read_file()
``` 

<a href="../toolbox/files/csv_file.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    filename: 'str',
    create: 'bool' = False,
    append: 'bool' = False,
    read: 'bool' = False,
    write: 'bool' = False,
    encoding: 'str' = 'utf-8',
    dialect: 'str' = 'unix',
    **kwargs
)
```

Creates a file manager for CSV files. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file to manage. 
 - <b>`create`</b> (bool, optional):  Expect to create the file. If it exists, it will be replaced. Defaults to False. 
 - <b>`append`</b> (bool, optional):  Expect to extend the file. Data will be added at the end. Defaults to False. 
 - <b>`read`</b> (bool, optional):  Expect to also read the file. Defaults to False. 
 - <b>`write`</b> (bool, optional):  Expect to also write to the file. Defaults to False. 
 - <b>`encoding`</b> (str, optional):  The file encoding. Defaults to CSV_ENCODING. 
 - <b>`dialect`</b> (str, optional):  The CSV dialect to use. If 'auto' is given, the reader will try detecting the CSV dialect by reading a sample at the head of the file. Defaults to CSV_DIALECT. 
 - <b>`delimiter`</b> (str, optional):  A one-character string used to separate fields. Defaults to ",". 
 - <b>`doublequote`</b> (bool, optional):  Controls how instances of quotechar appearing inside a field should themselves be quoted. When True, the character is doubled. When False, the escapechar is used as a prefix to the quotechar. Defaults to True. 
 - <b>`escapechar`</b> (str, optional):   A one-character string used by the writer to escape the delimiter if quoting is set to QUOTE_NONE and the quotechar if doublequote is False. On reading, the escapechar removes any special meaning from the following character. Defaults to None, which disables escaping. 
 - <b>`lineterminator`</b> (str, optional):  The string used to terminate lines produced by the writer. Defaults to "\r\n". 
 - <b>`quotechar`</b> (str, optional):  A one-character string used to quote fields containing special characters, such as the delimiter or quotechar, or which contain new-line characters. Defaults to '"'. 
 - <b>`quoting`</b> (bool, optional):  Controls when quotes should be be generated by the writer, or recognized by the reader. It can take on any of the QUOTE_* constants. Defaults to QUOTE_MINIMAL. 
 - <b>`skipinitialspace`</b> (bool, optional):  When True, spaces immediately following the delimiter are ignored. The default is False. 
 - <b>`strict`</b> (bool, optional):   When True, raise exception Error on bad CSV input. Defaults to False. 
 - <b>`fieldnames`</b> (sequence, optional):  The name of each column in the CSV. Depending on the access mode, the manner how fieldnames is consumed differs. 

When reading, if fieldnames is omitted, the values in the first row of the file will be used as the fieldnames. Regardless of how the fieldnames are determined, the dictionary preserves their original ordering. 

If a row has more fields than fieldnames, the remaining data is put in a list and stored with the fieldname specified by restkey (which defaults to None). If a non-blank row has fewer fields than fieldnames, the missing values are filled-in with the value of restval (which defaults to None). 

For reading headless CSV, set fieldnames to False. 

When writing, if fieldnames is omitted and the first row is a dictionary, its keys will be used as fieldnames. Every subsequent row will need to be dictionaries as well. If the first row is a sequence, no header will be added, and all subsequent row will need to be sequences as well. 

The fieldnames sequence identify the order in which values from the rows are written to the file. The optional restval parameter specifies the value to be written if the dictionary is missing a key in fieldnames. If the current row contains a key not found in fieldnames, the optional extrasaction parameter indicates what action to take. If it is set to 'raise', the default value, a ValueError is raised. If it is set to 'ignore', extra values in the row are ignored. Any other optional or keyword arguments are passed to the underlying writer instance. 




---

<a href="../toolbox/files/csv_file.py#L187"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `close`

```python
close() → CSVFile
```

Closes the file. 

Note: it does nothing if the file is already closed. 



**Returns:**
 
 - <b>`CSVFile`</b>:  Chains the instance. 

---

<a href="../toolbox/files/csv_file.py#L237"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read`

```python
read() → dict | list
```

Reads the next content from the file. 

Note: the file must be opened upfront. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the file is not opened. 
 - <b>`OSError`</b>:  If the file cannot be read. 



**Returns:**
 
 - <b>`dict | list`</b>:  The content loaded from the file, or None if the file is at EOF. 

---

<a href="../toolbox/files/csv_file.py#L202"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `read_file`

```python
read_file() → list[dict | list]
```

Reads all the content from the file. 

Note: If the file was already opened, it is first closed, then opened in read mode. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be read. 
 - <b>`FileNotFoundError`</b>:  If the file does not exist. 



**Returns:**
 
 - <b>`list[dict | list]`</b>:  The content read from the file. 

---

<a href="../toolbox/files/csv_file.py#L273"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write`

```python
write(data: 'dict | list') → int
```

Writes content to the file. 

Note: the file must be opened upfront. 



**Args:**
 
 - <b>`data`</b> (dict | list):  The content to write to the file. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the file is not opened. 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written. 

---

<a href="../toolbox/files/csv_file.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `write_file`

```python
write_file(data: 'Iterable[dict | list]') → int
```

Writes whole content to the file. 

Note: If the file was already opened, it is first closed, then opened in write mode. 



**Args:**
 
 - <b>`data`</b> (Iterable[dict | list]):  The content to write to the file. 



**Raises:**
 
 - <b>`OSError`</b>:  If the file cannot be written. 



**Returns:**
 
 - <b>`int`</b>:  The number of bytes written. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._