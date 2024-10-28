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