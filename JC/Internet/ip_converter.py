"""
Write, in Python code, a function ipv6_hex2dec(ipv6) to convert an IPv6
address to decimal. [7]

Note: You may not use the built-in function which converts a hexadecimal string
to an integer.

Sample execution:
>> print (ipv6_hex2dec("0000:0000:0000:0000:0000:0000:0000:000f"))
0:0:0:0:0:0:0:15

>> print (ipv6_hex2dec ("fdb1:344c:33da:0000:0040:0000:0000:0000"))
64945:13388:13274:0:64:0:0:0

>> print (ipv6_hex2dec("2001:0db8:0000:0000:0000:ff00:0042:8329"))
8193:3512:0:0:0:65280:66:33577
"""

valid_digits = "0123456789abcdef"

def ipv6_hex2dec(ipv6):
    dec = ''
    ipv6_spilt = ipv6.split(":") #Storing each part in a list

    for elem in ipv6_spilt: #iterating through each part
        val = hex_to_dec(elem) #converting from hexidecimal to decimal
        dec += f"{val}:" #Adding to the initialised string 
    
    return dec[:-1] #Last element will be : which is not needed

def hex_to_dec(hn):
    hn = hn[::-1]
    dn = 0
    for i in range(len(hn)):
        for j in range(len(valid_digits)):
            if hn[i] == valid_digits[j]:
                dn += j * 16**i
    return dn
        

print (ipv6_hex2dec("0000:0000:0000:0000:0000:0000:0000:000f"))
#0:0:0:0:0:0:0:15
print (ipv6_hex2dec ("fdb1:344c:33da:0000:0040:0000:0000:0000"))
#64945:13388:13274:0:64:0:0:0
print (ipv6_hex2dec("2001:0db8:0000:0000:0000:ff00:0042:8329"))
#8193:3512:0:0:0:65280:66:33577

"""
Write, in Python code, a function expand_ipv6(short_ipv6) to convert
an abbreviated IPv6 addressto its original form. [7]

Sample execution:
>>print (expand_ipv6 ("2001:db8::ff00:42:8329"))
2001:0db8:0000:0000:0000:ff00:0042:8329

>> print (expand_ipv6 ("::f"))
0000:0000:0000:0000:0000:0000:0000:000f

>> print (expand_ipv6 ("fdb1:344c:33da:0:40::"))
fbd1:344c:33da:0000:0040:0000:0000:0000
"""

def expand_ipv6(short_ipv6):
    full = ""
    short_ipv6_split = short_ipv6.split(":")
    print(short_ipv6_split)
    for elem in short_ipv6_split:
        while len(elem) < 4:
            elem = "0" + elem
        full += f"{elem}:"
    return full[:-1]



print(expand_ipv6 ("2001:db8::ff00:42:8329"))
#2001:0db8:0000:0000:0000:ff00:0042:8329
print(expand_ipv6 ("::f"))
#0000:0000:0000:0000:0000:0000:0000:000f
print(expand_ipv6 ("fdb1:344c:33da:0:40::"))
#fbd1:344c:33da:0000:0040:0000:0000:0000
