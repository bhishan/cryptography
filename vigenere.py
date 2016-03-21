alphabets = "abcdefghijklmnopqrstuvwxyz"

text = raw_input("Enter the text : ")

text = text.replace(" ", "")

text_length = len(text)

key = raw_input("Enter the key for encryption/decryption : ")

key_length = len(key)

cipher_text = ""

def make_chunks(text, text_length, key_length):
    for i in range(0, text_length, key_length):
        #print text[i : i + key_length]
        yield text[i : i + key_length]

mygenerator = make_chunks(text, text_length, key_length)

for item in mygenerator:
    print item
    for i in range(0, len(item)):
        print item[i], key[i]
        #cipher_index =  alphabets.index(key[i]) + alphabets.index(item[i])
        cipher_index =  alphabets.index(item[i]) - alphabets.index(key[i])
        cipher_text += alphabets[cipher_index % 26]
        print cipher_text



    
