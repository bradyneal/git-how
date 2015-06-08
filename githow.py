#!/usr/bin/env python

from argparse import ArgumentParser
from sys import argv
from os.path import join, abspath
from builtins import input


TOOL_DESC = "Provides information regarding how to use git in specific " \
            "ways and allows user to easily add to that information"
TOOL_NAME = "githow"

SUBCOMMANDS = ["config", "undo", "create", "shorthand"]
SUMCOMMAND_TO_HELP = {
    "config": "git configuration",
    "undo": "undoing things in git",
    "create": "starting new projects in git",
    "shorthand": "useful git shorthand"
}

SUBPARSER_TITLE = "subcommands"
SUBPARSER_DESC = "Allow reading of and appending to corresponding help files"
SUBPARSER_HELP = "read usage: <subcommand>; " \
                 "edit usage: <subcommand> -a [new help message]"
SUBPARSER_APPEND_HELP = "append to help file"

FILE_FOLDER = "help_files/"


def default():
    """Print the full git help text."""
    print("")
    for filename in SUBCOMMANDS:
        print_file(filename)


def print_file(filename):
    """Print the file header and the contents of the file."""
    with open(build_path(filename), 'r') as f:
        print(f.read())


def append_to_help_file(filename, message):
    """Append the message to the end of the file."""
    message = " ".join(message)
    confirmed = None
    while confirmed is None:
        confirmed = process_yes_no_response(input(
            'Are you sure you want to append "' + message +
            '" to the ' + filename + ' file? (y/n): '))
    if confirmed:
        with open(build_path(filename), 'a') as f:
            f.write(message + "\n")
            print('appended "' + message + '"' +
                  " to " + filename + " file")


def process_yes_no_response(response):
    """
    Return True if the response is affirmative,
    False if the response is negative,
    or None if the response is neither affirmative nor negative.
    """
    response = response.lower()
    affirmative = ["yes", "y"]
    negative = ["no", "n"]
    if response in affirmative:
        return True
    if response in negative:
        return False


def build_path(help_file):
    """Build the absolute path to the help file."""
    return abspath(join(FILE_FOLDER, help_file))


def add_subparsers(parser):
    """Add all of the subcommand subparsers."""
    subparsers = parser.add_subparsers(title=SUBPARSER_TITLE,
                                       description=SUBPARSER_DESC,
                                       help=SUBPARSER_HELP)

    for subcommand in SUBCOMMANDS:
        subparser = subparsers.add_parser(subcommand,
                                          help=SUMCOMMAND_TO_HELP[subcommand])
        subparser.set_defaults(filename=subcommand)
        subparser.add_argument("-a", "--append", default=False, nargs="+",
                               dest="message", help=SUBPARSER_APPEND_HELP)


def parse_args(args):
    """Parse the command-line arguments and return the result."""
    parser = ArgumentParser(description=TOOL_DESC, prog=TOOL_NAME)
    add_subparsers(parser)
    return parser.parse_args(args)


if __name__ == '__main__':
    if len(argv) == 1:  # no command line arguments
        default()
    else:
        parsed = parse_args(argv[1:])
        if parsed.message:
            append_to_help_file(parsed.filename, parsed.message)
        else:
            print_file(parsed.filename)