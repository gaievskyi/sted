from re import sub, findall
from common.constants import *


def read_text(unformatted_text: str) -> str:
    """Open text from the file or read it directly.

    Arguments:
        unformatted_text (str): path to a file OR inputed text

    Returns:
        str: reads and returns text as a text
    """
    try:
        with open(unformatted_text, "rt") as f:
            # creating global var needed at writing func.
            global in_path
            in_path = unformatted_text
            # reading data
            txt = f.read()

    except FileNotFoundError:
        answer = input(READ_AS_TEXT)
        while True:
            if answer in POSITIVE_ANSWERS:
                txt = unformatted_text
                break
            elif answer in NEGATIVE_ANSWERS:
                unformatted_text = input(ENTER_AGAIN)
                return read_text(unformatted_text)
            else:
                answer = input(INVALID_ANSWER_TRY_AGAIN)
    return txt


def remove_extra_spaces(txt: str) -> str:
    """Remove exta spaces.

    Args:
        txt (str): stores the original text

    Returns:
        str: returns formatted text
    """
    result = sub(r"  ", " ", txt)
    return remove_extra_spaces(result) if findall("  ", result) else result


def format_punctuation(txt: str) -> str:
    """Remove or add spaces around the punctuation signs.

    Args:
        txt (str): stores the original text

    Returns:
        str: returns formatted text
    """
    punctuation = (",", ".", "!", "?")

    for i in range(len(txt)-1):
        if txt[i] in punctuation:
            # del before symbols
            if txt[i-1] == " ":
                txt = txt[:i-1] + txt[i:]
                return format_punctuation(txt)
            # add after symbols
            if txt[i+1] != " " and txt[i+1] != "\n":
                txt = txt[:i+1] + " " + txt[i+1:]
                return format_punctuation(txt)
    return txt


def format_uppercase(txt: str) -> str:
    """Capitalize letters where it's needed (new sentence, etc).

    Arguments:
        txt (str): stores the original text

    Returns:
        str: returns formatted text
    """
    abbreviations = (
        'al.', 'cd.', 'cdn.', 'col.', 'cykl.', 'cyt.', 'cz.', 'dosł.',
        'godz.', 'iron.', 'itd.', 'itp.', 'jw.', 'jęz.', 'lic.', 'm.in.',
        'mies.', 'mkw.', 'muz.', 'n.e.', 'n.p.m.', 'nast.', 'np.', 'nw.',
        'o.o.', 'p.n.e.', 'p.o.', 'pl.', 'pn.', 'pt.', 'płd.', 'płn.',
        'rys.', 'sp.', 'str.', 'tab.', 'tj.', 'tzn.', 'tzw.', 'wsch.',
        'zach.', 'zob.', 'źr.', 'żeń.', 'approx.' 'appt.', 'A.S.A.P.'
    )
    punctuation = (".", "!", "?", ".\n", "!\n", "?\n")

    txt = txt.replace("\n", "\n ").split(" ")
    txt[0] = txt[0].capitalize()

    for el in range(len(txt)-1):
        if txt[el].endswith(punctuation):
            if txt[el] not in abbreviations:
                txt[el+1] = txt[el+1].capitalize()

    txt = " ".join(txt)
    txt = txt.replace("\n ", "\n")
    return txt


def get_stats(txt: str) -> str:
    """Return the statistics of the text.
    Contains quantity of spaces, lines, symbols, words.

    Arguments:
        txt (str): stores the original text

    Returns:
        str: returns statistics
    """
    separators = "\"\\!?.,{};:'\n()[-|'<>«»~%“”„”_=*¯#+/]\f\t\r\v"

    spaces = txt.count(" ")
    lines = len(txt.splitlines())
    for _ in separators:
        txt = txt.replace(_, "")
    symbols = len(txt) - spaces
    words = len(txt.strip().split(" "))

    return (f"\n{'-'*(9+len(str(max(spaces, lines, symbols, words))))}\n"  # print line '----'
            f"Spaces:  {spaces}\n"
            f"Lines:   {lines}\n"
            f"Symbols: {symbols}\n"
            f"Words:   {words}"
            f"\n{'-'*(9+len(str(max(spaces, lines, symbols, words))))}")   # print line '----'


def find_mistakes(txt: str) -> str:
    """Find mistakes and return them.

    Arguments:
        txt (str): stores the original text

    Returns:
        str: mistakes log
    """
    separators = "\"\\!?.,{};:'\n()[-–|'<>«»~%“”„”_=*¯#+/]\f\t\r\v"

    # Clean up the txt
    for el in separators:
        txt = txt.replace(el, " ")

    # Convert to the list & lowercase
    txt = txt.lower().split()

    # Create the Polish dict
    with open("common/dict.txt", "rt") as f:
        dictionary = f.read()
    dictionary = dictionary.split(" ")

    # Search mistakes
    mistakes = [x for x in txt if x not in dictionary]

    # Return results
    info = ""
    if len(mistakes) == 0:
        info += "Mistakes were not found."
    else:
        info += ("|> This words aren't in Polish dictionary. "
                 f"Check them for mistakes:\n{mistakes}")
    return info


def write_file(path: str, formatted_text: str) -> None:
    """"Writes formatted text to the path.

    Args:
        path (str): path to write formatted text
        formatted_text (str): formatted text

    Raises:
        OSError: wrong file extension

    Returns:
        str: succesful writting message
    """
    message = f"|> Text has been succesfully written into /{path}"

    # Alias for writing
    def do_writing(path) -> None:
        with open(path, "wt") as f:
            f.write(formatted_text)

    if not path.endswith((".txt", ".rtf", ".docx", ".doc", ".pdf", ".odt")):
        raise OSError("File extension must be "
                      "'.txt', '.rtf', '.docx', '.doc', '.pdf', '.odt'")
    else:
        # if text was read from file
        try:
            if path != in_path:
                do_writing(path)
                return message
            # else: rewrite the file
            answer = input(REWRITE)
            while True:
                if answer in POSITIVE_ANSWERS:
                    do_writing(path)
                    return message
                elif answer in NEGATIVE_ANSWERS:
                    path = input(ENTER_AGAIN)
                    return write_file(path, formatted_text)
                else:
                    answer = input(INVALID_ANSWER_TRY_AGAIN)
        # if text was read directly.
        except NameError:
            do_writing(path)
            return message
