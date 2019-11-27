import typing
import operator

import numpy as np

from src.poketype import PokeType
from src.typecharts.VI import matrix
from src.util import merge_symmetric_dict_values_by


class TypeList:
    def __init__(self, types: typing.Iterable[PokeType] = None):
        if types == None:
            types = []

        self.types = sorted(types)

    @staticmethod
    def _get_type_interaction_multipliers(target_type: PokeType, interacting_types: typing.Iterable[PokeType]) -> dict:
        multipliers = matrix[target_type, interacting_types]
        effects = {}

        for i, type_ in enumerate(interacting_types):
            effects[type_] = multipliers[i]

        return effects

    @staticmethod
    def _get_type_interaction_product(target_type: PokeType, interacting_types: typing.Iterable[PokeType]) -> dict:
        multipliers = matrix[target_type, interacting_types]

        product = np.prod(multipliers)

        return product

    @staticmethod
    def _get_all_type_interactions(target_type: PokeType, target_self: bool):
        if target_self:
            array = matrix.transpose()
        else:
            array = matrix

        array = array[target_type]

        effects = {}
        for i, multiplier in enumerate(array):
            if multiplier != 1:
                effects[PokeType(i)] = multiplier

        return effects

    def interacts_with(self, interacting_types: typing.Iterable[PokeType], aggregate: bool = True) -> dict:
        interactions = {}

        for type_ in self.types:
            if aggregate:
                interactions[type_] = self._get_type_interaction_product(type_, interacting_types)
            else:
                interactions[type_] = self._get_type_interaction_multipliers(type_, interacting_types)

        return interactions

    def get_all_interactions(self, strengths: bool = True, aggregate: bool = True) -> dict:
        interactions = {}

        for type_ in self.types:
            type_interactions = self._get_all_type_interactions(type_, not strengths)

            if aggregate:
                interactions = merge_symmetric_dict_values_by(operator.mul, interactions, type_interactions)
            else:
                interactions[type_] = type_interactions

        if aggregate:
            interactions = {k: v for k, v in interactions.items() if v != 1}

        return interactions
