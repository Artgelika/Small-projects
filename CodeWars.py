# There are my solutions of CodeWars' problems.
# It also contains interesting other people's suggestions
# from this site (all of those are marked).
# There is indicated specific level of exercises.
# 1kyu is the hardest, 8kyu is the weakest.




###### 6kyu
# Weird IPv6 hex string parsing_______________
# IN - "ACDD-0101-9ABC-AAAA-FFFF-2222-FBDE-ACCC"
# OUT - "48242406085346"
def parse_IPv6(iPv6):
    tik = iPv6[4]
    list_split = iPv6.split(tik)
    list_of_list = []
    for element in list_split:
        temp = []
        for el in element:
            temp.append(int(el, 16))
        list_of_list.extend([temp])

    list_of_list = [sum(elem) for elem in list_of_list]
    sum_ = ""
    for el in list_of_list:
        sum_ += str(el)
    return sum_

# What century it is__________________________
def what_century(year):
    st = ""
    if year[0] == '1':
        st = 'th'
    elif year[1] == '0':
        st = "st"
    elif year[1] == '1':
        st = "nd"
    elif year[1] == '2':
        st = "rd"
    else: st = "th"
        
    if year[2:] == '00':
        return str( int(year[:2])) + "th"
        
    return str( int(year[:2]) + 1) + st
#_____________________________________________

###### 7kyu
# Right in the Centre_________________________
# is 'abc' in the centre of string?
def is_in_middle(sequence):
    prefix = (len(sequence) - 3)//2
    new_seq = sequence[prefix:-prefix-1]
    return "ab" in new_seq 

# Validate PIN________________________________
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6 ) and pin.isdigit()

# Another solution
def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()
#______________________________________________

# Simple eviternity numbers____________________
# contains only digits 8, 5 and 3, and
# the count of the digit 8 >= count of digit 5 >= count of digit 3.
# def solve(a,b):
    # contain only 8, 5, 3
    # list_of_numbers = [num for num in range(a,b) if 8 in num or 5 or 3 in num]
    # outl = []
    # for el in range(a,b):
    #     if ('8' in str(el)) or ('8' and '5' in str(el)) or ('8' and '5' and '3' in str(el)):
    #         # if ('0' and '1' and '2' and '4' and '6' and '9') not in str(el):
    #         outl.append(el)
    # return outl

# rozwiazanie nr 2 (CodeWars)
# eviternity = [int(n) for n in map(str, range(10 ** 6))
#               if set(n) <= set('358') and n.count('3') <= n.count('5') <= n.count('8')]
# solve = lambda a, b, f=__import__('bisect').bisect_left: f(eviternity, b) - f(eviternity, a)

# rozwiazanie nr 3
u = [8, 58, 85, 88, 358, 385, 538, 583, 588, 835, 853, 858, 885, 888, 3588, 3858, 3885, 5388, 5588, 5838, 5858, 5883, 5885, 5888, 8358, 8385, 8538, 8558, 8583, 8585, 8588, 8835, 8853, 8855, 8858, 8885, 8888, 35588, 35858, 35885, 35888, 38558, 38585, 38588, 38855, 38858, 38885, 53588, 53858, 53885, 53888, 55388, 55838, 55883, 55888, 58358, 58385, 58388, 58538, 58583, 58588, 58835, 58838, 58853, 58858, 58883, 58885, 58888, 83558, 83585, 83588, 83855, 83858, 83885, 85358, 85385, 85388, 85538, 85583, 85588, 85835, 85838, 85853, 85858, 85883, 85885, 85888, 88355, 88358, 88385, 88535, 88538, 88553, 88558, 88583, 88585, 88588, 88835, 88853, 88855, 88858, 88885, 88888, 335588, 335858, 335885, 338558, 338585, 338855, 353588, 353858, 353885, 355388, 355838, 355883, 355888, 358358, 358385, 358538, 358583, 358588, 358835, 358853, 358858, 358885, 358888, 383558, 383585, 383855, 385358, 385385, 385538, 385583, 385588, 385835, 385853, 385858, 385885, 385888, 388355, 388535, 388553, 388558, 388585, 388588, 388855, 388858, 388885]

def solve(a, b):
    return sum(a <= x < b for x in u)
# print(solve(0,100))
#______________________________________________

# Say Me Please Operations_____________________
def sayMeOperations(stringNumbers):
    str_ = ""
    list_numbers = [int(x) for x in stringNumbers.split()]
    for i in range(len(list_numbers)-2):
        if list_numbers[i] + list_numbers[i+1] == list_numbers[i+2]:
            str_ += "addition"
        elif list_numbers[i] - list_numbers[i+1] == list_numbers[i+2]:
            str_ += "subtraction"
        elif list_numbers[i] * list_numbers[i+1] == list_numbers[i+2]:
            str_ += "multiplication"
        else:
            str_ += "division"
        if i != (len(list_numbers)-3):
             str_ += ", "
    return str_

# Somebody's interesting solution (from CodeWars)
# def sayMeOperations(stringNumbers):
#     nums = [int(i) for i in stringNumbers.split()]

#     return ', '.join({
#         a * b: 'multiplication',
#         a - b: 'subtraction',        
#         a + b: 'addition',        
#     }.get(c, 'division') for a,b,c in zip(nums, nums[1:], nums[2:]))
# print(sayMeOperations('1 2 3 5 8'))
#______________________________________________

# Simple consecutive pairs_____________________
def pairs(ar):
    coun = 0
    # creating list of tuples (with pairs)
    for i in range(0, len(ar)-1, 2):
        tup = (ar[i], ar[i+1])
        print(tup)
        if abs(tup[1] - tup[0]) == 1:
            coun += 1
    return coun
    
# print(pairs([1,2,5,8,-4,-3,7,6,5]))

# GCD sum______________________________________
def solve(s,g):
    num2 = s-g
    if num2 % g == 0:
        return g, num2
    else:
        return -1

def solve2(s,g):
    return (g, s-g) if (s-g) % g == 0 else -1
# print(solve(12,4))

# # solution from CodeWars
# def solve(s,g):
#     return -1 if s % g else (g, s - g)
#______________________________________________

#Reverse Letter________________________________
def reverse_letter(string):
    str_ = ""
    for letter in string:
        if letter.isalpha():
            str_ += letter
    return str_[::-1]
    
def reverse_letter2(s):  #CodeWars
  return ''.join([i for i in s if i.isalpha()])[::-1]    
#______________________________________________
