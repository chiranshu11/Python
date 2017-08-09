import webbrowser
import entertainment_center

class Movie():
#init is a method used to initialize an object for the aspect of current movie
#Underscore or __ this indicates that the function name(here say init) is reserved in python
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,run_time):
#self,its a keyword which creates its object
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
#self.title returns movie title
#self.storyline return storyline
#self.poster_image_url returns poster image
#self.trailer_youtube_url returns youtube trailer 

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
