import string

def inversion():
    """To invert ABC in reverse table ZYX

    Args:
        word (String): Enter the word you want to invert
    """

    abc = "".join(string.ascii_uppercase)
    # print(abc)

    inverse = str.maketrans(abc, abc[::-1], ' ')
    word = str(input("Enter a word for inversion : "))
    inverted = word.upper().translate(inverse)
    print("The inverted word for the word ", word ," is : ", inverted)
    return inverted


def static_inversion(word):
    """To invert ABC in reverse table ZYX

    Args:
        word (String): The static word you want to invert
    """

    abc = "".join(string.ascii_uppercase)
    # print(abc)

    inverse = str.maketrans(abc, abc[::-1], ' ')
    inverted = str(word).upper().translate(inverse)
    print("The inverted word for the word ", word ," is : ", inverted)
    return inverted


# @test1
# inversion()
# @test2
# static_inversion("Fade")