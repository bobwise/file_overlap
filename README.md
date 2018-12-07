# file_overlap

Python script that searches two files or directories of files for a given regular expression. It then outputs all matches found in the first path, the second path, or both paths.

# usage

>`python file_overlap.py /path/to/first/file/or/directory /path/to/second/file/or/directory regex out1.txt out2.txt both.txt .scss True`

- /path/to/first/file/or/directory: the first location to search. If this is a directory, the search will include all child directories and files.
- /path/to/second/file/or/directory: the second location to search. If this is a directory, the search will include all child directories and files.
- regex: The regular expression to search for
- out1.txt: after execution, this file will contain all matches to the regular expression that appear in the first path but not the second.
- out2.txt: after execution, this file will contain all matches to the regular expression that appear in the second path but not the first.
- both.txt: after execution, this file will contain all matches to the regular expression that appear in both paths.
- .scss: if provided, the program will only search in files that match this extension (case-insensitive).
- True: if True, the program will ignore all paths that include "node_modules".