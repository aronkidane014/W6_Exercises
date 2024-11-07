class Restaurant:
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0  
        self.customer_ratings = []  

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        try:
            num_served_today = int(input("How many customers served today? "))
            if num_served_today < 0:
                print("Please enter a non-negative number.")
            else:
                self.number_served += num_served_today
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self):
        try:
            rating = int(input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? "))
            if 1 <= rating <= 5:
                self.customer_ratings.append(rating)
                average_rating = sum(self.customer_ratings) / len(self.customer_ratings)
                print(f"Your rating was {rating}. The average rating for this restaurant is {average_rating:.1f}")
            else:
                print("Please enter a rating between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 5.")


restaurant1 = Restaurant("Weed's", "Fast Food")
restaurant2 = Restaurant("Burgir Kirg", "Burgers")
restaurant3 = Restaurant("Tinkle Outside the Binkle", "Mexican")


restaurant1.print_num_served()


restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()


restaurant1.customer_rating() 
restaurant1.customer_rating()  
restaurant1.customer_rating()  
restaurant1.customer_rating()  
