print("welcome to Evans video game quiz")
print("There are 7 questions good luck on the quiz")
def end_game(ans):
    if ans == "quit":
        print('Game over')
        # exit
        quit()
score = 0
correct_answer = True
def correct(score):
    print("correct") 
    score = score + 1

def incorrect(score):
    print ("incorrect") 
    score = 0
    print(score)
    #score_total = 7
    
question1 = input("what is the name of the red ghost in pacman?")
awnser1 = "blinky"
end_game(question1)
if question1 == awnser1:
    correct(score)
else:
    incorrect(score)

question2 = input("what currency does Mario collect in Super Mario Bros?")
awnser2 = ("coins")
end_game(question2)

if question2 == awnser2:
    print("correct")
else:
    print("incorrect")

question3 = input("what is link's favorite horse?")
awnser3 = ("epona")
end_game(question3)

if question3.lower().strip() == awnser3:
    print("correct")
else:
    print("incorrect")

question4 = input("what color is spyro?")
answer4 = "purple"
end_game(question4)

if question4 == answer4:
    print("correct")
else:
    end_game(question4)
    print("incorrect")

question5 = input("what is the name of sonics sidekick?")
answer5 = ("tails")
end_game(question5)

if question5 == answer5:
    print("correct")
else:
    print("incorrect")

question6 = input("what was the nes called in japan?")
answer6 = ("the famicom")
end_game(question6)

if question6 == answer6:
    print("correct")
else:
    print("incorrect")

question7 = input("who is the father of video games")
answer7 = ("ralph baer")
end_game(question7)

if question7 == answer7:
    print("correct")
else:
    print("incorrect")
    print("thanks for playing")
    
    
    
