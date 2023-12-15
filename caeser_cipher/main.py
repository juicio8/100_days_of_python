from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


def caesar(plain_text, shift_amount, shift_direction):
    end_text = ''
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    if shift_direction == 'decode':
        shift_amount *= -1
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if shift_direction == 'decode' and new_position < 0:
                new_position = len(alphabet) + new_position
            elif shift_direction == 'encode' and new_position > 25:
                new_position = new_position - position
                new_position -= 1
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the encoded result: {end_text}")


def caesar_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    signal = input(
        "Type 'yes' if you wnat to go again. Otherwise type 'no'. \n")
    if signal == 'yes':
        caesar_cipher()
    else:
        print("Goodbye!")


caesar_cipher()
