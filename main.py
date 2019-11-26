from src.poketype import PokeType
from src.typearray import TypeList

if __name__ == "__main__":
    t = TypeList([PokeType.Fighting])
    multipliers = t.interacts_with([PokeType.Normal, PokeType.Bug], False)
    product = t.interacts_with([PokeType.Normal, PokeType.Bug], True)

    types = t.get_interacting_types()

    pass
