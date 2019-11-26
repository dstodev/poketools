import typing


def merge_symmetric_dict_values_by(op: typing.Callable, *dict_list: dict) -> dict:
    updated = {}

    for dict_ in dict_list:
        for k, v in dict_.items():
            if k in updated:
                updated[k] = op(updated[k], v)
            else:
                updated[k] = v

    return updated
