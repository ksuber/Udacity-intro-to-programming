import fresh_tomatoes
import videos


shaolin_vs_wutang = videos.Movies("Shaolin vs Wu Tang", " The film is about the rivalry\
between the martial arts schools Shaolin and Wu Tang. It is also called Shaolin and\
Wu-Tang in the Master Killer Collection.", "1 hour 27 min", "https://www.youtube.com/watch?v=eN2uwv96tHw",  # noqa
                                  "https://img.fstatic.com/w156DTY4vVozZKjgl-Iipn_VhRs=/fit-in/290x478/smart/https://cdn.fstatic.com/media/movies/covers/2010/12/7b013bf7c5d1d3293f74004ff903652f.jpg"  # noqa)

mystery_of_chessboxing=videos.Movies("Mystery of Chessboxing", "Lee Yi Min stars as a young boy,\
 Ah Pao, who wants to learn kung fu so that he can avenge his father's death at\
 the hands of the Ghost Faced Killer ", "1h 30min", "https://www.youtube.com/watch?v=R2fgGM4Y71U",  # noqa
                                       "https://i.pinimg.com/originals/3a/ff/c6/3affc64b2a60c260accc5110b0183035.jpg"  # noqa)


shogun_assassin=videos.Movies("Shogun Assassin", "When the wife of the Shogun's Decapitator is murdered and he is \
ordered to commit suicide by the paranoid Shogun, he and his four-year-old son escape and become assassins for hire,\
embarking on a journey of blood and violent death", "1h 25min", "https://www.youtube.com/watch?v=bFOjbAQmIjY",  # noqa
                                "https://www.limitedruns.com/media/images/productimage-picture-shogun-assassin-1146.JPG"  # noqa)

the_36_chambers_of_shaolin=videos.Movies("The 36 Chambers of Shaolin", "A man studies kung fu at the Shaolin Temple to fight back against the oppressive Manchu government.",  # noqa
                                           " 1h 55min",
                                           "https://www.youtube.com/watch?v=65GQtH6pzTY",  # noqa
                                           "http://www.cityonfire.com/wp-content/uploads/2011/03/600full-the-36th-chamber-of-shaolin-poster.jpg"  # noqa)


return_to_the_36th_chamber=videos.Movies("Return to the 36th Chamber",
                                         "A mistreated millworker learns martial arts to fight back\
                                          against his bosses",
                                           "1h 39min",
                                           "https://www.youtube.com/watch?v=kOlwlSvK8Y4",  # noqa
                                           "http://www.gstatic.com/tv/thumb/movieposters/6586/p6586_p_v8_aa.jpg"  # noqa)


the_shaolin_drunken_monk=videos.Movies("The Shaolin Drunken Monk", "The son of a martial arts teacher comes under\
 the tutelage of a hermit who instructs him in the ways of Drunken Kung Fu",
  "1h 23min ",
 "https://www.youtube.com/watch?v=nc9D1Yoj7dA", "https://sep.yimg.com/ay/yhst-61160669843094/shaolin-drunken-monk-3.gif"  # noqa)

movies=[shaolin_vs_wutang, mystery_of_chessboxing, shogun_assassin,
        the_36_chambers_of_shaolin, return_to_the_36th_chamber,
        the_shaolin_drunken_monk]

fresh_tomatoes.open_movies_page(movies)
