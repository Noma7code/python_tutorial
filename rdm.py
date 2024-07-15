import numpy as np
print(np.random.rand())#producing random values
np.random.seed(123) # ensures reproducibility
print(np.random.rand())#rand: genrate random float between 0 and 1
coin=np.random.randint(0,2)#randint :generate random integers
print(coin)
if coin==0:
    print("heads")
else:
    pritn("tails")

# Starting step
step = 50

# Roll the dice
dice=np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step+1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
#random walk
np.random.seed(456)
outcomes=[]
for x in range(10):
    coin=np.random.randint(0,2)

    if x==0:
     outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)

np.random.seed(123)
tail=[0]
for x in range(10):
    coin=np.random.randint(0,2)
    tail.append(tail[x]+coin)
print(tail)


# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)
