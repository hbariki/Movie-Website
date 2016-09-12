"In this file it creates Class for Movie trailers Application"
# Imports webbrowser module that helps to open movie trailer
import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        # default movie constructor intializes the data of the movie like title, storyline, poster_image, trailer_youtube
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # Instance method to open the youtube trailer for the class movie.
        webbrowser.open(self.trailer_youtube_url)
