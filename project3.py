question_bank = [['easy', """The original WU members are __A__, GZA, __B__ Man, Raekwon, __C__ Killah,
Inspectah Deck, __D__ God, Masta Killa, Ol Dirty Bastard and ocassionally __E__."""],

levels = ['easy', 'normal', 'hard', ]
answers = ['capadonna', 'u', 'ghostface', 'method', 'rza']

answer_keys = ["__A__", '__B__', '__C__', '__D__', '__E__']


def game_dificulty(user_difficulty, levels):
    if user_difficulty.lower() not in levels:
        user_difficulty = raw_input("""To start game begin by typing a difficulty level.
Acceptable choices are easy, normal, and hard""")
    else:
        return user_difficulty


def game_board(user_difficulty, question_bank):
    for row in question_bank:
        if row[0] == user_difficulty:
            question = " ".join(row[1:])
            # todo add print for level and rules and question display
            print str(question)
            return str(question)


def word_in_pos(word, answer_keys):
    for pos in answer_keys:
        if pos in word:
            return pos
    return None


def play_game(game_board, answer_keys, answers):
    count = 0
    replaced = []
    game_board = game_board.split()
    for word in game_board:
        answer = word_in_pos(word, answer_keys)
        if answer is not None:
            user_input = raw_input("Input an Answer: " + answer + " ")
            while user_input != answers[-1] and count <= 4:
                print "Incorrect Answer Try Again"
                count += 1

            else:
                print "Great! Correct Answer"
                popped = answers.pop()
                word = word.replace(answer, popped)
                replaced.append(word)
                print answers

        else:
            replaced.append(word)
        replaced = " ".join(replaced)
        return replaced
        print "You Loose"
# print question_bank[1][0]


user_difficulty = raw_input("""Welcome to 36 chambers. To start game begin by typing
a difficulty level. Acceptable choices are easy, normal,and hard: """)

print user_difficulty
game_dificulty(user_difficulty, levels)
gb = game_board(user_difficulty, question_bank)
play_game(gb, answer_keys, answers)
