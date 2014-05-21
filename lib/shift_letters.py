def shift_n_letters(letter, n):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    x = alphabet.index(letter) + 1
    if x + n <= len(alphabet):
        return alphabet[x + n - 1]
    else:
        return alphabet[((x + n) % 26) - 1]


def shift_text(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    new_string = []
    for e in text:
        if e not in alphabet:
            new_string.append(e)
        if e in alphabet:
            new_string.append(shift_n_letters(e, 13))
    return ''.join(new_string)

