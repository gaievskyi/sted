# **STED**

Small text beautifier. Formats inline texts and ready txt-files. :snake:

**Usage**:

```Terminal
>>> python sted.py <text or path to txt-file> --spaces --capitals --stats --mistakes --path </some/path>

>>> python sted.py <text or path to txt-file> -sctm -p </some/path>
```

**Options**:

```Terminal
<path/text>: can be a path to your text-file OR directly typed text.

-s, --spaces: Format spaces in the text. Remove exta spaces.

-c, --capitals: Format capitals (new sentence, etc).

-m, --mistakes: Find mistakes and print info.

-t, --stats: Return statistics of a text (words, spaces, etc).


-p, path </some/path>: Path where formatted text will be written.
```

**Examples**:

```Terminal
>>> python sted.py text.txt -sctm -p new_text.txt

>>> python sted.py "hello,world!  " -sc
```
