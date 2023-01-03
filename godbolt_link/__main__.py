"""Main entry point for godbolt_link and python -m godbolt_link"""
from .lib import make_godbolt_url


def main():
    """Main command line entry point"""
    import argparse

    description = 'Command-line tool and library to generate Compiler Explorer links'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--template', type=str, required=True,
                        help='This link would be used to set up panel layout, compilers, options etc. '
                             'To get it, open godbolt.org, place @place_the_code_here@ text in source window. '
                             'Then get link via \'>Share>Full Link\' in the right top corner')
    parser.add_argument('src', type=str, nargs=1,
                        help='Path to source code file')
    args = parser.parse_args()

    with open(args.src[0], "r") as file:
        source = file.read()

    print(make_godbolt_url(args.template, source))


if __name__ == '__main__':
    main()
