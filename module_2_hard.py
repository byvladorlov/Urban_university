import random
#num_1 = random.randint(3,20)
num_1 = 9
print(num_1)
for i in range(1, num_1):
    #print(i, end=' ')
    for j in range(2,num_1):
        if num_1 % (i + j) == 0:
            print(i,j, end=' ')
            continue
        if i == j:
            break