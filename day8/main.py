alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_len = len(alphabet)


def ceaser_alg(text: str, shift: int, direction: str):
    shift_value = shift
    ceaser_word = ""
    if direction == "decode":
        shift_value *= -1
    for letter in text:
        if letter not in alphabet:
            ceaser_word += letter
            continue
        index = alphabet.index(letter)
        if (index - shift) < 0 and direction == "decode":
            new_index = (index - shift) * -1
            ceaser_word += alphabet[alphabet_len - new_index]
        elif index + shift > (alphabet_len - 1) and direction == "encode":
            new_index = shift - ((alphabet_len - 1) - index)
            ceaser_word += alphabet[new_index - 1]
        else:
            ceaser_word += alphabet[index + shift_value]

    print(f"The {direction}d text is {ceaser_word}")


while True:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            if shift > alphabet_len:
                raise ValueError(
                    f"Shift value cannot be greater than {alphabet_len}")
            break
        except ValueError as e:
            print(e)
            print("Please try again.")

    ceaser_alg(text, shift, direction)
    answer = input(
        "Type 'yes' if you want to go agian. otherwise type 'no'").lower()
    if answer == "no":
        print("Good Bye!")
        break
