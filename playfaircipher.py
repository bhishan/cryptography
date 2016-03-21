from collections import OrderedDict

alphabets = "abcdefghiklmnopqrstuvwxyz"  #english alphabets excluding j, since we have key_square matrix of size 5*5, we remove j

text_to_encrypt = ""

key_square = [[0 for x in range(5)]for x in range(5)] #initializing the 5*5 matrix with 0's 

key = raw_input("Enter the key:: ")  #Taking key for encryption/decryption 

plain_text = raw_input("Enter the plain text:: ") #Taking plain text input from console.

last_elem = plain_text[-1]

key_plain_con = key.replace(" ", "") + alphabets

to_keep = "".join(OrderedDict.fromkeys(key_plain_con))

count = 0
for i in range(5):
    for j in range(5):
        key_square[i][j] = to_keep[count]
        count += 1

length_of_pt = len(plain_text)

for i in range(length_of_pt-1):
    if plain_text[i] == plain_text[i+1]:
        text_to_encrypt += plain_text[i] + "x"
    else:
        text_to_encrypt += plain_text[i]

text_to_encrypt += last_elem

if len(text_to_encrypt) % 2 != 0:
    text_to_encrypt += "x"

print "Text to encrypt: ", text_to_encrypt

encrypted_text = ""

def index_in_2d(elem):
    for i, each_list in enumerate(key_square):
        try:
            return (i, each_list.index(elem))
        except ValueError:
            continue

for i in range(0, len(text_to_encrypt)-1, 2):
    char1x, char1y = index_in_2d(text_to_encrypt[i])
    char2x, char2y = index_in_2d(text_to_encrypt[i+1])
    if char1x == char2x:
        encrypted_text += key_square[char1x][(char1y + 1) % 5] + key_square[char2x][(char2y +1) % 5]
    elif char1y == char2y:
        encrypted_text += key_square[(char1x+1) % 5][char1y] + key_square[(char2x+1) % 5][char2y]
    else:
        encrypted_text += key_square[char1x][char2y] + key_square[char2x][char1y]

print "Encrypted text: ", encrypted_text

decrypted_text = ""

for i in range(0, len(encrypted_text)-1, 2):
    char1x, char1y = index_in_2d(encrypted_text[i])
    char2x, char2y = index_in_2d(encrypted_text[i+1])
    if char1x == char2x:
        decrypted_text += key_square[char1x][(char1y - 1) % 5] + key_square[char2x][(char2y -1) % 5]
    elif char1y == char2y:
        decrypted_text += key_square[(char1x-1) % 5][char1y] + key_square[(char2x-1) % 5][char2y]
    else:
        decrypted_text += key_square[char1x][char2y] + key_square[char2x][char1y]


print "Decrypted text: ", decrypted_text
