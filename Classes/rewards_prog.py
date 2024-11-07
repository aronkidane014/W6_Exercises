cust_list = []

class RewardsProgram:
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email 

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        global cust_list
        cust_list.append((self.cust_name, self.phone, self.email))


customer1 = RewardsProgram("Mohamed Salah", "555-1234", "salah@liverpool.com")
customer2 = RewardsProgram("Virgil van Dijk", "555-5678", "vandijk@liverpool.com")
customer3 = RewardsProgram("Alisson Becker", "555-9101", "alisson@liverpool.com")


customer1.profile()
customer1.thank_you()
customer1.add_to_cust_list()

customer2.profile()
customer2.thank_you()
customer2.add_to_cust_list()

customer3.profile()
customer3.thank_you()
customer3.add_to_cust_list()


print("\nCustomer List:")
for cust in cust_list:
    print(cust)
