import quiz_game as qg

# Questions for quiz list of list
question_bank = [['easy', """The original WU members are __A__, GZA, __B__ Man, Raekwon, __C__ Killah,
Inspectah Deck, __D__ God, Masta Killa, Ol Dirty Bastard and ocassionally __E__."""],
                 ['normal', """It had always been planned for __A__ Man to be the first breakout star from the groups lineup
with the b side of the first single being his now classic eponymous solo track. In __B__ 1994 his solo
album __C__ was released. It was entirely produced by __D__, who for the most part continued with the grimy,
raw textures he explored on 36 __E__."""],
                 ['hard', """In the late summer, and early fall of 1995 saw the release of Raekwons Only Built 4 __A__ Linx,
and GZAs __B__ Swords, which would turn out to be the groups two most significant and well-received
solo projects.The OBFCL album also featured rapper __C__, who was the first non Wu Tang affiliated MC to
appear on a Wu Tang Clan album. Nas was featured on the song verbal __D__. Ghostface followed soon
after with the __E__ man album"""], ]
# quiz levels
levels = ['easy', 'normal', 'hard', ]
# quiz answers list of list in reverse order
answers = [['easy', 'capadonna', 'u', 'ghostface', 'method', 'rza'],
           ['normal', 'chambers', 'rza', 'tical', 'november', 'method'],
           ['hard', 'iron', 'intercourse', 'nas', 'liquids', 'cuban'], ]
# blanks for quiz to replace with answers
answer_keys = ["__A__", '__B__', '__C__', '__D__', '__E__']


print "*" * 100
user_difficulty = raw_input("""Welcome to 36 chambers. To start game begin by typing
a difficulty level. Acceptable choices are easy, normal,and hard: """)


qg.game_dificulty(user_difficulty, levels)
gb, answers = qg.game_board(user_difficulty, question_bank, answers)
qg.play_game(gb, answer_keys, answers)
