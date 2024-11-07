
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


class FoodTruck(Restaurant):
    """A child class of Restaurant to represent a food truck."""

    def __init__(self, rest_name, food_type):
        
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'  
        self.truck_location = ""     
        self.location_history = []  

    def accepts_private_bookings(self):
        """Prompts if the truck accepts private bookings and updates attribute."""
        response = input("Does this food truck accept private bookings? Y/N ").strip().upper()
        if response == 'Y':
            self.private_bookings = 'Y'
            print("This food truck currently accepts private bookings.")
        else:
            self.private_bookings = 'N'
            print("This food truck does not accept private bookings.")

    def relocate_truck(self):
        """Prompts for the truck's location and adds it to the location history."""
        location = input("Enter the truck's current location (street address, city): ").strip()
        self.truck_location = location
        print(f"Truck is currently located at {self.truck_location}")

        
        if location not in self.location_history:  
            self.location_history.append(location)
    
    def show_location_history(self):
        """Prints the history of locations where the truck has been located."""
        print("\nLocation History:")
        for loc in self.location_history:
            print(loc)


food_truck = FoodTruck("Taco Frenzy", "Mexican")


food_truck.describe_rest()


food_truck.accepts_private_bookings()


food_truck.relocate_truck() 
food_truck.relocate_truck()  
food_truck.show_location_history()
