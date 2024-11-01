name = input("Enter a name: ")

def trunc_name(name):
    name = name.lower()  
    if name[0] in 'aeiou':
        return name  
    elif len(name) > 1 and name[0] not in 'aeiou' and name[1] in 'aeiou':
        return name[1:]  
    else:
        return name[2:]  

truncated = trunc_name(name)

print(f"Original Name: {name}")
print(f"Truncated Name: {truncated}")

def name_game(name):
   
    truncated = trunc_name(name)

    
    yield f"{name.capitalize()}, {name.capitalize()}, bo-{truncated}"
    yield f"banana fana fo-{truncated}"
    yield f"me my mo-{truncated}"
    yield f"{name.capitalize()}!"


    if name[0].lower() in 'bfm':
        special_trunc = name[1:]  
        yield f"banana fana fo-{special_trunc}"
        yield f"me my mo-{special_trunc}"
        yield f"{name.capitalize()}!"


test_names = [name, "carly", "CHARLIE", "Aidan", "Braden", "Billy Bob"]


for test_name in test_names:
    print(f"\nName Game for: {test_name}")
    for line in name_game(test_name):
        print(line)