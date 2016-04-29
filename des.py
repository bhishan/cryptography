def bit_rearrangement(table, lookup_string):
    rearranged_string = ''
    rows, cols = len(table), len(table[0])
    for i in range(rows):
        for j in range(cols):
            lookup_index = table[i][j]
            rearranged_string += lookup_string[lookup_index - 1]
    return rearranged_string

def shift_left(initial_key, number):
    temp = initial_key[number:]
    to_append = initial_key[:number]
    return temp +to_append

def message_encoding(ln, rn, key):
    temp_ln = rn[:]
    e_rn = bit_rearrangement(e_bit_selection_table, rn)
    f_value = int(e_rn, 2) ^ int(key, 2)
    f_value = format(f_value, '048b')
    f = six_to_four_bits(f_value)
    final_f = bit_rearrangement(p, f)
    rn = int(ln, 2) ^ int(final_f, 2)
    rn = format(rn, '032b')
    return [temp_ln, rn]    

def six_to_four_bits(msg):
    final_msg = ''
    s_count = 0
    for i in range(0, len(msg), 6):
        current_chunk = msg[i:i+6]  
        row_str = current_chunk[0] + current_chunk[-1]
        row = int(row_str, 2)
        col_str = current_chunk[1:5]
        col = int(col_str, 2)
        table = s_table[s_count]
        num = table[row][col]
        final_msg += format(num, '04b')
        s_count += 1
    return final_msg

ip_inverse = [[40,8,48,16,56,24,64,32], [39,7,47,15,55,23,63,31],  [38,6,46,14,54,22,62,30], [37,5,45,13,53,21,61,29], [36,4,44,12,52,20,60,28], [35,3,43,11,51,19,59,27], [34,2,42,10,50,18,58,26], [33,1,41,9,49,17,57,25]]

p = [[16,7,20,21], [29,12,28,17], [1,15,23,26], [5,18,31,10], [2,8,24,14], [32,27,3,9], [19,13,30,6], [22,11,4,25]]

pc1 = [[57,49, 41, 33, 25, 17, 9], [1, 58, 50, 42, 34, 26, 18], [10, 2, 59, 51, 43, 35, 27], [19, 11, 3, 60, 52, 44, 36], [63, 55, 47, 39, 31, 23, 15], [7, 62, 54, 46, 38, 30, 22], [14, 6, 61, 53, 45, 37, 29], [21, 13, 5, 28, 20, 12, 4]]


pc2 = [[14,17,11,24,1,5], [3,28,15,6,21,10], [23,19,12,4,26,8], [16,7,27,20,13,2], [41,52,31,37,47,55], [30,40,51,45,33,48], [44,49,39,56,34,53], [46,42,50,36,29,32]]
left_shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

ip_table = [[58,50,42,34,26,18,10,2], [60,52,44,36,28,20,12,4], [62,54,46,38,30,22,14,6], [64,56,48,40,32,24,16,8], [57,49,41,33,25,17,9,1], [59,51,43,35,27,19,11,3], [61,53,45,37,29,21,13,5], [63,55,47,39,31,23,15,7]]

e_bit_selection_table = [[32,1,2,3,4,5], [4,5,6,7,8,9], [8,9,10,11,12,13], [12,13,14,15,16,17], [16,17,18,19,20,21], [20,21,22,23,24,25], [24,25,26,27,28,29], [28,29,30,31,32,1]]

s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7], [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8], [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0], [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10], [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5], [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15], [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

s3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8], [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1], [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7], [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

s4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15], [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9], [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4], [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

s5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9], [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6], [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14], [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

s6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11], [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8], [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6], [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

s7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1], [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6], [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

s8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7], [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2], [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8], [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

s_table = [s1,s2,s3,s4,s5,s6,s7,s8]
C = []
D = []
K = []
k_plus = ""

key = input("Enter key: ")

bin_key = bin(key)

bin_key = bin_key.replace('0b', '')

message = input("Enter the message: ")

bin_message = bin(message)

bin_message = bin_message.replace('0b', '')
append_z = ''
if(len(bin_message) < 64):
    for i in range(64 - len(bin_message)):
        append_z += "0"

bin_message = append_z + bin_message

ip_message = ''

message_l0, message_r0 = ip_message[:len(ip_message)/2], ip_message[len(ip_message)/2:]

append_bin = ""
if(len(bin_key) < 64):
    for i in range(64 - len(bin_key)):
        append_bin += "0"
bin_key = append_bin + bin_key
k_plus = bit_rearrangement(pc1, bin_key)

left_key, right_key = k_plus[:len(k_plus)/2], k_plus[len(k_plus)/2:]

for i in range(16):
    left_key = shift_left(left_key, left_shifts[i])
    right_key = shift_left(right_key, left_shifts[i])
    C.append(left_key)
    D.append(right_key)


for i in range(16):
    temp_key = C[i] + D[i]
    final_key = bit_rearrangement(pc2, temp_key)
    K.append(final_key)

ip_message = bit_rearrangement(ip_table, bin_message)

ln, rn = ip_message[:len(ip_message)/2] , ip_message[len(ip_message)/2:]
  
for i in range(16):
    ln, rn = message_encoding(ln, rn, K[i])

rnln = rn+ln 

encrypted_msg = bit_rearrangement(ip_inverse, rnln)

encrypted_bin_to_int = int(encrypted_msg, 2)
encrypted_msg_hex = format(encrypted_bin_to_int, '016x')
print "Encrypted Hexadecimal format: ", encrypted_msg_hex
    
