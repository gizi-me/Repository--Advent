# day three of AOC 2024

import numpy as np

# part one: scan memory and add up all multiplications mul(0,0), mul(0,00), mul(0,000), mul(00,0), mul(000,0), mul(00,00), mul(000,00)
# mul(00,000), mul(000,000)

# open file

file = open('input_day3.txt','r')

# define list where append multiplication parts

# multi = []

# go through lines and append every 12 entries, if 'mul' appears

# for x in file:  # x is the line in the file
#     x = x.replace(' ', '_')
#     #print(x)
#     # print(len(x))
#     for i in range(0,len(x)-3): 
#         if x[i:i+3] == 'mul':
#             multi.append(x[i:i+12])
#             #print(x[i:i+12])

# print('length multi', len(multi))
    
# j = 0

# while j < len(multi):
#     element = multi[j]
#     #print(element)
#     if ',' and ')' in element:
#         for i in range(0,12):
#             if element[i] == ')':
                
#                 element = element[4:i]
                
#                 break
#         multi[j] = element
#         j += 1
#     else:
#         del multi[j]

    

# print('länge jetzt', len(multi))
# multi_ = []

# for element in multi:
#     #print('new',element)
#     for i in range(0,len(element)):
#         if element[i] == ',':
#             # print(element)
            
#             x = int(element[:i])
           
#             # print(x)
#             y = int(element[i+1:])
#             # print(y)
#             multi_.append((x*y))


# #print (multi)
# summe = sum(multi_)

# print(summe)

# part two: do() enables, dont() stops__________________________________________________________________________________________

test = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

# define function that checks if a valid mul(,) part is there and collect the 'do()'s and 'don't()'s along the way
# also through away the mul and brackets. The result is a list with do() and don't() and the numbers that should be multiplied between them
# order of appearance will be conserved

def mul(file):
    # list for commands and numbers
    multi_ = []
    # go through the lines of the file
    for x in file:
        # search for valid commands
        for i in range(0,len(x)-3): 
    
            if x[i:i+4]=='mul(':
                element = x[i:i+12]
                if ',' and '(' and ')' in element:
                    j = 4
                    while j <= 12:
                        if element[j] == ')':
                            multi_.append(element[4:j])
                            j = 13
                        else:
                            j += 1

            elif x[i:i+4] == 'do()':
                multi_.append('do()')

            elif x[i:i+7] == "don't()":
                multi_.append("don't()")
    # return the list of valid commands and numbers            
    return multi_

def do_dont(file):
    data = mul(file)
    multi_2 = []

    i = 0

    while i < len(data):
       
        if data[i] == "don't()":
            
            i += 1
            while i < len(data) and data[i] != 'do()':
                i += 1
            if  i < len(data) and data[i] == 'do()':
                
                i += 1
        else:
            
            if ',' in data[i]:
                x, y = map(int, data[i].split(','))  
                multi_2.append(x * y)
            i += 1
    summe = sum(multi_2)
    return summe


summe_part2 = do_dont('input_day3.txt')
print('part two:', summe_part2)

# for some reason the script does not work right now