import re

flag_dict = {
    'Flag1': {'Action': "Print movie ratings", 'Symbol': 'r'},
    'Flag2': {'Action': "Print all movie data", 'Function': "_", 'Symbol': 'a'},
    'Flag3': {'Action': "Print movie production Function", 'Other': "_", 'Symbol': 'p'},
    'Flag4': {'Action': "Print movie metadata", 'Function': "_", 'Symbol': 'm'}}

help_plz_kthx = """
    *** Begin Help File ***

    General help

    To do this, type "that" and press enter.
    To do something else, type "thisthat" and press enter.

    Flags List

    -{flag1} :   {flag1_action}
    -{flag2} :   {flag2_action}
    -{flag3} :   {flag3_action}
    -{flag4} :   {flag4_action}

    *** End Help File ***

    """.format(
    flag1=flag_dict['Flag1']['Symbol'],
    flag2=flag_dict['Flag2']['Symbol'],
    flag3=flag_dict['Flag3']['Symbol'],
    flag4=flag_dict['Flag4']['Symbol'],
    flag1_action=flag_dict['Flag1']['Action'],
    flag2_action=flag_dict['Flag2']['Action'],
    flag3_action=flag_dict['Flag3']['Action'],
    flag4_action=flag_dict['Flag4']['Action'],
)


def clean_title(movie):

    unformatted_title = re.match(r'(.+?)(?:.m4v.+| \(\d{1,4}p HD\).+| \(HD\).+)', movie)

    if unformatted_title:
        return unformatted_title.group(1).replace("_", ":")


def flatten_string(string):

    return string.upper().strip()


def print_help():

    print(help_plz_kthx)


def print_movies(movie_dict):

    for movie in movie_dict:
        print(movie)


def print_dict_pairs_neat(dict, print_name):

    print('Printing {}...'.format(print_name))

    for k, v in dict.items():
        print('\t', k.title(), ':', v)


def print_ratings(dict):

    print('Printing ratings...')

    for k, v in dict.items():
        print('\t', '{} gave it {}'.format(k, v))


def parse_user_input(uinput):
    #todo remove third flag element
    match_object = re.match(r"([\w\W\d]+?) (-\w{1,4})", uinput)
    if match_object is None:
        return uinput
    return match_object