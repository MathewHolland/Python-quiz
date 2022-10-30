#Intro to quiz

print ("""Hello and welcome to my quiz! 

We will start by introducing ourselves""")
print ("\n")
name = input ("What is your name? ")
print("\n")
print ("nice to meat you", name, "my name is .......") #input your own name

print ("\n")

playing = input ("would you like to start? ")
if playing != "yes":
    quit()
    
score = 0    
#Quiz start ///  round one... single choice 

print ("Question 1/5")
answer = input ("what is 1 + 1? ")
if answer == "2":
    print ("Correct")
    score += 1
else:
    print ("Inccorect")
    
print ("\n")

print ("Question 2/5")
answer = input ("what is 5 + 198? ")
if answer == "203":
    print ("Corrct")
    score += 1
else:
    print ("Inccorect")
    
print ("\n")

print ("Question 3/5")
answer = input ("what is 5 x 5? ")
if answer == "25":
    print ("Correct")
    score += 1
else:
    print ("Inccorect")
    
print ("\n")

print ("Question 4/5")
answer = input ("what is 50 + 50? ")
if answer == "2500":
    print ("Correct")
    score += 1
else:
    print ("Incorrect")
    
print ("\n")

print ("Question 5/5")
answer = input ("What is PI? ")
if answer == "3.14":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect")
    
print ("\n")
    
#Start of round 2... multiple choice

print("\n")

print ("okay we will now start round 2, this round, please answer each question with 'a, b, c or d' ")

print("\n")

print ("Question 1/6")
answer = input ("What year did World War Two end? a) 1987, b) 1946, c) 1945, d) 1894 ")
if answer == "c":
    print ("That is correct!")
    score +=1
else:
    print ("That is not correct, the correct answer was 'c'")
    
print ("\n")

print ("Question 2/6")
answer = input ("What year did England win the world cup? a)1996, b) 1896, c) 1966, d) 1766 ")
if answer == "c":
    print ("Correct")
    score += 1
else:
    print ("The correct answer is 'c'")
    
print ("\n")

print ("Question 3/6")
answer = input ("What kind of food is penne? a) rice, b) pasta, c) pizza, d) vegetable ")
if answer == "b":
    print ("That is the right answer")
    score += 1
else:
    print ("That is the incorrect answer, 'b' was the right answer")

print ("\n")  

print ("Question 4/6")
answer = input ("Who discovered Penacillin? a) Ben Shillings, b) Alexander Fleming, c) Alexander Grimm, d) Ben sharp ")
if answer == "b":
    print ("You got it right!")
    score += 1
else:
    print ("That is wrong, 'b' was the correct answer")
    
print ("\n")

print ("Question 5/6")
answer = input ("What was the first film to be recognised as part of the MCU? a) Black Panther, b) The Hulk, c) Spiderman d) Iron Man ")
if answer == "d":
    print ("That is correct")
    score += 1
else:
    print ("You got it wrong, the right answer was 'd'")
    
print ("\n")

print ("Question 6/6")
answer = input ("Who was the Prime Minister of the U.K during WW2? a) Theresa May, b) David Cameron, c) Winston Chirchill, d) Margret Thatcher ")
if answer == "c":
    print ("That is correct")
    score += 1
else:
    print ("That is not correct")

print ("""
       
       \n
       
       """)
print ("So that concludes the quiz, now to see how well you did....")
print ("You got", score, "out of 11")