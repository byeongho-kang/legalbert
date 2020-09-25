import re


def deduplicate_spaces(string, remove_newlines=True):
    single_spaced_string = str(string).strip()

    if remove_newlines:
        single_spaced_string = single_spaced_string.replace('\n', ' ').replace('\r', ' ')

    single_spaced_string = re.sub(' +', ' ', single_spaced_string)

    return single_spaced_string
