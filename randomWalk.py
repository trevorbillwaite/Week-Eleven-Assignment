# Basic Structure for a Random Walk simulation
# Dan Neumann
'''

You flip a coin.
If it comes up heads, you take a step forward;
tails means to take a step backward.
Repeat this n times.
Calculate distance from start

Repeat this process a large number of times.
Calculate and print the average for a given value of n
Start with 100 to 1000, step 10
'''

import random

# Define ranges here
startRange = 0
endRange = 100
stepRange = 1



def main():
    printHeader()
    for n in range(startRange,endRange,stepRange):
        averageDistance = getRandomWalk(n)
        print("For {} steps, the average distance is: {}".format(n,averageDistance))


def printHeader():
    print("A coin is flipped a random number of times.  When the result is heads, you take a step forward. When the result is tails, you take a step backwards.")

def getRandomWalk(steps):
    distance = 0
    for i in range(steps):
        flip = random.randint(1,2)
        # heads = 1
        if flip == 1:
            distance += 1
        # tails = 2
        else:
            distance -= 1
    # Calculate a random walk of given steps
    # If the result of the flip is heads, step forward
    # If the result of the flip is tails, step backward
    
    return distance # replace with actual average

if __name__ == "__main__":
    main()