import random

def guess_next_letter(pattern, used_letters=[], word_list=['about', 'abound', ...]):
    """Returns a letter from the alphabet.
    Input parameters:
				pattern: current state of the game board, with underscores "_" in the
            places of spaces (for example, "____e", that is, four underscores
            followed by 'e').
        used_letters: letters you have guessed in previous turns for the same
            word (for example, ['a', 'e', 's']).
        word_list: list of words from which the game word is drawn.
    """
    alphabetOriginalList = list("abcdefghigklmnopqrstuvwxyz")
    for item in used_letters:
        for alphabetItem in alphabetOriginalList:
            if alphabetItem == item:
                alphabetOriginalList.remove(alphabetItem)
    return alphabetOriginalList[random.randint(0, len(alphabetOriginalList) - 1)]


def test_function_should_return_something():
    pattern = "____e"
    used_letters = list("ab")
    word_list = [...]
    print(guess_next_letter(pattern, used_letters, word_list))
    assert guess_next_letter(pattern, used_letters, word_list) is not None


test_function_should_return_something()