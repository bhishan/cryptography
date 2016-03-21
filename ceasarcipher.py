
alphabets = "abcdefghijklmnopqrstuvwxyz"

key = 3
length = len(alphabets)
#print length
encrypted_index = 0
def ceasar_encryption(msg):
    encrypted_text = ""
    for letter in msg:
        if letter != " ":
            encrypted_index = (alphabets.index(letter) + key) % length
            encrypted_text += alphabets[encrypted_index]
        else:
            encrypted_text += " "
    return encrypted_text


def ceasar_decryption(msg):
    decrypted_text = ""
    for letter in msg:
        if letter != " ":
            decrypted_index = ((alphabets.index(letter) - key) % length)
            decrypted_text += alphabets[decrypted_index]
        else:
            decrypted_text += " "
    return decrypted_text

msg = raw_input("Enter the message to encrypt")
encrypted = ceasar_encryption(msg)
print encrypted
decrypted = ceasar_decryption(encrypted)
print decrypted
