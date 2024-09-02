valid_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#opt 1.1
def den_to_bin(dn):
    if dn // 2 != 0:
        return str(den_to_bin(dn//2)) + str(dn%2)
    else:
        return str(dn%2)

#opt 1.2
def bin_to_den(bn):
    length = len(bn)-1
    
    if length == 0:
        return int(bn[0]) * 2**length

    return bin_to_den(bn[1:]) + int(bn[0]) * 2**length

#opt 2.1
def bin_to_oct(bn):
    bn = bn[::-1]
    dn = 0
    for i in range(len(bn)):
        dn += int(bn[i]) * 2**i
    
    def den_to_oct(dn):
        if dn // 8 != 0:
            return str(den_to_oct(dn//8)) + valid_digits[dn%8]
        else:
            return valid_digits[dn%8]
            
    return den_to_oct(dn)

#opt 2.2
def oct_to_bin(sym):
    def oct_to_den(sym):
        length = len(sym)-1
        if length == 0:
            for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return i * 8**length
                    
        for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return oct_to_den(sym[1:]) + i * 8**length
    
    dn = oct_to_den(sym)
    bn = ''
    while dn//2 > 0:
        bn += str(dn % 2)
        dn //= 2 
    bn += str(dn % 2)
    return bn[::-1]


#opt 2.3
def bin_to_hex(bn):
    bn = bn[::-1]
    dn = 0
    for i in range(len(bn)):
        dn += int(bn[i]) * 2**i
    
    def dec_to_hex(dn):
        if dn // 16 != 0:
            return str(dec_to_hex(dn//16)) + valid_digits[dn%16]
        else:
            return valid_digits[dn%16]
            
    return dec_to_hex(dn)

#opt 2.4
def hex_to_bin(sym):
    def hex_to_den(sym):
        length = len(sym)-1
        if length == 0:
            for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return i * 16**length
                    
        for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return hex_to_den(sym[1:]) + i * 16**length
    
    dn = hex_to_den(sym)
    bn = ''
    while dn//2 > 0:
        bn += str(dn % 2)
        dn //= 2 
    bn += str(dn % 2)
    return bn[::-1]

#opt 2.5
def oct_to_hex(sym):
    def oct_to_dec(sym):
        length = len(sym)-1
        if length == 0:
            for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return i * 8**length
                    
        for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return oct_to_dec(sym[1:]) + i * 8**length
    
    dn = oct_to_dec(sym)
    def dec_to_hex(dn):
        if dn // 16 != 0:
            return str(dec_to_hex(dn//16)) + valid_digits[dn%16]
        else:
            return valid_digits[dn%16]
            
    return dec_to_hex(dn)

#opt 2.6
def hex_to_oct(sym):
    def hex_to_dec(sym):
        length = len(sym)-1
        if length == 0:
            for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return i * 16**length
                    
        for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return hex_to_dec(sym[1:]) + i * 16**length
    
    dn = hex_to_dec(sym)
    def dec_to_oct(dn):
        if dn // 8 != 0:
            return str(dec_to_oct(dn//8)) + valid_digits[dn%8]
        else:
            return valid_digits[dn%8]
            
    return dec_to_oct(dn)

#opt 3
def any_to_any(sym, base1, base2):
    def any_to_dec(sym, base1):
        length = len(sym)-1
        if length == 0:
            for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return i * base1**length
                    
        for i in range(len(valid_digits)):
                if sym[0] == valid_digits[i]:
                    return any_to_dec(sym[1:], base1) + i * base1**length
    
    def den_to_any(dn, base2):
        if dn // base2 != 0:
            return str(den_to_any(dn//base2, base2)) + valid_digits[dn%base2]
        else:
            return valid_digits[dn%base2]
            
    return den_to_any(any_to_dec(sym, base1), base2)

#check if the input is valid
def check(base, sym):
    for i in range(len(sym)):
        if sym[i] not in valid_digits[:base]:
            return False
    return True

while True:
    print('Hello, All Mighty Universe Council. How many I help you today?')
    print('1. Convertion between denary and binary number')
    print('2. Convertion between binary, octal and hexadecimal numbers')
    print('3. Convert between any numeral systems')
    print('4. Exit')

    choice = input('Please enter your choice: ')

    if choice == '1':
        print('1. Convert denary to binary')
        print('2. Convert binary to denary')
        choice = input('Please enter your choice: ')
        if choice == '1':
            dn = input('Please enter a Denary number: ')
            if not dn.isdigit():
                print('Invalid input. Please try again.\n')
                continue
            print('The converted Binary number is: {}\n'.format(den_to_bin(int(dn))))

        elif choice == '2':
            bn = input('Please enter a Binary number: ')
            if not check(2, bn):
                print('Invalid input. Please try again.\n')
                continue
            print('The converted Denary number is: {}\n'.format(bin_to_den(bn)))

        else:
            print('Invalid choice. Please try again.\n')

    elif choice == '2':
        print('1. Convert binary to octal')
        print('2. Convert octal to binary')
        print('3. Convert binary to hexadecimal')
        print('4. Convert hexadecimal to binary')
        print('5. Convert octal to hexadecimal')
        print('6. Convert hexadecimal to octal')
        choice = input('Please enter your choice: ')
        if choice == '1':
            bn = input('Please enter a Binary number: ')
            if not check(2, bn):
                print('Invalid input. Please try again.\n')
                continue
            print('The converted Octal number is: {}\n'.format(bin_to_oct(bn)))

        elif choice == '2':
            on = input('Please enter a Octal number: ')
            if not check(8, on):
                print('Invalid input. Please try again.\n')
                continue
            print('The converted Binary number is: {}\n'.format(oct_to_bin(on)))

        elif choice == '3':
            bn = input('Please enter a Binary number: ')
            if not check(2, bn):
                print('Invalid input. Please try again.\n')
                continue
            print('The converted Hexadecimal number is: {}\n'.format(bin_to_hex(bn)))

        elif choice == '4':
            hn = input('Please enter a Hexadecimal number: ')
            if not check(16, hn):
                print('Invalid input. Please try again.\n')
                continue
            print('The converted Binary number is: {}\n'.format(hex_to_bin(hn)))

        elif choice == '5':
            on = input('Please enter a Octal number: ')
            if not check(8, on):
                print('Invalid input. Please try again.\n')
                continue
            print('The converted Hexadecimal number is: {}\n'.format(oct_to_hex(on)))

        elif choice == '6':
            hn = input('Please enter a Hexadecimal number: ')
            if not check(16, hn):
                print('Invalid input. Please try again.\n')
                continue
            print('The converted Octal number is: {}\n'.format(hex_to_oct(hn)))

        else:
            print('Invalid choice. Please try again.\n')

    elif choice == '3':
        base1 = input('Please enter the base of the number you want to convert: ')
        if not base1.isdigit():
                print('Invalid input. Please try again.\n')
                continue
        
        sym = input('Please enter the number you want to convert: ')
        if not check(int(base1), sym):
            print('Invalid input. Please try again.\n')
            continue

        base2 = input('Please enter the base you want to convert to: ')
        if not base2.isdigit() or int(base2) <= 1:
                print('Invalid input. Please try again.\n')
                continue
        
        print('The converted number is: {}\n'.format(any_to_any(sym, int(base1), int(base2))))

    elif choice == '4':
        print('Thank you for using this service. Goodbye and have a nice day in alien talks.')
        break
    
    else:
        print('Invalid choice. Please try again.\n')