
with open("ReadWriteFiles/pi_million_digits.txt", "r") as pi:
   print(pi.readline())

with open("ReadWriteFiles/pi_million_digits.txt", "r") as pi:
    pi_lines = pi.readlines()
    print(pi_lines[:500])

    

user_birthday = input("Enter your birthday in the format MMDDYY: ")


birthday_found = None
with open("ReadWriteFiles/pi_million_digits.txt", "r") as pi:
    pi_lines = pi.readlines()

    for line in pi_lines:
        if user_birthday in line:
            print("Your birthday is in the first million digits of pi")
            birthday_found = 1
            break
    if birthday_found != 1:
        print("Sorry, your birthday was not found in the first million digits of pi")

        
user_birthday = input("Enter your birthday in the format MMDDYY: ")


birthday_found = None

with open("ReadWriteFiles/pi_million_digits.txt", "r") as pi:
    pi_lines = pi.readlines()

    
    for line in pi_lines:
        if user_birthday in line:
            print("Your birthday is in the first million digits of pi")
            birthday_found = 1
            break

    if birthday_found != 1:
        print("Sorry, your birthday was not found in the first million digits of pi")


user_birthday = input("Enter your birthday in the format MMDDYY: ")


birthday_found = None


pi_string = ""


with open("ReadWriteFiles/pi_million_digits.txt", "r") as pi:
    pi_lines = pi.readlines()
    for line in pi_lines:
        pi_string += line.strip()

if user_birthday in pi_string:
    birthday_position = pi_string.index(user_birthday) - 1  
    print(f"Your birthday begins at decimal place {birthday_position}")
    birthday_found = 1
else:
    print("Sorry, your birthday was not found in the first million digits of pi")



