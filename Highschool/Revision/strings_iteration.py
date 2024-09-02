#Q1:
def fooDNA(s1, s2):
    for i in range(len(s1)):
        n1 = s1[i]
        n2 = s2[i]
        if (n1 == 'A' and n2 != 'T') or \
           (n1 == 'T' and n2 != 'A') or \
           (n1 == 'G' and n2 != 'C') or \
           (n1 == 'C' and n2 != 'G'):
            return False
    return True

#Q2:
# Method 1: (Complexity: O(n^2)
# def foo15(s):
#     total = 0
    
#     for i in range(len(s)):
#         if s[i].isdigit:
#             while i < len(s):
#                 if s[i].isdigit():
#                     total += int(s[i])
#                 if total == 15:
#                     return True
#                 i += 1
#             total = 0
#     return False

#Sliding Window method (Better, less complexity): (Complexity: O(n)
def foo15(s):
    s = int(s)
    start = 0
    end = 0
    temp_sum = 0
    while end < len(s):
        if temp_sum < 15:
            temp_sum += s[end]
            end += 1
        elif temp_sum > 15:
            temp_sum -= s[start]
            start += 1
        if temp_sum == 15:
            return True
    return False

#Q3:
def fooSPR(P1, P2):
    p1_w = 0
    p2_w = 0
    for i in range(len(P1)):
        if (P1[i] == "S" and P2[i] == "R") or\
           (P1[i] == "R" and P2[i] == "P") or\
           (P1[i] == "P" and P2[i] == "S"):
               p2_w += 1
        elif (P2[i] == "S" and P1[i] == "R") or\
             (P2[i] == "R" and P1[i] == "P") or\
             (P2[i] == "P" and P1[i] == "S"):
                 p1_w += 1
        
    if p1_w > p2_w:
        return "Player 1"
    elif p2_w > p1_w:
        return "Player 2"
    return "Draw"

#Q4:
def fooSum2digits(s):
    for i in range(2, len(s)):
        total = (int(s[i-2]) + int(s[i-1]))%10
        if total != int(s[i]):
            return False
    return True

#Q5:
#Method 1 (not good):
# def encrypt(s):
#     enc_vals = ''
#     for i in s:
#         bef_val = ord(i)
#         aft_val = bef_val+3
#         if aft_val > 90:
#             aft_val = 64 + aft_val - 90
#         enc_vals += chr(aft_val)
#     return enc_vals
#Method 2 (better):
def encrypt(s, key):
    result = ''
    for d in s:
        result += chr((ord(d) - ord('A') + key) % 26 + ord('A'))
    return result

#Q6:
def decrypt(s, key):
    return encrypt(s, -key)

#7：
# def is_saw_teeth(s):
#     if s[0] < s[1]:
#         next_bigger = False
#     elif s[0] > s[1]:
#         next_bigger = True
        
#     for i in range(len(s)-1):
#         if s[i] < s[i+1]:
#             if next_bigger == False:
#                 next_bigger = True
#                 continue
            
#         elif s[i] > s[i+1]:
#             if next_bigger == True:
#                 next_bigger = False
#                 continue
#         return False
#     return True

def is_saw_teeth(a):
    for i in range(1, len(a)-1):
        if (int(a[i]) == int(a[i-1]) * int(a[i+1]) - int(a[i+1])) <= 0:
            print(a[i])
            return False
    return True

print(is_saw_teeth("1214364"))


