valid_digits = '0123456789ABCDEF'

#decimal to binary
def dec_to_bin_rec(dn):
    if dn // 2 !=0:
        return str(dec_to_bin_rec(dn//2)) + valid_digits[dn%2]
    
    return valid_digits[dn%2]

def dec_to_bin_itr(dn):
    bn = ''
    while dn//2 > 0:
        bn += valid_digits[dn % 2]
        dn //= 2
    bn += valid_digits[dn % 2]
    return bn[::-1]

#decimal to hexadecimal
def dec_to_hex_rec(dn):
    if dn // 16 != 0:
        return str(dec_to_hex_rec(dn//16)) + valid_digits[dn%16]
    
    return valid_digits[dn%16]

def dec_to_hex_itr(dn):
    hn = ''
    while dn//16 > 0:
        hn += valid_digits[dn % 16]
        dn //= 16
    hn += valid_digits[dn % 16]
    return hn[::-1]

#binary to decimal
def bin_to_dec_rec(bn):
    length = len(bn)-1
    if length == 0:
        return int(bn[0]) * 2**length
    
    return bin_to_dec_rec(bn[1:]) + int(bn[0]) * 2**length

def bin_to_dec_itr(bn):
    bn = bn[::-1]
    dn = 0
    for i in range(len(bn)):
        dn += int(bn[i]) * 2**i
    return dn

#octal to decimal
def oct_to_dec_rec(on):
    length = len(on)-1
    if length == 0:
        return int(on[0]) * 8**length
    
    return oct_to_dec_rec(on[1:]) + int(on[0]) * 8**length

def oct_to_dec_itr(on):
    on = on[::-1]
    dn = 0
    for i in range(len(on)):
        dn += int(on[i]) * 8**i
    return dn

#hexadecimal to decimal
def hex_to_dec_rec(hn):
    length = len(hn)-1
    if length == 0:
        for i in range(len(valid_digits)):
            if hn[0] == valid_digits[i]:
                return i * 16**length
    for i in range(len(valid_digits)):
        if hn[0] == valid_digits[i]:
            return hex_to_dec_rec(hn[1:]) + i * 16**length
        
def hex_to_dec_itr(hn):
    hn = hn[::-1]
    dn = 0
    for i in range(len(hn)):
        for j in range(len(valid_digits)):
            if hn[i] == valid_digits[j]:
                dn += j * 16**i
    return dn

#hexadecimal to binary
def hex_to_bin(hn):
    return dec_to_bin_itr(hex_to_dec_rec(hn))

print(dec_to_bin_rec(10))
print(dec_to_bin_itr(10))
print(dec_to_hex_rec(10))
print(dec_to_hex_itr(10))
print(bin_to_dec_rec('1010'))
print(bin_to_dec_itr('1010'))
print(oct_to_dec_rec('12'))
print(oct_to_dec_itr('12'))
print(hex_to_dec_rec('A'))
print(hex_to_dec_itr('A'))
print(hex_to_bin('A'))


