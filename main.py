from src.poke_type import PokeType
from src.type_array import TypeArray

if __name__ == "__main__":
    t = TypeArray([PokeType.Fighting])
    multipliers = t.interacts_with([PokeType.Normal, PokeType.Bug], True)
    product = t.interacts_with([PokeType.Normal, PokeType.Bug], False)

    pass
