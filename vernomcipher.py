#sample plain text : hello
#sample key : axhjb

def make_chunks(text, text_length, key_length):
    for i in range(0, text_length, key_length):
        yield text[i : i + key_length]


def encryptdecrypt(cipher_generator):
    final_text = ""
    for item in cipher_generator:
        for i in range(0, len(item)):
            final_text += alphabets[alphabets.index(key[i]) ^ alphabets.index(item[i])]
    return final_text

alphabets = "abcdefghijklmnopqrstuvwxyz"

plain_text = raw_input("Enter the plain text: ")

key = raw_input("Enter the key: ")

plain_text = plain_text.replace(" ", "")

p_generator = make_chunks(plain_text, len(plain_text), len(key))

cipher_text = encryptdecrypt(p_generator)

print "The cipher text is : ", cipher_text

c_generator = make_chunks(cipher_text, len(cipher_text), len(key))

decrypted_text = encryptdecrypt(c_generator)

print "The decrypted text is : ", decrypted_text

