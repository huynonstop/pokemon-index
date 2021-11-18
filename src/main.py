import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog='pks', description='Pokemon search')

    allow_otps = ['pkdex', 'type', 'move', 'item', 'ability']
    parser.add_argument('-o', '--options', type=str, required=True, nargs=1, choices=allow_otps,
                        action='store', metavar='OPTIONS', help=f'find options in {str(allow_otps)}')
    parser.add_argument('args', type=str,
                        nargs='+', metavar='A', help='Argument for find options')
    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    print(args)
    return 0


if __name__ == '__main__':
    main()
