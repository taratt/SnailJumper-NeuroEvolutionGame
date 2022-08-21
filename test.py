import random
import numpy as np
for i in range(30):
    x = np.random.normal()
    # print(x)

x = [1 ,7,4,2,9,1,2,3]

weights = {1: np.array([1,2,3]), 2: np.array([2,4,5])}
weights2 = {1: np.array([4,2,7]), 2: np.array([0,4,1])}

weights3 = {}
for i in weights.keys():
    weights3[i] = weights2[i] + weights[i]
# print(weights3)
# print(x[-1])
# print(np.array((i+1) for i in range(3)))
x = [10, 40, 20 ,30]
fitnesses = np.array([xs for xs in x])
fitnesses = fitnesses/sum(fitnesses)
for i in range(len(fitnesses)-1):
            fitnesses[i+1] += fitnesses[i]
rand = random.random()
c = 0
for j in range(len(fitnesses)):
                if rand < fitnesses[j]:
                    c = j
                    break
print(c,rand)


print(fitnesses)