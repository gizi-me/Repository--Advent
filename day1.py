# day one of AOC 2024
import numpy as np

# Import der Daten
data = np.loadtxt('input_day1.txt')

# part one: total distance _____________________________________________________________________________
# Listen ordnen

left = np.sort(data[:,0])

right = np.sort(data[:,1])

# distanz berechnen

dist = np.abs(left - right)

tot_distance = np.sum(dist)

print('total distance:', tot_distance)

# part two: similarity score ____________________________________________________________________________
def compare(list1, list2):
    lenght = len(list1)
    score = 0
    for i in range(0,lenght):
        counter = 0
        for j in range(0,lenght):
            if list1[i] == list2[j]:
                counter += 1
        score += counter * list1[i]
    return score

print(compare(left,right))

        
