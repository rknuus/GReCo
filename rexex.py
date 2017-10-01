#!/usr/bin/env python3

import CommonMark
import sys


def run(args):
    parser = CommonMark.Parser()
    ast = parser.parse(' '.join(args))
    CommonMark.dumpAST(ast)
    return 0


def main():
    sys.exit(run(sys.argv[1:]))


if __name__ == "__main__":
    # execute only if run as a script
    main()
