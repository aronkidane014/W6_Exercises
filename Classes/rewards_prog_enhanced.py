class RewardsProgram:
    """A class to manage a customer's rewards program, tracking visits and points earned."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []  
        self.rewards_points = 0  
        self.rewards_by_restaurant = {}  

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        global cust_list
        cust_list.append((self.cust_name, self.phone, self.email))

    def visit_rest(self):
        restaurant_name = input("Name of restaurant: ").strip()
        
        
        if restaurant_name not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant_name)

        
        try:
            bill_amount = float(input("What was the total food bill for this visit? $"))
            points_for_this_visit = self.calculate_rewards(bill_amount)
            print(f"Points for this visit: {points_for_this_visit}")
            
            
            self.rewards_points += points_for_this_visit
            print(f"Total rewards points earned: {self.rewards_points}")

            
            if restaurant_name in self.rewards_by_restaurant:
                self.rewards_by_restaurant[restaurant_name] += points_for_this_visit
            else:
                self.rewards_by_restaurant[restaurant_name] = points_for_this_visit

            print(f"Thank you for visiting {restaurant_name}!")

        except ValueError:
            print("Invalid input. Please enter a valid bill amount.")

    def calculate_rewards(self, bill_amount):
        """Calculate rewards points based on the bill amount. Points are earned at a rate of $1 to 1 point."""
        points = int(bill_amount)  
        return points


cust_list = []


customer1 = RewardsProgram("Mohamed Salah", "555-1234", "salah@liverpool.com")


customer1.profile()


customer1.visit_rest()  
customer1.visit_rest()  
customer1.visit_rest() 


print("\nRewards Points by Restaurant:")
for restaurant, points in customer1.rewards_by_restaurant.items():
    print(f"{restaurant}: {points} points")
