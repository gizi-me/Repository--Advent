# day three of AOC 2024

import numpy as np

# part one: scan memory and add up all multiplications mul(0,0), mul(0,00), mul(0,000), mul(00,0), mul(000,0), mul(00,00), mul(000,00)
# mul(00,000), mul(000,000)

# open file

file = open('input_day3.txt','r')



# define list where append multiplication parts

multi = []

# go through lines and append every 12 entries, if 'mul' appears

for x in file:  # x is the line in the file
    x = x.replace(' ', '_')
    #print(x)
    # print(len(x))
    for i in range(0,len(x)-3): 
        if x[i]=='m' and x[i+1] == 'u' and x[i+2] == 'l':
            multi.append(x[i:i+12])
            print(x[i:i+12])

print('length multi', len(multi))
    
j = 0

while j < len(multi):
    element = multi[j]
    #print(element)
    if ',' and ')' in element:
        for i in range(0,12):
            if element[i] == ')':
                
                element = element[4:i]
                
                break
        multi[j] = element
        j += 1
    else:
        del multi[j]

    

print('länge jetzt', len(multi))
multi_ = []

for element in multi:
    #print('new',element)
    for i in range(0,len(element)):
        if element[i] == ',':
            # print(element)
            
            x = int(element[:i])
           
            # print(x)
            y = int(element[i+1:])
            # print(y)
            multi_.append((x*y))


#print (multi)
summe = sum(multi_)

print(summe)


    