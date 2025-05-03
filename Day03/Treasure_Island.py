#Treasure island project by using Flow control using the if, elif and else conditions.

print("Welcome to Treasure Island.")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________/
******************************************************************************* ''')
print("Your mission is to find the treasure")
print("Let's start!")

print("You are at a cross-road, where do you want to go? 'Right?' or 'Left?' ")
direction = input("Press 'R' for right and 'L' for left: ")

if direction == "R":
    print("Oops you are dead now! Restart!")
elif direction == "L" :
    print("You passed the first level!")
    
    print("Welcome to the second level \n Now you are in a dessert and you see a pond near a palm tree \n Would you swim or would you wait for night? ")
    level_2 = input("Press 'S' for swim and 'W' for wait : ")

    if level_2 == "S":
        print("It was a mirage! You failed level 2")

    elif level_2 == "W":
        print("You passed level 2! Now to the last level!")

        print("You are in the last stage of the treasure hunt! \n There are 3 doors infront of you 'Red' 'Blue' 'Green'. Which one would you choose?")
        level_3= input("Select 'R' for red door 'B' for Blue door and 'G' for Green door : ")

        if level_3 == 'R':
            print("You choose the wrong door! Game over!")
        
        elif level_3 == 'B' :
            print("You choose the right door! You won the Game! WINNERRRR")

        elif level_3 == 'G' :
            print("You choose the wrong door! Game over!")

        else :
            print("Invalid format, please read the instruction again!")

    else:
        print("Invalid selection! Please read the instruction again!")

else :
    print("Invalid selection, please read the instruction again!")

