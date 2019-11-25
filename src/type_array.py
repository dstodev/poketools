import typing

import numpy as np

from src.base_type import BaseType
from src.typecharts.VI import matrix


class TypeArray:
    def __init__(self, types: typing.Iterable[BaseType] = None):
        if types == None:
            types = []

        self.types = types

    @staticmethod
    def get_type_vector(types: typing.Iterable[BaseType]) -> np.ndarray:
        type_vector = np.zeros_like(matrix[0], dtype=int)

        for i in types:
            type_vector[i] = 1

        return type_vector

    @staticmethod
    def get_type_multipliers(type_: BaseType, types: typing.Iterable[BaseType]):
        multipliers = matrix[type_, types]
        effects = {}

        for i, interacting_type in enumerate(types):
            effects[interacting_type] = multipliers[i]

        return effects

    def interacts_with(self, types: typing.Iterable[BaseType], separate: bool = False):
        effectives = {}

        for type_ in self.types:
            if separate:
                effectives[type_] = self.get_type_multipliers(type_, types)

            else:
                multipliers = matrix[type_, types]
                effectives[type_] = np.prod(multipliers)

        return effectives
