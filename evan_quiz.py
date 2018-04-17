print("welcome to Evans quiz ")
print("There are 7 questions good luck on the quiz")
def end_game(ans):
    if ans == "quit":
        print('Game over')
        # exit
        quit()
#question1 = super easy
question1 = input("what color is an apple?")
awnser1 = ("red")
end_game(question1)
if question1 == awnser1:
    print("Correct!!!")
else:
    print ("incorrect")

question2 = input("what currency does Mario collect in Super Mario Bros?")
awnser2 = ("coins")
end_game(question2)

if question2 == awnser2:
    print("Correct!!!")
else:
    print("incorrect!")

question3 = input("what is link's favorite horse?")
awnser3 = ("epona")
end_game(question3)

if question3.lower().strip() == awnser3:
    print("Correct!!!")
else:
    print("incorrect!")

question4 = input("what color is spyro?")
answer4 = "purple"
end_game(question4)

if question4 == answer4:
    print("Correct!!!")
else:
    end_game(question4)
    print("incorrect!")

question5 = input("what is sonics archnemesis?")
answer5 = ("dr eggman")
end_game(question5)

if question5 == answer5:
    print("Correct!!!")
else:
    print("incorrect!")

question6 = input("how does kirby copy his enemies moves")
answer6 = ("he inhales them")
end_game(question6)

if question6 == answer6:
    print("Correct!!!")
else:
    print("incorrect!")

question7 = input("who is the father of video games")
answer7 = ("ralph baer")
end_game(question7)

if question7 == answer7:
    print("Correct!!!")
else:
    print("incorrect!")
