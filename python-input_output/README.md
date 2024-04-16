# Reading and Writing Files

open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: open(filename, mode, encoding=None)
```python
f = open('workfile', 'w', encoding="utf-8")
```

The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used.
- 'r' open for reading (default)
- 'w' open for writing, truncating the file first
- 'x' open for exclusive creation, failing if the file already exists
- 'a' open for writing, appending to the end of file if it exists
- 'b' binary mode
- 't text mode (default)
- '+' open for updating (reading and writing)