# Trevor Waite
# Week 11 Assignment


from BowlingGame import Game

# Open textscores.txt for reading
inFile = open("testscores.txt", "r")

for line in inFile:
    line = line.strip() # take out punctuation from text file
    scoreList = line.split(",") # split the lines into a list separated by commas
    scoreList = [int(i) for i in scoreList] # makes it into a list of integers
    finalScore = scoreList.pop() # takes off the final number from each line of the textscores.txt file and makes it the final score
    g = Game()
    for roll in scoreList:
        g.roll(roll)
    score = g.score()
    print("The calculated score was {} and the score in the testscores.txt file was {}.".format(score, finalScore))
    if score == finalScore:
        print("The score was correct.")
    else:
        print("The scores do not match.  The final score is actually equal to", score)
    
        
    
inFile.close()

