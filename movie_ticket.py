day = input("Enter a day: ").lower()
age = int(input("Enter your age: "))
fam_input = input("Are you with family?: ").lower()
ticket = 0
ticket_after_discount = 0
family_discount = 0

def calculate_ticket_price():
    global ticket
    if day == "monday":
        ticket = 1000
    elif day == "tuesday":
        ticket = 900
    elif day == "wednesday":
        ticket = 800
    elif day == "thursday":
        ticket = 700
    elif day == "friday":
        ticket = 600
    elif day == "saturday":
        ticket = 500
    elif day == "sunday":
        ticket = 1200
    else:
        print("Invalid day")
        return calculate_ticket_price()

def calculate_discount():
    global ticket_after_discount
    if age < 18:
        ticket_after_discount = ticket - 50
    elif 18 <= age < 25:
        ticket_after_discount = ticket - 30
    else:
        ticket_after_discount = ticket - 100

def apply_family_discount():
    global family_discount
    if fam_input in ["ye", "yesh", "yep", "y","yes"]:
        family_discount = ticket_after_discount - 40
    elif fam_input in ["no", "nope", "nah", "noo", "n"]:
        family_discount = "No discount"
    else:
        family_discount = "No answer"

calculate_ticket_price()
calculate_discount()
apply_family_discount()

print(f"Your ticket price is {ticket}")
print(f"After discount, it is {ticket_after_discount:.2f}")
print(f" Family discount is 40 rs ")
print(f" After fam discpunt is {family_discount}")
