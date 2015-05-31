#!/usr/bin/env python3

from argparse import ArgumentParser
from sys import argv

TOOL_DESC = "Provides information regarding how to use git in specific " \
            "ways and allows user to easily add to that information"
TOOL_NAME = "githow"

SUBCOMMANDS = ["config", "undo", "create", "shorthand"]
SUMCOMMAND_TO_HELP = {
    "config": "git configuration",
    "undo": "undoing things in git",
    "create": "temp",
    "shorthand": "temp"
}

APPEND_ARGS = ["-a", "--append"]
APPEND_HELP = "Append to end of file"

SUBPARSER_TITLE = "subcommands"
SUBPARSER_DESC = "Allow reading of and appending to corresponding help files"
SUBPARSER_HELP = "read usage: <subcommand>; " \
                 "edit usage: <subcommand> -a [new help message]"
SUBPARSER_APPEND_HELP = "append to help file; usage: <subcommand> -a [new help message]"

FILE_FOLDER = "help_files/"
UNDO_FILENAME = "undo"
CONFIG_FILENAME = "config"
CREATE_FILENAME = "create"
SHORTHAND_FILENAME = "shorthand"
FILENAMES = [UNDO_FILENAME, CONFIG_FILENAME, SHORTHAND_FILENAME]
FILENAME_TO_HEADER = {
    UNDO_FILENAME: "UNDOING THINGS:",
    CONFIG_FILENAME: "EDITING CONFIG FILE:",
    SHORTHAND_FILENAME: "USEFUL SHORTHAND:"
}


def default():
    """Print the full git help text."""
    print()
    for filename in FILENAMES:
        print_file(filename)
        print()


def print_file(filename):
    """Print the file header and the contents of the file."""
    with open(FILE_FOLDER + filename, 'r') as f:
        print(FILENAME_TO_HEADER[filename])
        print(f.read())


def append_file(filename, message):
    """Append the message to the end of the file."""
    with open(FILE_FOLDER + filename, 'a') as f:
        pass
        # f.write(message)


def get_args_message(args):
    # i = max(last_index(argv, "-a"), last_index(argv, "--append"), last_index())
    print(args)
    # need to figuer out how the keywords/filename stuff will work out
    # probably can all be put into an array


def last_index(l, x):
    for i, e in enumerate(reversed(l)):
        if e == x:
            return len(l) - 1 - i


def add_subparsers(parser):
    subparsers = parser.add_subparsers(title=SUBPARSER_TITLE,
                                       description=SUBPARSER_DESC,
                                       help=SUBPARSER_HELP)

    for subcommand in SUBCOMMANDS:
        subparser = subparsers.add_parser(subcommand,
                                          help=SUMCOMMAND_TO_HELP[subcommand])
        subparser.set_defaults(filename=subcommand)
        subparser.add_argument("-a", "--append", action="store_true",
                               help=SUBPARSER_APPEND_HELP)


def parse_args():
    """Parse the command-line arguments and return the result"""
    parser = ArgumentParser(description=TOOL_DESC, prog=TOOL_NAME)
    parser.add_argument("-a", "--append", action='store_true',
                        help=APPEND_HELP)

    add_subparsers(parser)

    args = parser.parse_args()
    if "-a" in argv or "--append" in argv:
        # append_file(args.filename, get_args_message(args))
        print("appended to " + args.filename + " file")
    else:
        print_file(args.filename)

    return parser.parse_args()


if __name__ == '__main__':
    if len(argv) == 1:  # no command line arguments
        default()
    else:
        parse_args()
