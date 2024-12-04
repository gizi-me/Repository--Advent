# day two of AOC 2024

import numpy as np

# part one: how many reports are safe? _________________________________________________________________

# load data, not equal number in eah row
with open('input_day2.txt', 'r') as file:
    data = [[int(value) for value in line.strip().split()] for line in file]    # srip and split devides each line and entries, int delivers integer


def incr_decr(list):
    dif = np.diff(list)
    if all( x < 0 for x in dif):
        return True
    elif all( x > 0 for x in dif):
        return True
    else:
        return False

data_test = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]

counter = 0

for i in range(0,len(data)):
    line = data[i]
    if incr_decr(line) == True:
        counter_int = 0
        for j in range(0,len(line)-1):
            abs_val = abs(line[j]-line[j+1])
            if abs_val == 0 or abs_val > 3:
                break
            else:
                counter_int += 1
        if counter_int == len(line)-1:
            counter += 1

print(counter)

# part two: single bad levels can get removed __________________________________________________________

def incr_decr_updated(liste):
    # calculate differences between entries
    dif = np.diff(liste)
    
    # see if they are increasing or decreasing
    if all( x < 0 for x in dif):
        for i in range(0,len(dif)):
            if dif[i] < -3:
                del liste[i+1]
                break
        return True, liste
    elif all( x > 0 for x in dif):
        for i in range(0,len(dif)):
            if dif[i] > 3:
                del liste[i+1]
                break
        return True, liste
    # if not, see if you could remove one 'bad' element
    else:
        # print(liste)
        # print(dif)
        #print('len',len(dif))
        # if bad element is found, remove it
        for i in range(0,len(dif)-2):
            #print(i)
            
            if 0 in dif:
                index_ = np.where(dif == 0)
                index_ = index_[0][0]
                if index_.size > 1:
                    print('zu viele nullen')
                else:
                    index_ = int(index_)
                    del liste[index_+1]
                    # print('case 1')
                    # print(liste)
                break
            elif dif[i] < 0 and dif[i+1] > 0 and dif[i+2] > 0:
                del liste[i+1]
                # print('case 2')
                break
            elif dif[i] > 0 and dif[i+1] < 0 and dif[i+2] < 0:
                del liste[i+1]
                # print('case 3')
                break
            elif dif[i] < 0 and dif[i+1] > 0 and dif[i+2] < 0:
                del liste[i+2]
                # print('case 4')
                break
            elif dif[i] > 0 and dif[i+1] < 0 and dif[i+2] > 0:
                del liste[i+2]
                # print('case 5')
                break
            elif dif[i+2] > 0 and dif[i+1] < 0 and dif[i] < 0:
                del liste[i+3]
                # print('case 6')
                break
            elif dif[i+2] < 0 and dif[i+1] > 0 and dif[i] > 0:
                # print('liste[i+3',liste[i+3])
                del liste[i+3]
                # print('case 7')
                # print(liste)
                break
    
        #dif =np.diff(liste)
        #print(liste)
        #print(dif)
        # calculate differences of new list, see if it is increasing or decreasing
    dif = np.diff(liste)
    
    
    if all( x < 0 for x in dif):
        return True, liste
    elif all( x > 0 for x in dif):
        return True, liste
    # if not, print out list and return False
    else:
        return False, liste

    
data_test = [[1,1,1,1,1],[2,3,4,5,9],[7,5,1],[8,9,8,10,12]]  

counter_2 = 0

for i in range(0,len(data)):
    line = data[i]
    # print(line)
    new_line = incr_decr_updated(line)
    if new_line[0] == True:
        line = new_line[1]
        #print(line)
        dif_ = abs(np.diff(line))

        if all(x > 0 and x < 4 for x in dif_):
            counter_2 += 1
            # print('true line:',line)


print(counter_2, len(data))

