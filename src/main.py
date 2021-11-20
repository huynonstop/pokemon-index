import argparse

from dataloader import DataLoader
from handler import Handler


def create_parser():
    parser = argparse.ArgumentParser(
        prog='pks', description='Pokemon search')

    allow_otps = ['pkdex', 'type', 'move', 'item', 'ability', 'ability_name']
    parser.add_argument('-o', '--options', type=str, required=True, choices=allow_otps,
                        action='store', metavar='OPTIONS', help=f'find options in {str(allow_otps)}')
    parser.add_argument('args', type=str.lower,
                        nargs='+', metavar='A', help='Argument for find options')
    return parser, allow_otps


def main() -> None:
    parser, allow_otps = create_parser()
    args = parser.parse_args()
    dl = DataLoader()
    if args.options == allow_otps[0]:
        print(Handler.pkdex(dl.pokedex, args.args[0]))
    elif args.options == allow_otps[1]:
        print(Handler.type(dl.types, *args.args))
    elif args.options == allow_otps[2]:
        print(Handler.move(dl.moves, args.args[0]))
    elif args.options == allow_otps[3]:
        print(Handler.item(dl.items, args.args[0]))
    elif args.options == allow_otps[4]:
        print(Handler.ability(dl.pokedex, args.args[0]))
    elif args.options == allow_otps[5]:
        print(Handler.ability_name(dl.abilities, args.args[0]))
    return 0


if __name__ == '__main__':
    main()
