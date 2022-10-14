from cipher_art import logo

def caesar(plain_text, shift_amount, direc_type):
    cipher_text = ""
    if direc_type == "encode":
        for letter in plain_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                if new_position > 25:
                    new_position %= 26
                new_letter = alphabet[new_position]
                cipher_text += new_letter

        print(f"The encoded text is {cipher_text}")
    
    elif direc_type == "decode":
        for letter in plain_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                if abs(new_position) > 25 :
                    new_position %= 26
                new_letter = alphabet[new_position]
                cipher_text += new_letter
                if letter not in plain_text:
                    cipher_text += letter
        print(f"The decoded text is {cipher_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    re_run = input("type yes to start over, otherwise type no to end ")
    if re_run == "no":
        should_continue = False
        print("messages deciphered")



