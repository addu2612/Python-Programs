import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters_nr=int(input("How many letters would you like in the password?:\n"))
numbers_nr=int(input("How many numbers would you like in the password?:\n"))
symbols_nr=int(input("How many symbols would you like in the password?:\n"))

password=""

for i in range(0,letters_nr):
    a=random.choice(letters)
    password+=a
for i in range(0,numbers_nr):
    b=random.choice(numbers)
    password+=b
for i in range(0,symbols_nr):
    c=random.choice(symbols)
    password+=c       
password_list=list(password)
random.shuffle(password_list)

print("".join(password_list))