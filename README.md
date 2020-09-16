## STED

Small Python :snake: **text beautifier**. Formats inline texts and ready txt-files.
Removes extra spaces, finds mistakes, formats capitals, returns statistics etc.

### Usage:

```Terminal
~ % python3 sted.py <path or text> --spaces --capitals --stats --mistakes --path </path>

~ % python3 sted.py <path or text> -sctm -p </path>
```

### Options:

```Terminal
<path/text>: path to your text-file OR inline text.

-s, --spaces: Format spaces in the text. Remove exta spaces.

-c, --capitals: Format capitals.

-m, --mistakes: Find mistakes and print info.

-t, --stats: Return statistics of a text (words, spaces, etc).


-p, path </some/path>: Path where formatted text will be written.
```

### Examples:

```Terminal
~ % python3 sted.py text.txt -sctm -p new_text.txt

~ % python3 sted.py "hello,world!  " -sc
```

### Requirements:

- Python 3 or higher.
