import webbrowser


class Videos(object):
     """Creates an intialized video object.
    Input:
        title, plot and duration.
    Behavior:
        Creates a video object.
    Attributes:
        Title (str): Movie Title
        plot (str): Movie Plot.
        duration (str): Movie length.
        
    Returns:
        Intialized video object.
    Methods:
        Can_I_Stream (str): Opens browser to video streaming check site.
        show_trailer (str) Opens browser to youtube to play trailer
    """
    vVALID_RATING = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, plot, duration):
        """ initalizes objects with attributes to display in tile"""
        self.title = title
        self.plot = plot
        self.duration = duration

    def Can_I_Stream(self):
       """Open the webbroser with a link to streaming video site.
    Input:
        None.
    Behavior:
        Opens the default webbroswer using self.title plus www.justwatch.com
        to display a site showing if the movie or show is availbl.
    Returns:
        None.

    """
        webbrowser.open("https://www.justwatch.com/us/search?q=" + self.title)

    def show_trailer(self):
        """Open the webbroser with the movie trailer.
    Input:
        None.
    Behavior:
        Opens the default webbroswer using self.trailer_youtube_trailer
        to display the movie trailer.
    Returns:
        None.

    """
        webbrowser.open(self.trailer)


class Movies(Videos):
   """Creates an intialized Movie object inherits from Parent class Videos .
    Input:
        title, plot,duration, trailer_youtube_url, poster_image_url.
    Behavior:
        Creates a Movie object.
    Attributes:
        Title (str): Movie Title
        plot (str): Movie Plot.
        duration (str): Movie length.
        trailer_youtube_url (str) Link to trailer on Youtube
        poster_image_url (str) Link to url for poster image
        
    Returns:
        Intialized Movie object.
    Methods:
        Can_I_Stream (str): Opens browser to video streaming check site.
        show_trailer (str) Opens browser to youtube to play trailer
    """

    def __init__(self, title, plot, duration, trailer_youtube_url, poster_image_url):
        ''' Inherents attributes for Video and sets trailer and poster '''
        super(Movies, self).__init__(title, plot, duration)
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url


class Tv_Shows(Videos):
      """Creates an intialized Tv show object inherits from Parent class Videos .
    Input:
        title, plot,duration, trailer_youtube_url, poster_image_url.
    Behavior:
        Creates a Movie object.
    Attributes:
        Title (str): Movie Title
        plot (str): Movie Plot.
        duration (str): Movie length.
        trailer_youtube_url (str) Link to trailer on Youtube
        poster_image_url (str) Link to url for poster image
        
    Returns:
        Intialized Tv show object.
    Methods:
        Can_I_Stream (str): Opens browser to video streaming check site.
        show_trailer (str) Opens browser to youtube to play trailer
    """
    def __init__(self, title, plot, duration, trailer_youtube_url, poster_image_url, ):
        ''' Inherents attributes for Video and sets trailer and poster '''
        super(Tv_Shows, self).__init__(title, plot, duration)
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
