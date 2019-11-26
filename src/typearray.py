import typing
import operator

import numpy as np

from src.poketype import PokeType
from src.typecharts.VI import matrix
from src.util import merge_dicts_with


class TypeList:
    def __init__(self, types: typing.Iterable[PokeType] = None):
        if types == None:
            types = []

        self.types = sorted(types)

    @staticmethod
    def get_type_interaction_multipliers(target_type: PokeType, interacting_types: typing.Iterable[PokeType]) -> dict:
        multipliers = matrix[target_type, interacting_types]
        effects = {}

        for i, type_ in enumerate(interacting_types):
            effects[type_] = multipliers[i]

        return effects

    @staticmethod
    def get_type_interaction_product(target_type: PokeType, interacting_types: typing.Iterable[PokeType]) -> dict:
        multipliers = matrix[target_type, interacting_types]

        product = np.prod(multipliers)

        return product

    @staticmethod
    def get_all_type_interactions(target_type: PokeType, target_self: bool) -> np.ma.masked_array:
        if target_self:
            array = matrix.transpose()
        else:
            array = matrix

        array = array[target_type]
        array = np.ma.masked_equal(array, 1)

        return array

    @classmethod
    def get_all_type_interactions_by_multiplier(cls, target_type: PokeType, target_self: bool):
        array = cls.get_all_type_interactions(target_type, target_self)
        effects = {}

        for (i, multiplier), masked in zip(np.ndenumerate(array), array.mask):
            if not masked:
                effects[PokeType(i[0])] = multiplier

        return effects

    def interacts_with(self, interacting_types: typing.Iterable[PokeType], aggregate: bool = True):
        interactions = {}

        for type_ in self.types:
            if aggregate:
                interactions[type_] = self.get_type_interaction_product(type_, interacting_types)
            else:
                interactions[type_] = self.get_type_interaction_multipliers(type_, interacting_types)

        return interactions

    def get_all_interactions(self, strengths: bool = True, aggregate: bool = True):
        interactions = {}

        for type_ in self.types:
            type_interactions = self.get_all_type_interactions_by_multiplier(type_, not strengths)

            if aggregate:
                interactions = merge_dicts_with(operator.mul, interactions, type_interactions)
            else:
                interactions[type_] = type_interactions

        return interactions
