import random
num_1 = random.randint(3,20)
print(num_1)
for i in range(1, num_1):
    #print(i, end=' ')
    for j in range(2,num_1):
        if num_1 % (i + j) == 0 and i < j:
            print(f'{i}{j}', end='')

