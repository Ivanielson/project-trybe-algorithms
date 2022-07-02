def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False
    if high_index < 0:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


if __name__ == "__main__":
    word = "I"
    print(is_palindrome_recursive(word, 0, len(word)-1))