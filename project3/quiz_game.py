import textwrap  # to wrap text printed to screen evenly


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
    # redraws the board updated withh a correct answer
    for key, answer in replace_keys:
        text = text.replace(key, answer.title())
    print "*" * 100 + "\n" + textwrap.fill(text, 75) + '\n' + "*" * 100


def wrong_answer(answer):
    print "\n\nIncorrect Answer Try Again"
    user_input = raw_input("Input an Answer for " + answer + " :")
    return user_input


def correct_answer(word, answer, answers, redrawn_board, replaced):
    new_board = []
    print "Great! Correct Answer\n\n"
    popped = answers.pop()
    word = word.replace(answer, popped)
    replacement_key = (answer, word)
    new_board.append(replacement_key)
    redraw_board(redrawn_board, new_board)
    word = word.replace(answer, popped)
    return replaced.append(word)


def play_game(game_board, answer_keys, answers):
    """ Game engine takes a board of questions plus answer and keys.
    splits questions into words to check for replacement and reassembles
     reprompts on incorrect and calls redraw_board on correct respones"""
    count, replaced = 0, []
    game_board = game_board.split()
    re_board = " ".join(game_board)
    for word in game_board:
        answer = word_in_pos(word, answer_keys)
        if answer is not None:
            user_input = raw_input("Input an Answer for " + answer + " : ")
            while user_input != answers[-1]:
                if count <= 3:
                    user_input = wrong_answer(answer)
                    count += 1
                else:
                    print "\n\nSorry You Loose"
                    return
            else:
                correct_answer(word, answer, answers, re_board, replaced)
        else:
            replaced.append(word)
    print "YOU WIN!!!\n\n" + " ".join(replaced)
