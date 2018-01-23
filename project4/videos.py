import webbrowser


class Videos(object):
    """ Class to create video objects for movies and shows """
    vVALID_RATING = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, plot, duration):
        """ initalizes objects with attributes to display in tile"""
        self.title = title
        self.plot = plot
        self.duration = duration

    def Can_I_Stream(self):
        """ Function to check if video is available on any streaming sites"""
        webbrowser.open("https://www.justwatch.com/us/search?q=" + self.title)

    def show_trailer(self):
        """Function to play trailer or lip form youtube or other service"""
        webbrowser.open(self.trailer)


class Movies(Videos):
    """ Class to hold movie object child of Videos"""

    def __init__(self, title, plot, duration, trailer_youtube_url, poster_image_url):
        ''' Inherents attributes for Video and sets trailer and poster '''
        super(Movies, self).__init__(title, plot, duration)
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url


class Tv_Shows(Videos):
    """ Class to hold tv show objects child of Videos"""

    def __init__(self, title, plot, duration, trailer_youtube_url, poster_image_url, ):
        ''' Inherents attributes for Video and sets trailer and poster '''
        super(Tv_Shows, self).__init__(title, plot, duration)
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
