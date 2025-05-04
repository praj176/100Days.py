#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

let = int(input("Enter the number of letters you want to use?"))
num = int(input("Enter the number of numbers you want to use for your password?"))
symb = int(input("Enter the number of symbol characters to use in your password?"))

#Easy level passwords are generated in a defined sequence

# password = ""
# for l in range(0,let):
#     password += random.choice(letters)
    
# for n in range(0,num):
#     password += random.choice(numbers)
    
# for s in range(0,symb):
#     password += random.choice(symbols)
    
# print(password)

#Hard level : Password are random 

list = []
for l in range(0,let):
    list += random.choice(letters)
    
for n in range(0,num):
    list.append(random.choice(numbers))
    
for s in range(0,symb):
    list += random.choice(symbols)
    
random.shuffle(list)

print(list)

password = ""
for i in list:
    password += i

print(f"Your password is -> {password}")
    

     
