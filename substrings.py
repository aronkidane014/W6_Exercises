# Full_Name= "Ibrahima Konate"
# #print(f"full Name:{Full_Name.find("Ibrahima Konate")}")
 
# name_space = Full_Name.find(" ")
# first_name= Full_Name[:name_space]
# last_name= Full_Name[name_space + 1:]
# print(f"Full Name:{Full_Name}")
# print(f"First Name: {first_name}")
# print(f"Last Name:{last_name}")

Names= ["Trent Arnold", "Darwin Nunez", "Mohammed Salah"]
for full_name in Names:
 name_space = full_name.find(" ")
 first_name= full_name[:name_space]
 last_name= full_name[name_space + 1:]

 print(f"Full Name: {full_name}")
 print(f"First Name: {first_name}")
 print(f"Last Name: {last_name}\n")

 def format_name(name):
    
    name_parts = name.split()
    
    
    Names = [
    "Lorde",
    "Billie Eilish",
    "Megan Thee Stallion"
]

def format_name(full_name):
    name_parts = full_name.split()
    
    if len(name_parts) == 1:
        return f"Name: {name_parts[0]}"
    elif len(name_parts) == 2:
        first_name, last_name = name_parts
        return f"First Name: {first_name}, Last Name: {last_name}"
    elif len(name_parts) == 3:
        first_name, middle_name, last_name = name_parts
        return f"First Name: {first_name}, Middle Name: {middle_name}, Last Name: {last_name}"
    else:
        return "Invalid name format"

for full_name in Names:
    formatted_name = format_name(full_name)
    print(f"Full Name: {full_name}")
    print(formatted_name)
    print()
