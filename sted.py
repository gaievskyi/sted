# STED: text beautifier. Python3 required.
# Functions module located at `sted/functions.py`
import functions as f
# `sted/arguments.py`
import arguments


def stedtxt(unformatted_text: str,
            spaces=False,
            capitals=False,
            find_mistakes=False,
            stats=False,
            path=None
            ):
    """
    Allows to format a text according to printing standarts.
    Supports autocapitalize, autospaces after punctuation marks
    etc. Works with (.txt), (.docx), (.rtf), try other extensions
    on your own risk.

    Args:
        unformatted_text (str): path to your text file / inline text
        spaces (bool): remove extra spaces
        capitals (bool): autocapitalize where needed (new sentence)
        find_mistakes (bool): check for mistakes in the text, print log
        stats (bool): print statistics (letters, sentences etc)
        path (str or None): path to write the file 
    """
    formatted_text = f.read_text(unformatted_text)
    mistakes = ""
    statistics = ""
    console_log = ""

    if spaces:
        formatted_text = f.format_spaces(formatted_text)

    if capitals:
        formatted_text = f.to_uppercase(formatted_text)

    if find_mistakes:
        mistakes += f.find_mistakes(formatted_text)

    if stats:
        statistics += f.get_stats(formatted_text)

    # Write a file if [text_out] is flagged:
    if path is not None:
        console_log += "[*] Additional info:\n" if stats or find_mistakes else ""
        return console_log + statistics + "\n" + mistakes + f.write_file(path, formatted_text)
    # Return results to console if not
    else:
        console_log += "[*] Formatted text:\n" + formatted_text
        console_log += "\n[*] Additional info:\n" if stats or find_mistakes else ""

        if len(statistics or mistakes) > 0:
            return console_log + statistics + "\n" + mistakes
        return console_log


if __name__ == "__main__":
    args = arguments.args()
    print(stedtxt(*args))
