import argparse
import sys


def args():
    parser = argparse.ArgumentParser(
        description="Small Python text beautifier. Formats texts or text files.",
        usage=f"python {sys.argv[0]} path/text [-h] [-s] [-c] [-m] [-t] [-p path]"
    )
    # Input file or text [required]
    parser.add_argument("input",
                        metavar="path/text",
                        nargs=1,
                        help="Path to source file/Text itself"
                        )
    # Format spaces [optional]
    parser.add_argument("-s", "--spaces",
                        required=False,
                        action="store_const",
                        const=True,
                        default=False,
                        help="Formats spaces in the text. Removes exta spaces."
                        )
    # Formats capitals [optional]
    parser.add_argument("-c", "--capitals",
                        required=False,
                        default=False,
                        action="store_const",
                        const=True,
                        help="Capitalizes letters where needed (new sentence)")
    # Find mistakes [optional]
    parser.add_argument("-m", "--mistakes",
                        required=False,
                        default=False,
                        action="store_const",
                        const=True,
                        help="Finds mistakes and prints info. Only Polish supported.")
    # Print statistics [optional]
    parser.add_argument("-t", "--stats",
                        required=False,
                        default=False,
                        action="store_const",
                        const=True,
                        help="Returns the statistics of the text.")
    # Write to file [optional]
    parser.add_argument("-p", "--path",
                        required=False,
                        metavar="path",
                        default=None,
                        help="Path to output file('.txt', '.rtf', or '.doc')")
    args = parser.parse_args()
    inpath = args.input[0]
    spaces = args.spaces
    capitals = args.capitals
    mistakes = args.mistakes
    stats = args.stats
    path = args.path
    return inpath, spaces, capitals, mistakes, stats, path
