"""Sted: text beautifier.

This script allows the user to format their text according to printing
standarts. Supports autocapitalize, autospaces after commas and dots etc.

This tool accepts different text-files as (.txt) or (.docx) available
in OS Windows and MacOS, but you can test it even with other file extensions.

This script requires Python3 to be installed. Functions module is located at `sted/functions.py`. 

Contains the following functions:
    * stedtxt - the main function of the script
"""


import functions


def stedtxt(text_in: str, spaces=False, capitals=False, find_mistakes=False, stats=False, text_out=None) -> str:
    """
    Main STED function

    Args:
        text_in (str): path to your text file / printed actual text
        spaces (bool): removes extra spaces in your text
        capitals (bool): replaces lowercase to Uppercase if a new sentence
        find_mistakes (bool): checks for mistakes in a text, prints a log
        stats (bool): prints statistics of your text
        text_out (str or None): path to formatted file 

    Returns:
        text_formatted(str), stats(str): prints formatted text, statistics to terminal.

    """
    MESSAGE_LOG = "-"*5 + " CONSOLE LOG:"
    MESSAGE_TEXT = "-"*5 + " FORMATTED TEXT:\n"

    original_text = functions.open_text(text_in)
    formatted_text = original_text[:]
    mistakes = ""
    statistics = ""
    console_log = ""

    # if [format_spaces] is flagged:
    if spaces:
        formatted_text = functions.format_spaces(formatted_text)

    # if [capitals] is flagged:
    if capitals:
        formatted_text = functions.to_uppercase(formatted_text)

    # if [find_mistakes] is flagged:
    if find_mistakes:
        mistakes += functions.find_mistakes(formatted_text)

    # if [stats] is flagged:
    if stats:
        statistics += functions.get_stats(formatted_text)

    # Writing a file if [text_out] is flagged:
    if text_out is not None:
        console_log += MESSAGE_LOG + "\n" if stats or find_mistakes else ""
        return console_log + str(statistics) + "\n" + str(mistakes) + "\n" + functions.text_out(text_out, formatted_text)
    # Returning results to terminal if not
    else:
        console_log += MESSAGE_TEXT + formatted_text + "\n\n"
        console_log += MESSAGE_LOG + "\n" if stats or find_mistakes else ""
        return console_log + str(statistics) + "\n" + str(mistakes) + "\n"


if __name__ == "__main__":
    args = functions.args()
    print(stedtxt(*args))
