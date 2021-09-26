
<p style="text-align:center;font-size:100px">Pycheck</p>

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Python-Version](https://img.shields.io/badge/python-3.9-blue) ![issues](https://img.shields.io/github/issues/Brijeshkrishna/pycheck)  ![License](https://img.shields.io/github/license/brijeshkrishna/pycheck) 

## A package that allows check python syntax with flake8 and mypy with color
  
#  Installation

```bash
$ python setup.py install mydog 
```


or
```bash
$ python -m pip install mydog
```

### Pycheck officially supports Python 2.7 & 3.6+.

## Cloning the repository

``
git clone https://github.com/Brijeshkrishna/mydog.git 
``  

## How to use:

```bash
$ pycheck incorrect_py.py
1 > .\pycheck\pycheck.py:204:29 E272  multiple spaces before keyword
2 > .\pycheck\pycheck.py:204:80 E501  line too long (91 > 79 characters)
3 > .\pycheck\pycheck.py:21 error  Item "None" of "Optional[Match[str]]" has no attribute "group"
Found 3 errors (checked 1 source files) 
```
```bash
$ pycheck correct_py.py
Success: no issues found (checked 1 source files) 
```
### Help
```bash
$ pycheck --help
Usage: pycheck [OPTIONS] FILENAME

Options:
  -o TEXT  output file
  --help   Show this message and exit.
```
### Save to a file
```bash
$ pycheck file.py -o output.txt
$ cat output.txt
1 > setup.py:33 error: Argument 1 to "fun" has incompatible type "int"; expected "str"
Found 1 errors (checked 1 source file)
```
## License

Pycheck is licensed and distributed under the MIT license.  [Contact me](mailto:brijeshkrishnaga@gmail.com)  if you're looking for an exception to the terms. 

## Contributors 
####  If want to Contributor to pycheck contact me .

