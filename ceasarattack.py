valid_words = ["hello", "world"]
alphabets = "abcdefghijklmnopqrstuvwxyz"

frequencies = [0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060, 0.065, 0.005, 0.005, 0.035, 0.030, 0.070, 0.080, 0.020, 0.002, 0.065, 0.060, 0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002]

freq = []

sai_values = []

cipher_text = raw_input("Enter the cipher text: ")

#cipher_text = cipher_text.replace(" ", "")
text_length = len(cipher_text)

unique_text = ""

for letter in cipher_text:
    
    if letter not in unique_text and letter.isalpha():
        unique_text += letter

for letter in unique_text:
    freq.append(cipher_text.count(letter)/float(text_length))


for i in range(0, 26):
    sai = 0
    for letter in unique_text:
        sai = sai + freq[unique_text.index(letter)] * frequencies[alphabets.index(letter) -i]
    sai_values.append(sai)

new_sai_values = sai_values[:]

new_sai_values.sort(reverse=True)
#print sai_values

exit_status = 0
for each_sai in new_sai_values:
    de_text = ""
    dump_key = sai_values.index(each_sai)
    for letter in cipher_text:
        if letter != " ":
            de_text += alphabets[alphabets.index(letter) - dump_key]
        else:
            de_text += letter
    #print de_text.split()
    for each_word in de_text.split():
        #print each_word
        if each_word in valid_words:
            exit_status = 1
    if exit_status == 1:
        break
print de_text
