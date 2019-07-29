import requests as r
import json
import func_lib

#todo check if the movie_dict[movie]["Title"] matches the key (movie title)
# if it doesn't, prompt user to fix the key / add more details and GET
# again / skip the record

def flag_process(flag):
    '''
    if flag -r print ratings
    if flag -a print all
    if flag -p print production data
    if flag -m print metadata
    :param flag:
    :return:
    '''

    # todo look for "-" to indicate flag
    # todo better way to strip flag of minus sign?

    flag = flag.replace("-", "")

    if flag == 'r':
        func_lib.print_dict_pairs_neat(movie.get_ratings(), 'ratings')
    elif flag == 'a':
        func_lib.print_dict_pairs_neat(movie.get_all_data(), 'all data')
    elif flag == 'p':
        func_lib.print_dict_pairs_neat(movie.get_production_data(), 'production data')
    elif flag == 'm':
        func_lib.print_dict_pairs_neat(movie.get_metadata(), 'metadata')

class Movie:

    def __init__(self, title, movie_dict):

        #todo if any of these values are missing, it shouldn't do a keyerror
        self.title = title
        self.rated = movie_dict[title]['Rated']  # -m
        self.released = movie_dict[title]['Released']  # -p
        self.runtime = movie_dict[title]['Runtime']  # -m
        self.genre = movie_dict[title]['Genre']  # -m
        self.director = movie_dict[title]['Director']  # -p
        self.writers = movie_dict[title]['Writer']  # -p
        self.actors = movie_dict[title]['Actors']  # -p
        self.plot = movie_dict[title]['Plot']  # -m
        self.language = movie_dict[title]['Language']  # -m
        self.country = movie_dict[title]['Country']  # -m
        self.awards = movie_dict[title]['Awards']  # -m
        self.production = movie_dict[title]['Production']  # -p
        self.ratings = movie_dict[title]['Ratings']  # -r -m
        self.imdb_votes = movie_dict[title]['imdbVotes']

    def get_ratings(self):

        ratings_dict = {}

        for rating in self.ratings:

            if rating['Source'] == 'Internet Movie Database':
                ratings_dict[rating['Source']] = "{} from {} votes".format(rating['Value'], self.imdb_votes)
            else:
                ratings_dict[rating['Source']] = rating['Value']

        return ratings_dict

    def get_all_data(self):

        return self.__dict__

    def get_production_data(self):

        production_dict = {
            'Released': self.released,
            'Writers': self.writers,
            'Director': self.director,
            'Actors': self.actors,
            'Studio': self.production
        }

        return production_dict

    def get_metadata(self):

        metadata_dict = {
            'Title': self.title,
            'Rated': self.rated,
            'Runtime': self.runtime,
            'Genre': self.genre,
            'Plot': self.plot,
            'Language': self.language,
            'Country': self.country,
            'Awards': self.awards,
            'Ratings': self.ratings,
            'Imdb_votes': self.imdb_votes
        }

        return metadata_dict


''' Ask for movies '''

movie_dict = {}

while True:

    titles = input("""
    First things first, you have to load movies into the program.
    Copy and paste entire lines below and press Enter.
    Press X to exit.\n""")

    if titles.strip().upper() == 'X':
        print('Exiting...')
        break

    elif titles.strip() == '':
        print('Command not recognized.\n')
        continue

    else:
        ''' Cleaning input '''

        print('Loading movies...\n')

        api_url = 'http://www.omdbapi.com/?apikey=f2caa646&t='.encode()

        for dirty_title in titles.split('\n'):

            movie_title = func_lib.clean_title(dirty_title)

            if movie_title == None:

                print('Skipping {}...'.format(dirty_title))
                continue

            ''' get REQUESTS data '''

            # response = r.get(api_url + movie_title.encode())
            #
            # movie_data = json.loads(response.text)
            # movie_dict[movie_title] = movie_data

        break # move to the next loop


print('\nMovies loaded.\n')


movie_dict = {'Her Smell':{"Title":"Her Smell","Year":"2018","Rated":"R","Released":"10 May 2019","Runtime":"134 min","Genre":"Drama, Music","Director":"Alex Ross Perry","Writer":"Alex Ross Perry","Actors":"Elisabeth Moss, Angel Christian Roman, Cara Delevingne, Dan Stevens","Plot":"A self-destructive punk rocker struggles with sobriety while trying to recapture the creative inspiration that led her band to success.","Language":"English","Country":"USA, Greece","Awards":"N/A","Poster":"https://m.media-amazon.com/images/M/MV5BMTk2Mzg4NzI3NF5BMl5BanBnXkFtZTgwMzE5NDk1NzM@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.2/10"},{"Source":"Rotten Tomatoes","Value":"84%"},{"Source":"Metacritic","Value":"69/100"}],"Metascore":"69","imdbRating":"6.2","imdbVotes":"1,219","imdbID":"tt7942742","Type":"movie","DVD":"N/A","BoxOffice":"N/A","Production":"Gunpowder &amp; Sky","Website":"https://www.hersmellmovie.com/","Response":"True"},'Gloria Bell':{"Title":"Gloria Bell","Year":"2018","Rated":"R","Released":"22 Mar 2019","Runtime":"102 min","Genre":"Comedy, Drama, Romance","Director":"Sebastián Lelio","Writer":"Alice Johnson Boher (adapted screenplay), Sebastián Lelio, Gonzalo Maza (story)","Actors":"Julianne Moore, John Turturro, Caren Pistorius, Michael Cera","Plot":"A free-spirited woman in her 50s seeks out love at L.A. dance clubs.","Language":"English","Country":"Chile, USA","Awards":"N/A","Poster":"https://m.media-amazon.com/images/M/MV5BMTc5Nzc1OTk3OV5BMl5BanBnXkFtZTgwNDM1NTQ3NjM@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.4/10"},{"Source":"Metacritic","Value":"79/100"}],"Metascore":"79","imdbRating":"6.4","imdbVotes":"4,737","imdbID":"tt6902696","Type":"movie","DVD":"N/A","BoxOffice":"N/A","Production":"N/A","Website":"N/A","Response":"True"},'After':{"Title":"After","Year":"2019","Rated":"PG-13","Released":"12 Apr 2019","Runtime":"105 min","Genre":"Drama, Romance","Director":"Jenny Gage","Writer":"Tom Betterton (screenplay by), Tamara Chestna (screenplay by), Jenny Gage (screenplay by), Susan McMartin (screenplay by), Anna Todd (novel)","Actors":"Josephine Langford, Hero Fiennes Tiffin, Khadijha Red Thunder, Dylan Arnold","Plot":"A young woman falls for a guy with a dark secret and the two embark on a rocky relationship. Based on the novel by Anna Todd.","Language":"English","Country":"USA","Awards":"N/A","Poster":"https://m.media-amazon.com/images/M/MV5BOGUwMjk3YzktNDI0Yy00MzFiLWFjNmEtYTA2ODVjMzNhODhjXkEyXkFqcGdeQXVyOTQ1MDI4MzY@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"5.5/10"},{"Source":"Rotten Tomatoes","Value":"16%"},{"Source":"Metacritic","Value":"30/100"}],"Metascore":"30","imdbRating":"5.5","imdbVotes":"13,596","imdbID":"tt4126476","Type":"movie","DVD":"09 Jul 2019","BoxOffice":"N/A","Production":"Aviron Pictures","Website":"https://www.after-themovie.com/","Response":"True"}}


'''parse the user input'''


while True:

    command = input('\nEnter [movie] -[flag] and press enter.  Type "help" for more info.  Type "X" to exit.\n')

    if command.strip().lower() == 'help':
        func_lib.print_help()

    if command.strip().lower() == 'x':
        print('Exiting...')
        break

    command = func_lib.parse_user_input(command)

    '''grab command from the user input'''

    try:
        if command.group(1) in movie_dict:
            movie = Movie(command.group(1), movie_dict)
            flag_process(command.group(2))

        else:
            print(
                'Movie not recognized.\n'
                '*** TITLES ARE CASE-SENSITIVE ***\n'
                'To see the loaded movies, type "movies!".  For list of flags type "help!" and press enter.'
            )

    except AttributeError:
        if command in movie_dict:
            print('Flag not recognized.\nAdd a flag and try again.  For list of flags type "help!" and press enter.')
        else:
            print('Command not recognized.\nFor list of commands type "help!" and press enter.')