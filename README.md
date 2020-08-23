# STED &middot; [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/beeklz/sted/blob/master/LICENSE)

A small terminal built-in text beautifier. Formats inline texts and text files.

## Installing

```shell
$ git clone https://github.com/beeklz/sted
```
## Requirements:

- Python 3 or higher.
## Usage:

```shell
$ python3 sted.py <path or text> --spaces --capitals --stats --mistakes --path </path>
```
or
```shell
$ python3 sted.py <path or text> -sctm -p </path>
```

## Parameters:
parameter    | alias | description
------------ | ----- | ------------------------------------------
`path/text`  |       | define a path to your file or enter text.
`--spaces`   |  `-s` | format spaces. Remove exta spaces.
`--capitals` |  `-c` | format capitals.
`--mistakes` |  `-m` | find mistakes and print info.
`--stats`    |  `-t` | return statistics (quantity of words, etc)
`--path`     | `-p`  | define a path to write formatted file.

## Tests

```shell
$ python3 sted.py text.txt -sctm -p new_text.txt
>>> |> Text has been succesfully written into /new_text.txt
```

```shell
$ python3 sted.py "hello,world!  " -sc
>>> |> Formatted text:
>>> Hello, world!
```
## Licensing

Licenced by MIT License.
