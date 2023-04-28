import PyEncrypt as pye

# Quick example:

encrypted = pye.encrypt("Hello World!", "Example Key")
print(f'Encrypted: {encrypted}')

decrypted = pye.decrypt(encrypted, "Example Key")
print(f'Decrypted: {decrypted}')

# Better example: (If you want to eliminate the possibility of fatal errors)

important_data = "example=save;data=that;you=don't;want=to;be=lost;"

encrypted = pye.encrypt(important_data, "Example Key")
if encrypted != 400:
    important_data = encrypted
    print(important_data)
else:
    print("Uh oh!")
    # Your own error handling here (You can try telling the user something went wrong while saving or try again in a tiny bit.)

# Example with JSON/Dict:

data = {
    "example": "save",
    "data": "that",
    "you": "don't",
    "want": "to",
    "be": "lost"
}

encrypted = pye.encryptJSON(data, "Example Key")
if encrypted != 400:
    data = encrypted
    print(data)
else:
    print("Uh oh!")

decrypted = pye.decryptJSON(data, "Example Key")
if decrypted != 400:
    data = decrypted
    print(data)
else:
    print("Uh oh!")
