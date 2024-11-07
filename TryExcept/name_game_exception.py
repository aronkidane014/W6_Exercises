def play_name_game():
    
    name = None
    while name == None:
        try:
            name = input('Name? ').lower()
            
            
            if len(name) < 2 or not name.isalpha():
                raise ValueError("Not a valid name (must be 2 or more letters)")
        except ValueError as e:
            print(e)  
        else:
           
            print(f"Hello, {name.title()}!")
            break

    
    n = None
    while n == None:
        try:
            n = name[1]  
        except IndexError:
            print("Not a valid name (must be 2 or more letters)")
            raise SystemExit(0) 

   
    print(f"Your second letter is: {n}")


play_name_game()
