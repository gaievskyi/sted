# -*- coding: utf-8 -*-
"""STED. Text beautifier.

The main executive module which runs program with specified
parameters.

Example:
        $ python3 sted.py <path or text> -sctm -p </path>

.. More info on _Github repository:
   https://github.com/beeklz/sted

"""


import scripts.functions as fn
import scripts.arguments as arg


def stedtxt(unformatted_text: str,
            spaces=False,
            capitals=False,
            find_mistakes=False,
            stats=False,
            path=None
            ) -> str:
    """Beautify text or text file.

    Allows to format a text according to printing standarts.
    Supports autocapitalize, autospaces after punctuation marks,
    removes extra spaces, shows statistics of a text.

    Args:
        unformatted_text (str): path to your text file / inline text.
        spaces (bool, optional): remove extra spaces. Defaults to False.
        capitals (bool, optional): autocapitalize where needed (new sentence). Defaults to False.
        find_mistakes (bool, optional): check for mistakes in the text, print log. Defaults to False.
        stats (bool, optional): print statistics (letters, sentences etc). Defaults to False.
        path (str | None, optional): path to write. Defaults to None.

    Raises:
        OSError: got file name with invalid extension in writting function.

    Returns:
        str: formatted text
    """
    formatted_text = fn.read_text(unformatted_text)
    out = ""

    if spaces:
        formatted_text = fn.remove_extra_spaces(formatted_text)
        formatted_text = fn.format_punctuation(formatted_text)

    if capitals:
        formatted_text = fn.format_uppercase(formatted_text)

    if stats:
        out += fn.get_stats(formatted_text)

    if find_mistakes:
        out += fn.find_mistakes(formatted_text) + "\n"

    # if `path` is defined, write the file:
    if path is not None:
        # if file extension is correct
        try:
            return "\n" + fn.write_file(path, formatted_text) + out
        # if file extension is invalid
        except OSError as e:
            return "|> " + str(e) + "\n" "Try again."
    # else, return results to console
    else:
        return "\n|> Formatted text:\n\n" + formatted_text + out


if __name__ == "__main__":
    args = arg.args()
    print(stedtxt(*args))
