#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 
           'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
    # password = ""
    # for let in range(0, nr_letters):
    #     password += random.choice(letters)

    # for sym in range(0, nr_symbols):
    #     password += random.choice(symbols)
        
    # for num in range(0, nr_numbers):
    #     password += random.choice(numbers)
    # print(f"your password is: {password}")

#Hard Level

# #option 01
    # password = ""
    # sum_number = nr_letters + nr_symbols + nr_numbers

    # for i in range(0, sum_number):
    #     random_number = random.randint(0, 2)
    #     if (random_number == 0 and i <= nr_letters) or (random_number == 1 and i <= nr_symbols) or (random_number == 2 and i <= nr_numbers):
    #         random_number = random.randint(0, 2)
            
    #     if random_number == 0:
    #         random_number_of_letters = random.randint(0, len(letters) - 1)
    #         password += letters[random_number_of_letters]
    #     elif random_number == 1:
    #         random_number_of_symbols = random.randint(0, len(symbols) - 1)
    #         password += symbols[random_number_of_symbols]
    #     elif random_number == 2:
    #         random_number_of_numbers = random.randint(0, len(numbers) - 1)
    #         password += numbers[random_number_of_numbers]

    # print(f"your password is: {password}")

# #option 02
password_list = []
for let in range(0, nr_letters):
    password_list.append(random.choice(letters))

for sym in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
    
for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
    
#option 02 - 01
    # password = ""
    # lengt_of_password_list = len(password_list)
    # for p in range(0, lengt_of_password_list):
    #     random_choice = random.choice(password_list)
    #     password += random_choice
    #     password_list.remove(random_choice)
    # print(f"your password is: {password}")

# #option 02 - 02
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is: {password}")