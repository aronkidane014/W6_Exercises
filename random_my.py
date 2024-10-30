import random
fruit_list= ["apple", "banana", "cherry", "peach", "plum", "watermelon"]
for _ in range(1):
    choice_fruit = random.choice(fruit_list)
    print(F"your fruit of the day is: {choice_fruit}")

for i in range(1):
    random.shuffle(fruit_list)
    print(f"your fruit selection is: {fruit_list[i]}")

sampled_ftuits= random.sample(fruit_list, 2)
for fruit in sampled_ftuits:
    print(f"your sample fruit is:{fruit}")
    print("\n")

random_function = random.random
print("Using random.random():")
for _ in range(5):  
    print(f"Random float: {random_function()}")