from src.base_type import BaseType
from src.type_array import TypeArray

if __name__ == "__main__":
    t = TypeArray([BaseType.Fighting])
    multiplier = t.interacts_with([BaseType.Normal, BaseType.Bug], True)

    pass
