def reverse_dict(dict):
    dict = {value:key for key, value in dict.items()}
    return dict
    # swap keys and values within dict and return dict