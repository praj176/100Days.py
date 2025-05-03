import random

print("Welcome to the Rock Paper Scissors Game!")
user = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors: "))

# Print user choice
if user == 0:
    print("You chose Rock!")
    print('''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     ''')
elif user == 1:
    print("You chose Paper!")
    print('''
    | '_ \ / _` | '_ \ / _ \ '__|
    | |_) | (_| | |_) |  __/ |   
    | .__/ \__,_| .__/ \___|_|   
    | |         | |              
    |_|         |_ ''')
elif user == 2:
    print("You chose Scissors!")
    print('''  _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
''')
else:
    print("Invalid choice. Please enter 0, 1, or 2.")
    exit()

# Computer's choice
bot = random.randint(0, 2)

# Print bot choice
if bot == 0:
    print("Computer chose Rock!")
    print('''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     ''')
elif bot == 1:
    print("Computer chose Paper!")
    print('''
    | '_ \ / _` | '_ \ / _ \ '__|
    | |_) | (_| | |_) |  __/ |   
    | .__/ \__,_| .__/ \___|_|   
    | |         | |              
    |_|         |_ ''')
else:
    print("Computer chose Scissors!")
    print('''  _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
''')

# Decide the winner
if user == bot:
    print("It's a draw!")
elif user == 0 and bot == 2:
    print("You win!")
elif user == 0 and bot == 1:
    print("You lose!")
elif user == 1 and bot == 0:
    print("You win!")
elif user == 1 and bot == 2:
    print("You lose!")
elif user == 2 and bot == 1:
    print("You win!")
elif user == 2 and bot == 0:
    print("You lose!")
else:
    print("Something went wrong!")
