#insertation sort
numbers = [4,2,6,8,9,3,5,7,8]

#insertation sort
#j is index number 
for i in range (0,len(numbers)):
    minElement = 1000000
    minlocation = -1
    for j in range(i,len(numbers)):
        if minElement>numbers[j]:
            minElement= numbers[j]
            minLocation = j
            numbers[i],numbers[j] = numbers[j],numbers[i]
print(numbers)


#time complexity = (o)n^2
#(o)n^2 = worst case
#worst case = list is in reverse order
 
#(o)n = average case 
#average case = mixed up order 

#best case (o)1
#best case = already sorted 
