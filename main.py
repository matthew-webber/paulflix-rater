import re
import requests as r
import json


def clean_title(movie):
    non_title_chars = re.compile(r'(.+?)(?:.m4v.+| \(\d{1,4}p HD\).+| \(HD\).+)')

    movie_title = non_title_chars.match(movie)

    if movie_title:
        return movie_title.group(1).replace("_",":")

# titles = """Her Smell (1080p HD).m4v	2019-07-11 13:45 	2.8G
# Gloria Bell (1080p HD).m4v	2019-07-11 13:43 	1.6G
# After (HD).m4v	2019-07-10 15:10 	915M
# Through Black Spruce (1080p HD).m4v	2019-07-10 14:50 	1.8G
# Paper Year (1080p HD).m4v	2019-07-10 14:49 	1.4G
# Missing Link (1080p HD).m4v	2019-07-10 14:48 	1.5G
# Hellboy (1080p HD).m4v	2019-07-10 14:48 	2.0G
# Teen Spirit (HD).m4v	2019-07-06 11:25 	1.5G
# Alita_ Battle Angel (1080p HD).m4v	2019-06-29 15:52 	2.0G
# The Bits of Yesterday (1080p HD).m4v	2019-06-29 15:52 	1.7G
# Shaft (1080p HD).m4v	2019-06-29 15:51 	1.8G
# Making Babies (1080p HD).m4v	2019-06-29 15:51 	1.4G"""

#clean_titles = [clean_title(x) for x in titles.split('\n')]

movie_dict = {}
api_url = 'http://www.omdbapi.com/?apikey=f2caa646&t='.encode()

''' Input interface '''

while True:

    titles = input('Copy and paste entire lines below and press Enter.  Press X to exit.\n')

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

            movie_data = "Data"
            movie_dict[movie_title] = movie_data

    break # move to the next loop


print('\nMovies loaded.\n')

while True:

    print('To see Rotten Tomatoes rating, type [title] -r -rt.  For more, type -help.  To exit, type X.\n')

    command = input().strip().upper()

    if command == 'X':
        print('Exiting...')
        break
    elif command == '-help':
        pass
    elif command == '':
        pass