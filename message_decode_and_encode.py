# This proggram take a message from user and encode it then decode it again.
def encryption():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Encrypt = ''
    Decrypt = ''
    message = input("Enter message: ").lower()
    print("Encrypt = ")
    for i in message:
        if i in alphabet:
            if i == alphabet[25]:
                print(alphabet[0], end="")
                continue
            y = alphabet.find(i) + 1
            Encrypt = alphabet[y]
            Encrypt.join(alphabet[y])
            print(Encrypt, end="")
    print("\n" + "Decrypt = ")
    for i in message:
        if i in alphabet:
            x = alphabet.find(i)
            Decrypt = alphabet[x]
            print(Decrypt, end="")


encryption()