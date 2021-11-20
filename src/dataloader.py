import pandas as pd


class DataLoader:
    POKEDEX = 'pokedex'
    TYPES = 'types'
    MOVES = 'moves'
    ABILITITES = 'abilities'
    ITEMS = 'items'

    def __init__(self, data_folder_path='./data/raw-data') -> None:
        self.types_file = f'{self.TYPES}.csv'
        self.abilities_file = f'{self.ABILITITES}.csv'
        self.moves_file = f'{self.MOVES}.csv'
        self.items_file = f'{self.ITEMS}.csv'
        self.pokedex_file = f'{self.POKEDEX}.csv'

        self.data_folder_path = data_folder_path

        self._pokedex_df = self.read_pickle(self.POKEDEX)
        self._types_df = self.read_pickle(self.TYPES, 0)
        self._moves_df = self.read_pickle(self.MOVES)
        self._items_df = self.read_pickle(self.ITEMS)
        self._abilities_df = self.read_pickle(self.ABILITITES)

    def read_pickle(self, name, index=None):
        pickle_file = f'{name}.pickle'
        try:
            return pd.read_pickle(pickle_file)
        except FileNotFoundError:
            csv = pd.read_csv(
                f'{self.data_folder_path}/{name}.csv', index_col=index
            ).applymap(lambda s: s.lower() if type(s) == str else s)
            csv.to_pickle(pickle_file)
            return csv

    @property
    def pokedex(self):
        return self._pokedex_df

    @property
    def types(self):
        return self._types_df

    @property
    def abilities(self):
        return self._abilities_df

    @property
    def items(self):
        return self._items_df

    @property
    def moves(self):
        return self._moves_df
