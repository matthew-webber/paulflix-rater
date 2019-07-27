import re
import requests as r
import json

def print_dict_pairs_neat(dict, print_name):

    print('Printing {}...'.format(print_name))

    for k, v in dict.items():
        print('\t', k.title(), ':', v)


def print_ratings(dict):

    print('Printing ratings...')

    for k, v in dict.items():
        print('\t', '{} gave it {}'.format(k, v))


def parse_user_input(uinput):

    return re.match(r"([\w\W\d]+?) (-\w{1,4}) (-\w{1,4})", uinput)

class Movie:

    def __init__(self, title, movie_dict):

        self.title = title
        self.rated = movie_dict[title]['Rated'] # -m
        self.released = movie_dict[title]['Released'] # -p
        self.runtime = movie_dict[title]['Runtime'] # -m
        self.genre = movie_dict[title]['Genre'] # -m
        self.director = movie_dict[title]['Director'] # -p
        self.writers = movie_dict[title]['Writer'] # -p
        self.actors = movie_dict[title]['Actors'] # -p
        self.plot = movie_dict[title]['Plot'] # -m
        self.language = movie_dict[title]['Language'] # -m
        self.country = movie_dict[title]['Country'] # -m
        self.awards = movie_dict[title]['Awards'] # -m
        self.production = movie_dict[title]['Production'] # -p
        self.ratings = movie_dict[title]['Ratings'] # -r -m
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


movie_dict = {'Her Smell':{"Title":"Her Smell","Year":"2018","Rated":"R","Released":"10 May 2019","Runtime":"134 min","Genre":"Drama, Music","Director":"Alex Ross Perry","Writer":"Alex Ross Perry","Actors":"Elisabeth Moss, Angel Christian Roman, Cara Delevingne, Dan Stevens","Plot":"A self-destructive punk rocker struggles with sobriety while trying to recapture the creative inspiration that led her band to success.","Language":"English","Country":"USA, Greece","Awards":"N/A","Poster":"https://m.media-amazon.com/images/M/MV5BMTk2Mzg4NzI3NF5BMl5BanBnXkFtZTgwMzE5NDk1NzM@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.2/10"},{"Source":"Rotten Tomatoes","Value":"84%"},{"Source":"Metacritic","Value":"69/100"}],"Metascore":"69","imdbRating":"6.2","imdbVotes":"1,219","imdbID":"tt7942742","Type":"movie","DVD":"N/A","BoxOffice":"N/A","Production":"Gunpowder &amp; Sky","Website":"https://www.hersmellmovie.com/","Response":"True"},'Gloria Bell':{"Title":"Gloria Bell","Year":"2018","Rated":"R","Released":"22 Mar 2019","Runtime":"102 min","Genre":"Comedy, Drama, Romance","Director":"Sebastián Lelio","Writer":"Alice Johnson Boher (adapted screenplay), Sebastián Lelio, Gonzalo Maza (story)","Actors":"Julianne Moore, John Turturro, Caren Pistorius, Michael Cera","Plot":"A free-spirited woman in her 50s seeks out love at L.A. dance clubs.","Language":"English","Country":"Chile, USA","Awards":"N/A","Poster":"https://m.media-amazon.com/images/M/MV5BMTc5Nzc1OTk3OV5BMl5BanBnXkFtZTgwNDM1NTQ3NjM@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.4/10"},{"Source":"Metacritic","Value":"79/100"}],"Metascore":"79","imdbRating":"6.4","imdbVotes":"4,737","imdbID":"tt6902696","Type":"movie","DVD":"N/A","BoxOffice":"N/A","Production":"N/A","Website":"N/A","Response":"True"},'After':{"Title":"After","Year":"2019","Rated":"PG-13","Released":"12 Apr 2019","Runtime":"105 min","Genre":"Drama, Romance","Director":"Jenny Gage","Writer":"Tom Betterton (screenplay by), Tamara Chestna (screenplay by), Jenny Gage (screenplay by), Susan McMartin (screenplay by), Anna Todd (novel)","Actors":"Josephine Langford, Hero Fiennes Tiffin, Khadijha Red Thunder, Dylan Arnold","Plot":"A young woman falls for a guy with a dark secret and the two embark on a rocky relationship. Based on the novel by Anna Todd.","Language":"English","Country":"USA","Awards":"N/A","Poster":"https://m.media-amazon.com/images/M/MV5BOGUwMjk3YzktNDI0Yy00MzFiLWFjNmEtYTA2ODVjMzNhODhjXkEyXkFqcGdeQXVyOTQ1MDI4MzY@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"5.5/10"},{"Source":"Rotten Tomatoes","Value":"16%"},{"Source":"Metacritic","Value":"30/100"}],"Metascore":"30","imdbRating":"5.5","imdbVotes":"13,596","imdbID":"tt4126476","Type":"movie","DVD":"09 Jul 2019","BoxOffice":"N/A","Production":"Aviron Pictures","Website":"https://www.after-themovie.com/","Response":"True"}}

print('\nMovies loaded.\n')

'''parse the user input'''
uinput = 'After -r -all'
command = parse_user_input(uinput)

'''grab movie from the user input'''

if command.group(1) in movie_dict:
    movie = Movie(command.group(1), movie_dict)
else:
    #process_command(command.group(1))

'''if flag = -r then...'''

print_ratings(command.get_ratings())

'''if flag = -a then...'''

print_dict_pairs_neat(command.get_all_data(),'all data')

'''if flag = -p then...'''

print_dict_pairs_neat(command.get_production_data(),'production data')

'''if flag = -m then...'''

print_dict_pairs_neat(command.get_metadata(),'metadata')