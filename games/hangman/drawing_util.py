def draw_hangman(remaining_lives):
    match remaining_lives:
        case 6:
            draw_hangman_step_one()
        case 5:
            draw_hangman_step_two()
        case 4:
            draw_hangman_step_three()
        case 3:
            draw_hangman_step_four()
        case 2:
            draw_hangman_step_five()
        case 1:
            draw_hangman_step_six()
        case 0:
            draw_hangman_step_seven()


def draw_hangman_step_one():
    print("___|___")


def draw_hangman_step_two():
    print(
        "   |/\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_three():
    print(
        "   _______\n"
        "   |/ \n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_four():
    print(
        "   _______\n"
        "   |/    |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_five():
    print(
        "   _______\n"
        "   |/    |\n"
        "   |    (_)\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_six():
    print(
        "   _______\n"
        "   |/    |\n"
        "   |    (_)\n"
        "   |    \|/\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_seven():
    print(
        "   _______\n"
        "   |/    |\n"
        "   |    (_)\n"
        "   |    \|/\n"
        "   |     |\n"
        "   |    / \\\n"
        "___|___")
