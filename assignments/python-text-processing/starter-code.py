"""Simple text processing CLI starter for the assignment.
Usage examples (see README for full instructions):

python starter-code.py --count-lines sample.txt
"""
import argparse
import sys
from collections import Counter
import re


def count_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)


def count_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    words = re.findall(r"\w+", text.lower())
    return len(words)


def main():
    parser = argparse.ArgumentParser(description='Text processing utilities starter')
    parser.add_argument('--count-lines', nargs=1, help='Count lines in file')
    parser.add_argument('--count-words', nargs=1, help='Count words in file')
    args = parser.parse_args()

    if args.count_lines:
        path = args.count_lines[0]
        try:
            print(count_lines(path))
        except FileNotFoundError:
            print('File not found:', path, file=sys.stderr)
            sys.exit(2)
    elif args.count_words:
        path = args.count_words[0]
        try:
            print(count_words(path))
        except FileNotFoundError:
            print('File not found:', path, file=sys.stderr)
            sys.exit(2)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
