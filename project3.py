import textwrap  # to wrap text printed to screen evenly

#Questions for quiz list of list
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


def game_dificulty(user_difficulty, levels):
    # prompts user to select level until correct choice made returns user level
    while user_difficulty.lower() not in levels:
        user_difficulty = raw_input("""To start game begin by typing a difficulty level.
Acceptable choices are easy, normal, and hard:""")
    else:
        return user_difficulty


def game_board(user_difficulty, question_bank, answers):
    # selects the correct level questions and answers and returns value
    for row in question_bank:
        if row[0] == user_difficulty:
            question = " ".join(row[1:])
    for row in answers:
        if row[0] == user_difficulty:
            answers = row[1:]
    print "You have 5 guesses to complete"
    print " \n" + "*" * 100 + "\n" + textwrap.fill(str(question), 75) + '\n' + "*" * 100
    return str(question), answers


def word_in_pos(word, answer_keys):
    # Checks if current word is equal to an answer key blank
    for pos in answer_keys:
        if pos in word:
            return pos
    return None


def redraw_board(text, replace_keys):
    #redraws the board updated withh a correct answer 
    for key, answer in replace_keys:
        text = text.replace(key, answer.title())
    print "*" * 100 + "\n" + textwrap.fill(text, 75) + '\n' + "*" * 100


def play_game(game_board, answer_keys, answers):
    """ Game engine takes a board of questions plus answer and keys.
    splits questions into words to check for replacement and reassembles 
     reprompts on incorrect and calls redraw_board on correct respones"""
    count = 0
    replaced = []
    game_board = game_board.split()
    re_board = " ".join(game_board)
    new_board = []
    for word in game_board:
        answer = word_in_pos(word, answer_keys)
        if answer is not None:
            user_input = raw_input("Input an Answer for " + answer + " : ")
            while user_input != answers[-1]:
                if count <= 3:
                    print "\n\nIncorrect Answer Try Again"
                    count += 1
                    user_input = raw_input("Input an Answer for " + answer + " :")

                else:
                    print "Sorry You Loose"
                    return None

            else:
                print "Great! Correct Answer\n\n"
                popped = answers.pop()
                word = word.replace(answer, popped)
                replaced.append(word)
                replacement_key = (answer, word)
                new_board.append(replacement_key)
                redraw_board(re_board, new_board)

        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    print replaced

# print question_bank[1][0]


print "*" * 100
user_difficulty = raw_input("""Welcome to 36 chambers. To start game begin by typing
a difficulty level. Acceptable choices are easy, normal,and hard: """)


game_dificulty(user_difficulty, levels)
gb, answers = game_board(user_difficulty, question_bank, answers)
play_game(gb, answer_keys, answers)
