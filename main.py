import random

print("Welcome to the hand Cricket competion!!!")
marks = [1,2,3,4,5,6,7]

overs = 0
score = 0
opponet_score = 0

name = input("enter player's name: ")
print(name,"is batting!!!\n")




while True:
    mark = input("enter your mark ( from 1 to 7: ")
    if int(mark) > 7:
        print("enter a valid number within the range!!")
        continue

    wicket = random.randint(0, 6)
    opponent = marks[wicket]
    print("opponents mark is", opponent)

    if int(mark) != int(opponent) :
        score += int(mark)
        overs += 1
        print("your score is",score)
    elif int(mark) == int(opponent) or int(overs) <=6  :
        print("your turn is over!!!")
        break

print("\nnow your opponent is batting")
print("your taget is",score + 1)

while True:
    mark = input("enter your mark ( from 1 to 7: ")
    if int(mark) > 7:
        print("enter a valid number within the range!!")
        continue

    wicket = random.randint(0, 6)
    opponent = marks[wicket]
    print("opponents mark is", opponent)

    if int(mark) != int(opponent):
        opponet_score += int(opponent)
        overs += 1
        print("your opponent's is",opponet_score)
    elif int(mark) == int(opponent) or int(overs) <=6 :
        print("your opponet's turn is over!!!")
        break


print("\nyour score is",score)
print("your opponest's score is",opponet_score)

if score > opponet_score:
    print("\nyou won!!!")
elif score < opponet_score:
    print("you lost!!!")
elif score == opponet_score:
    print("its a tie!!!""")
