import typing

import numpy as np

from src.poke_type import PokeType
from src.typecharts.VI import matrix


class TypeArray:
    def __init__(self, types: typing.Iterable[PokeType] = None):
        if types == None:
            types = []

        self.types = types

    @staticmethod
    def get_type_vector(types: typing.Iterable[PokeType]) -> np.ndarray:
        type_vector = np.zeros_like(matrix[0], dtype=int)

        for i in types:
            type_vector[i] = 1

        return type_vector

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

        return np.prod(multipliers)

    def interacts_with(self, interacting_types: typing.Iterable[PokeType], separate: bool = False):
        interactions = {}

        for type_ in self.types:
            if separate:
                interactions[type_] = self.get_type_interaction_multipliers(type_, interacting_types)

            else:
                interactions[type_] = self.get_type_interaction_product(type_, interacting_types)

        return interactions
