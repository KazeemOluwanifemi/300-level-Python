running = 1

def encode_message(message, shift):
        encoded = " "
        if message is None:
            print("Invalid entry, please enter a message: ")
            return 1
        else:
            for char in message:
                if char.isalpha():
                    if char.isupper():
                        offset = ord("A")
                        shifted = ((ord(char) - offset + shift) % 26) + offset
                        encoded += chr(shifted)
                    elif char.islower():
                        offset = ord("a")
                        shifted = ((ord(char) - offset + shift) % 26) + offset
                        encoded += chr(shifted)
                else:
                    encoded += char        
            return encoded

while(running):
    print("Welcome to Caeser Cipher!")

    message = input("What message would you like to encode? ")
    shift = int(input("How many shift steps? "))

    print(encode_message(message, shift))
    