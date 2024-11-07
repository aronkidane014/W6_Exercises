try:
    
    number = int("Hello")
except ValueError:
    print("ValueError: Oops, that was not a valid number")
else:
    print("No error occurred")
finally:
    print("Let's try another one...")
try:
   
    print(undeclared_variable)
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")
else:
    print("No error occurred")
finally:
    print("Let's try another one...")
try:
   
    result = "string" + 5
except TypeError:
    print("TypeError: Oops, cannot combine a string with an integer")
else:
    print("No error occurred")
finally:
    print("Let's try another one...")

try:
    
    eval("def my_function(:)")
except SyntaxError:
    print("SyntaxError: Oops, there's a problem with the code structure")
else:
    print("No error occurred")
finally:
    print("Let's try another one...")

