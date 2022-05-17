import turtle
import random
s = turtle.getscreen()
p_1 = turtle.Turtle()
p_1.color("green")
p_1.shape("turtle")
p_1.penup()
p_1.goto(-200,100)
p_2 = p_1.clone()
p_2.color("red")
p_2.penup()
p_2.goto(-200,-100)
p_1.goto(300,60)
p_1.pendown()
p_1.circle(40)
p_1.penup()
p_1.goto(-200,100)
p_2.goto(300,-140)
p_2.pendown()
p_2.circle(40)
p_2.penup()
p_2.goto(-200,-100)
die = [1,2,3,4,5,6]
for i in range(20):
    if p_1.pos()>=(300,60):
        print("player one wins!!")
        break
    elif p_2.pos()>=(300,-100):
        print("player two wins!!")
        break
    else:
        p_1_turn = input("press enter to roll the dice")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        p_1.fd(20*die_outcome)
        p_2_turn = input("press enter to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        p_2.fd(20*die_outcome)
        
        