"""
This file can also be imported as a module and contains the following
functions:
    * open_text - opens the file with a text if it exists, otherwise reads [text_in] as a text.
    * format_spaces - formats spaces in the text.
    * to_uppercase - capitalizes the letters where it's needed.
    * get_stats - returns the statistics of the text.
    * find_mistakes - finds mistakes in the text and returns info. (supports Polish)
    * text_out - writes formatted text to the path.
"""

import argparse
import sys


POSITIVE_ANSWERS = ("Yes", 'Y', "y", "yes")
NEGATIVE_ANSWERS = ("No", 'N', "n", "no")
in_path = ""


def args():
    """Arguments parser for console/terminal"""
    parser = argparse.ArgumentParser(
        description="Small Python text beautifier. Formats texts or text files.",
        usage=f"python {sys.argv[0]} path/text [-h] [-s] [-c] [-m] [-t] [-o path]"
    )
    # Input file or text [required]
    parser.add_argument("input", metavar="path/text", nargs=1,
                        help="Path to source file/Text itself")
    # Format spaces [optional]
    parser.add_argument("-s", "--spaces", required=False, action="store_const", const=True,
                        default=False, help="Formats spaces in the text. Removes exta spaces.")
    # Formats capitals [optional]
    parser.add_argument("-c", "--capitals", required=False, default=False, action="store_const",
                        const=True, help="Capitalizes the letters where it's needed (new sentence, etc).")
    # Find mistakes [optional]
    parser.add_argument("-m", "--mistakes", required=False, default=False,
                        action="store_const", const=True, help="Finds mistakes and prints info. Only Polish supported.")
    # Print statistics [optional]
    parser.add_argument("-t", "--stats", required=False, default=False, action="store_const",
                        const=True, help="Returns the statistics of the text.")
    # Write to file [optional]
    parser.add_argument("-p", "--path", required=False, metavar="path",
                        default=None, help="Path to output file('.txt', '.rtf', or '.doc')")

    args = parser.parse_args()
    _inpath = args.input[0]
    _spaces = args.spaces
    _capitals = args.capitals
    _mistakes = args.mistakes
    _stats = args.stats
    _path = args.path
    return _inpath, _spaces, _capitals, _mistakes, _stats, _path


def open_text(text_in: str) -> str:
    """Tries to open the file with a text, otherwise reads [text_in] as a text.

    Arguments:
        text_in (str) -- path to the file or inputed text.

    Returns:
        text (str) -- reads and returns text as a string
    """
    try:
        with open(text_in, "rt") as file:
            in_path = text_in
            text = file.read()
    except FileNotFoundError:
        answer = input("[*] File was not found. Read as a text? (Y/n): ")
        while True:
            if answer in POSITIVE_ANSWERS:
                text = text_in
                break
            elif answer in NEGATIVE_ANSWERS:
                text_in = input(
                    "[*] Please, enter a path to your file again: ")
                return open_text(text_in)
            else:
                answer = input("[*] Invalid answer. Please, try again (Y/n): ")
    return text


def format_spaces(text: str) -> str:
    """Formats spaces in the text. Removes exta spaces.

    Arguments:
        text (str) -- stores the original text

    Returns:
        text (str) -- returns formatted text
    """
    separators = ",./!?"

    for i in range(len(text)-1):
        # removing 2+ extra spaces in a row
        if text[i] == " " and text[i+1] == " ":
            text = text[:i] + text[i+1:]
            return format_spaces(text)
        # formating spaces before/after special symbols
        if text[i] in separators:
            # del before symbols
            if text[i-1] == " ":
                text = text[:i-1] + text[i:]
                return format_spaces(text)
            # add after symbols
            if text[i+1] != " ":
                text = text[:i+1] + " " + text[i+1:]
                return format_spaces(text)
    return text


def to_uppercase(text: str) -> str:
    """Capitalizes the letters where it's needed (new sentence, etc).

    Arguments:
        text (str) -- stores the original text

    Returns:
        text (str) -- returns formatted text
    """
    abbreviations = (
        'al.', 'cd.', 'cdn.', 'col.', 'cykl.', 'cyt.', 'cz.', 'dosł.',
        'godz.', 'iron.', 'itd.', 'itp.', 'jw.', 'jęz.', 'lic.', 'm.in.',
        'mies.', 'mkw.', 'muz.', 'n.e.', 'n.p.m.', 'nast.', 'np.', 'nw.',
        'o.o.', 'p.n.e.', 'p.o.', 'pl.', 'pn.', 'pt.', 'płd.', 'płn.',
        'rys.', 'sp.', 'str.', 'tab.', 'tj.', 'tzn.', 'tzw.', 'wsch.',
        'zach.', 'zob.', 'źr.', 'żeń.', 'approx.' 'appt.', 'A.S.A.P.',
        'B.Y.O.B.', 'dept.', 'D.I.Y.', 'est.', 'E.T.A.', 'min.', 'misc.',
        'R.S.V.P.', 'tel.', 'temp.', 'vet.', 'vs.', 'Ave.', 'Blvd.', 'Dr.',
        'St.', 'e.g.', 'etc.', 'i.e.', 'n.b.', 'P.S.', 'т. е.', 'и т. д.',
        'и т. п.', 'и др.', 'и пр.', 'см.', 'н. э.', 'обл.', 'гp.', 'стр.',
        'акад.', 'доц.', 'ж. д.', 'ж.-д.', 'им.', 'ин-т', 'шт.', 'тип.',
        'укр.', 'унив.', 'яз.', 'чл.', 'цифр.', 'цв.'
    )

    text = text.replace("\n", "\n ").split(" ")
    text[0] = text[0].capitalize()

    for el in range(len(text)-1):
        if text[el].endswith((".", ".\n", "!", "!\n", "?", "?\n")):
            if text[el] not in abbreviations:
                text[el+1] = text[el+1].capitalize()

    text = " ".join(text)
    text = text.replace("\n ", "\n")
    return text


def get_stats(text: str) -> str:
    """Returns the statistics of the text. Contains:
       quantity of spaces, lines, symbols, words.

    Arguments:
        text (str) -- stores the original text

    Returns:
        (str) -- returns the statistics
    """
    separators = "\"\\!?.,{};:'\n()[-–|'<>«»~%“”„”_=*¯#+/]\f\t\r\v"

    spaces = len([ch for ch in text if ch == " "])
    lines = 1 + text.count("\n") if len(text) != 0 else 0
    symbols = len(text) - spaces
    for _ in separators:
        text = text.replace(_, "")
    words = len(text.replace("\n", " ").strip().split(
        " ")) if len(text) != 0 else 0
    return f"Spaces: [{spaces}] Lines: [{lines}] Symbols: [{symbols}] Words: [{words}]"


def find_mistakes(text: str) -> str:
    """Finds mistakes in the text and returns info.

    Arguments:
        text (str) -- stores the original text

    Returns:
        info (str) -- returns the info about mistakes
    """
    separators = "\"\\!?.,{};:'\n()[-–|'<>«»~%“”„”_=*¯#+/]\f\t\r\v"

    # Cleaning up the text
    for el in separators:
        text = text.replace(el, " ")

    # Converting to the list & lowercase
    text = text.lower().split()

    # Creating the Polish dict
    with open("dict.txt", "rt") as file:
        dictionary = file.read()
    dictionary = dictionary.split(" ")

    # Searching mistakes
    mistakes = [x for x in text if x not in dictionary]

    # Returning result
    info = ""
    if len(mistakes) == 0:
        info += "Mistakes were not found."
    else:
        info += f"This words aren't in Polish dictionary. Check them for mistakes: {mistakes}"
    return info


def text_out(out_path: str, text: str) -> None:
    """Writes formatted text to the path.

    Arguments:
        path (str) -- stores a path where will be formatted file
        text (str) -- stores a formatted text

    Raises:
        EnvironmentError -- occured by wrong extensions of writting file.

    Returns:
        message (str) -- succesful writting message
    """
    message = f"\n[=========] 100% Text has been succesfully written to '{out_path}'\n"
    if out_path.endswith((".txt", ".rtf", ".docx")):
        if out_path != in_path:
            with open(out_path, "wt") as file:
                file.write(text)
                return message
        else:
            answer = input(
                "[*] Are you sure you want to rewrite the file? (Y/n): ")
            if answer in POSITIVE_ANSWERS:
                with open(out_path, "wt") as file:
                    file.write(text)
                return message
            elif answer in NEGATIVE_ANSWERS:
                out_path = input(
                    "[*] Please, enter a path to your file again: ")
                return text_out(out_path, text)
            else:
                answer = input("[*] Invalid answer. Please, try again.")
    else:
        raise EnvironmentError("File's extension must be .txt, .rtf or .docx")
    return
