import argparse as ap

from src.poketype import PokeType
from src.typearray import TypeList


def get_parameters():
    parser = ap.ArgumentParser(description="Enter types and this program will output type matchups")

    parser.add_argument("types", metavar="TYPE", type=str.capitalize, nargs="+",
                        help="Types to calculate matchups against", choices=[type_.name for type_ in PokeType])

    return parser.parse_args()


if __name__ == "__main__":
    args = get_parameters()

    types = [PokeType[type_name] for type_name in args.types]
    types = TypeList(types)
    interactions = types.get_all_interactions(False)
    interactions = {k: interactions[k] for k in sorted(interactions, key=interactions.get, reverse=True)}

    all_types = [type_.name for type_ in PokeType]
    type_name_width = len(max(all_types, key=len))

    print(f"\nSelected types are: {', '.join(args.types)}")
    print(f"Multipliers against these types:")
    for weakness, multiplier in interactions.items():
        print(f"    {weakness.name:<{type_name_width}} {multiplier}")
