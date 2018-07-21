def ceaser(message, key):
    encrypted_message = ''

    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    for i in message:

        if i not in alphabet:
            encrypted_message += i
        else:
            encrypted_message += alphabet[
                (alphabet.index(i)+shift) % len(alphabet)]

    print("The encrypted message is:", encrypted_message)

while True:
    try:
        shift = int(input('Shift value: '))
        break
    except ValueError:
        print('Your shift value must be an integer.')
text = input("Your message: ").lower()
ceaser(text, shift)
