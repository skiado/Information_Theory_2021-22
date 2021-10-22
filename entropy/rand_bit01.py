import random

prob = input('prob = ')
f = open('rand_bit_'+prob+'.txt','w')
prob = float(prob)
for i in range(1000):
    a = random.random()
    if a > prob:
        f.write('0')
    else:
        f.write('1')
f.close()
