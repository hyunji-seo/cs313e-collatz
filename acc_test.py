# 1000 acceptance tests
import random
# generate random number pairs
for n in range(1000):
    i = random.randint(1, 1000)
    j = random.randint(1, 1000)
    if i != j:
    	print (str(i) + " " + str(j))

