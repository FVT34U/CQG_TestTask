<h1>Тестовое задание для CQG</h1>
<h3>Выполнил:</h3>
Казаркин Тимофей (a.k.a FVT34U)
<hr>

<h3>Задание:</h3>
Get a list of pairs from a configuration file (sample configuration file is provided below), and replace value1 by value2 for all matches in a given text file (sample text file is provided below). All values in configuration file are unique; no need to take care of preventing change of already changed value. Names of both files are passed as command line arguments. Sort changed lines by the total number of symbols replaced, starting from the most changed line. Output resulting text to console.

<h4>Sample configuration file:</h4>

```
a=z
b=y
c=x
```

<h4>Sample text file:</h4>

```
jgrebk6hnae
cnhjrfyjvth3nxr
b#sjcf_ansvo!
djf#aemfaaofna%
```

<hr>

<h3>Структура:</h3>
CQG_TestTask /
<br>&emsp;app /
<br>&emsp;&emsp;utils /
<br>&emsp;&emsp;&emsp;__init__.py
<br>&emsp;&emsp;&emsp;file_loader.py
<br>&emsp;&emsp;__init__.py
<br>&emsp;&emsp;converter.py
<br>&emsp;&emsp;main.py
<br>&emsp;data /
<br>&emsp;&emsp;config.txt
<br>&emsp;&emsp;input.txt
<br>&emsp;tests /
<br>&emsp;&emsp;test_converter.py
<br>&emsp;README.md

<hr>

<h3>Запуск программы:</h3>

PS path/to/CQG_TestTask> ```python app/main.py ./data/config.txt ./data/input.txt```

<hr>

<h3>Запуск тестов:</h3>

PS path/to/CQG_TestTask> ```python -m unittest tests/test_converter.py```