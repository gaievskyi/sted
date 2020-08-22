"""
This file can also be imported as a module and contains the following
functions:
    * read_text - opens a file with a text if exists, otherwise reads [text_in] as a text
    * format_spaces - formats spaces in the text
    * to_uppercase - capitalizes letters where needed (new sentence)
    * get_stats - returns statistics (letters, sentences etc)
    * find_mistakes - checks for mistakes in the text, prints log (supported: Polish)
    * write_file - writes formatted text to the path.
"""


def read_text(unformatted_text: str) -> str:
    """Tries to open a file with text, otherwise reads [text_in] as text.

    Arguments:
        unformatted_text (str) -- path to the file or inputed text.

    Returns:
        text (str) -- reads and returns text as a string
    """
    positive_answers = ("Yes", 'Y', "y", "yes")
    negative_answers = ("No", 'N', "n", "no")
    try:
        with open(unformatted_text, "rt") as f:
            # creating global var needed at writing func.
            global in_path
            in_path = unformatted_text
            # reading data
            text = f.read()
    except FileNotFoundError:
        answer = input("[*] File was not found. Read as a text? (Y/n): ")
        while True:
            if answer in positive_answers:
                text = unformatted_text
                break
            elif answer in negative_answers:
                unformatted_text = input("[*] Please, enter a path to your file again: ")
                return read_text(unformatted_text)
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
    punctuation = ",./!?"

    for i in range(len(text)-1):
        # removing 2+ extra spaces in a row
        if text[i] == " " and text[i+1] == " ":
            text = text[:i] + text[i+1:]
            return format_spaces(text)
        # formating spaces before/after special symbols
        if text[i] in punctuation:
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
    """Returns the statistics of the text.
    Contains quantity of spaces, lines, symbols, words.

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
    with open("dict.txt", "rt") as f:
        dictionary = f.read()
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


def write_file(path: str, formatted_text: str) -> None:
    """Writes formatted text to the path.

    Arguments:
        path (str) -- stores a path where will be formatted file
        formatted_text (str) -- stores a formatted text

    Raises:
        EnvironmentError -- occured by wrong extensions of writting file.

    Returns:
        message (str) -- succesful writting message
    """
    positive_answers = ("Yes", 'Y', "y", "yes")
    negative_answers = ("No", 'N', "n", "no")
    message = f"\n[=========] 100% Text has been succesfully written to '{path}'"

    if path.endswith((".txt", ".rtf", ".docx")):
        try:
            if path != in_path:
                with open(path, "wt") as f:
                    f.write(formatted_text)
                return message
            else:
                answer = input("[*] Are you sure you want to rewrite the file? (Y/n): ")
                if answer in positive_answers:
                    with open(path, "wt") as f:
                        f.write(formatted_text)
                    return message
                elif answer in negative_answers:
                    path = input("[*] Please, enter a path to your file again: ")
                    return write_file(path, formatted_text)
                else:
                    answer = input("[*] Invalid answer. Please, try again.")
        except NameError:
            with open(path, "wt") as f:
                f.write(formatted_text)
                return message
    else:
        raise EnvironmentError("File's extension must be .txt, .rtf or .docx")
