def first_word(text: str) -> str:
    res = ''
    first_check = False
    not_a_letter = False
    for letter in text:
        if letter.isalpha() or letter == "\'":
            not_a_letter = False
            res += letter
            if not first_check:
                first_check = True
        else:
            not_a_letter = True
        if (first_check and not_a_letter):
            return res
    return res


if __name__ == '__main__':
    print("Example:")
    print(first_word("... and so on ..."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
