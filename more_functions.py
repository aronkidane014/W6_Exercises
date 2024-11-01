
def display_mailing_label(name, address, city, state, zip_code):
    print(f"{name}")
    print(f"{address}")
    print(f"{city}, {state} {zip_code}")
    print("\n")


def add_numbers(*args):
    numbers_str = " + ".join(str(num) for num in args)
    result = sum(args)
    print(f"{numbers_str} = {result}")

def display_receipt(total_due, amount_paid):
    if amount_paid >= total_due:
        change_due = amount_paid - total_due
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Change Due: ${change_due:.2f}")
    else:
        balance_remaining = total_due - amount_paid
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Balance Remaining: ${balance_remaining:.2f}")
    print("\n")


display_mailing_label("Aron Kidane", "123 Main St", "Asmara", "ER", "12345")
display_mailing_label("Sara Johnson", "456 Elm St", "Addis Ababa", "ET", "54321")


add_numbers(5)                     
add_numbers(10, 20)                
add_numbers(1, 2, 3, 4, 5)         


display_receipt(50.00, 60.00)      
display_receipt(75.00, 75.00)     
display_receipt(30.00, 20.00)      
