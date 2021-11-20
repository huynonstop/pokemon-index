from pandas import DataFrame


class Handler:
    @staticmethod
    def pkdex(pokedex_df: DataFrame, name):
        return pokedex_df[pokedex_df['name'].str.startswith(name)]

    @staticmethod
    def type(types_df: DataFrame, *t):
        rs = types_df.loc[:, list(t)]
        rs.loc[:, 'total'] = rs.prod(axis=1)
        return rs.sort_index().sort_values(by=['total'], ascending=False)

    @staticmethod
    def move(moves_df: DataFrame, t):
        return moves_df[moves_df['type'] == t].sort_values(by=['type_damage'])

    @staticmethod
    def item(item_df: DataFrame, name):
        return item_df[item_df['name'].str.startswith(name)].sort_values(by=['cat', 'name'])

    @staticmethod
    def ability(pokedex_df: DataFrame, name):
        return pokedex_df[pokedex_df['ability_1'].str.startswith(name) | pokedex_df['ability_2'].str.startswith(name)]

    @staticmethod
    def ability_name(ab_df: DataFrame, name):
        return ab_df[ab_df['name'].str.startswith(name)].sort_values(by=['gen'])
