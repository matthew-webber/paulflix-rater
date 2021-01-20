import re
import requests as r
import json
from func_lib import *


def input_reader(command):

    if command == 'X':
        return "Exiting..."


# class UserCommand:
#
#     def __init__(self, command, flag1, flag2):
#         self.command = command
#         self.flag1 = flag1
#         self.flag2 = flag2
#
#     def get_ratings(self, movie_dict):
#         if self.flag2 == '-rt':
#             pass







titles = """Her Smell (1080p HD).m4v	2019-07-11 13:45 	2.8G
Gloria Bell (1080p HD).m4v	2019-07-11 13:43 	1.6G
After (HD).m4v	2019-07-10 15:10 	915M"""

#clean_titles = [clean_title(x) for x in titles.split('\n')]

movie_dict = {}
api_url = 'http://www.omdbapi.com/?apikey=f2caa646&t='.encode()

''' Input interface '''

while True:

    # titles = input("""
    # First things first, you have to load movies into the program.
    # Copy and paste entire lines below and press Enter.
    # Press X to exit.\n""")

    if titles.strip().upper() == 'X':
        print('Exiting...')
        break
    elif titles.strip() == '':
        print('Command not recognized.\n')
    else:

        ''' Cleaning input '''

        print('Loading movies...\n')

        for dirty_title in titles.split('\n'):

            movie_title = clean_title(dirty_title)

            if movie_title == None:
                print('Skipping {}...'.format(dirty_title))
                continue

            movie_data = json.loads("""{}""")
            movie_dict[movie_title] = movie_data

    break # move to the next loop


print('\nMovies loaded.\n')

# print('To see Rotten Tomatoes rating, type [title] -r -rt.  For more, type -help.  To exit, type X.\n')

# # _ = input().upper().strip()
# _ = "Her Smell -r -rt"
# _ = re.match(r"([\w\W\d]+?) (-\w{1,4}) (-\w{1,4})", _)
# command = UserCommand(_.group(1), _.group(2), _.group(3))
