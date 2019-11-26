import typing

import numpy as np

from src.poketype import PokeType
from src.typecharts.VI import matrix


class TypeList:
    def __init__(self, types: typing.Iterable[PokeType] = None):
        if types == None:
            types = []

        self.types = sorted(types)

    @staticmethod
    def get_type_interaction_multipliers(target_type: PokeType, interacting_types: typing.Iterable[PokeType]):
        multipliers = matrix[target_type, interacting_types]
        effects = {}

        for i, type_ in enumerate(interacting_types):
            effects[type_] = multipliers[i]

        return effects

    @staticmethod
    def get_type_interaction_product(target_type: PokeType, interacting_types: typing.Iterable[PokeType]):
        multipliers = matrix[target_type, interacting_types]

        key = sorted(interacting_types)
        key = tuple(key)

        return {key: np.prod(multipliers)}

    def interacts_with(self, interacting_types: typing.Iterable[PokeType], aggregate: bool = True):
        interactions = {}

        for type_ in self.types:
            if aggregate:
                interactions[type_] = self.get_type_interaction_product(type_, interacting_types)
            else:
                interactions[type_] = self.get_type_interaction_multipliers(type_, interacting_types)

        return interactions

    def get_interacting_types(self):
        interactions = {}

        for type_ in self.types:
            array = matrix.transpose()
            array = array[type_]
            array = np.ma.masked_equal(array, 1)  # type: np.ma.masked_array

            effects = {}
            for (i, multiplier), masked in zip(np.ndenumerate(array), array.mask):
                if not masked:
                    effects[PokeType(i[0])] = multiplier

            interactions[type_] = effects

        return interactions
