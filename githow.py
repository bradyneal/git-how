#!/usr/bin/env python3

from argparse import ArgumentParser
from sys import argv

DESCRIPTION = "Provides information regarding how to use git in specific ways"
PROGRAM_NAME = "githow"

FILE_FOLDER = "help_files/"
UNDO_FILENAME = "undo"
CONFIG_FILENAME = "config"
CREATE_FILENAME = "create"
SHORTHAND_FILENAME = "shorthand"
FILENAMES = [UNDO_FILENAME, CONFIG_FILENAME, SHORTHAND_FILENAME]
FILENAME_TO_HEADER = {
    UNDO_FILENAME : "UNDOING THINGS:",
    CONFIG_FILENAME : "EDITING CONFIG FILE:",
    SHORTHAND_FILENAME : "USEFUL SHORTHAND:"
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

def parse_args():
    parser = ArgumentParser(description=DESCRIPTION, prog=PROGRAM_NAME)
    subparsers = parser.add_subparsers()

    undo_parser = subparsers.add_parser("undo", help="temp")
    undo_parser.set_defaults(filename=UNDO_FILENAME)

    config_parser = subparsers.add_parser("config", help="temp")
    config_parser.set_defaults(filename=CONFIG_FILENAME)

    return parser.parse_args()

if __name__ == '__main__':
    if len(argv) == 1:  # no command line arguments
        default()
    else:
        args = parse_args()
        print_file(args.filename)