print("Welcome to Shukran Supermarkets!")
total = int(input("Total amount to be paid: "))

# Initialize the cash register with denominations and their initial counts
def initialize_register():
    return {
        1000: 10,  # 10 notes of 1000
        500: 20,   # 20 notes of 500
        200: 30,   # 30 notes of 200
        100: 50,   # 50 notes of 100
        50: 100,   # 100 notes of 50
        20: 200,   # 200 notes of 20
        10: 300,   # 300 coins of 10
        5: 500,    # 500 coins of 5
        1: 1000    # 1000 coins of 1
    }

# Display current cash register status
def display_register(register):
    print("Current cash register status:")
    for denomination, count in register.items():
        print(f"{denomination}: {count} notes/coins")

# Payment options selection
def payment_options(register):
    print("Payment Options:")
    print("1. Cash")
    print("2. Mobile Money")
    inp = int(input("Choose your payment option: "))
    if inp == 1:
        cash(register)
    elif inp == 2:
        mobile_money()
    else:
        print("Enter a valid option")
        payment_options(register)  # Prompt again if an invalid option is chosen

# Cash payment handling
def cash(register):
    while True:
        cash_paid = int(input("Enter amount paid in cash: "))
        if cash_paid < total:
            # Insufficient cash
            print("Insufficient cash")
            deficient = total - cash_paid
            print("Amount to be added: ", deficient)
        else:
            change = cash_paid - total
            if change == 0:
                print("No change needed.")
            else:
                print("Change: ", change)
                if not give_change(change, register):
                    print("Unable to provide exact change due to insufficient denominations.")
            end()
            break

# Function to give change and update the register
def give_change(change, register):
    denominations = sorted(register.keys(), reverse=True)
    change_distribution = {}

    for denom in denominations:
        if change >= denom and register[denom] > 0:
            count = min(change // denom, register[denom])  # Limit by available notes
            if count > 0:
                change_distribution[denom] = count
                register[denom] -= count  # Update register
                change -= denom * count

    # Print the change breakdown if exact change was possible
    if change == 0:
        print("Change breakdown:")
        for denom, count in change_distribution.items():
            print(f"{denom} x {count} note/coin(s)")
        return True
    else:
        # If exact change could not be given, return the denominations to the register
        for denom, count in change_distribution.items():
            register[denom] += count
        return False

# Mobile money payment handling
def mobile_money():
    mobile_pay = int(input("Enter amount paid on mobile money: "))
    if mobile_pay == total:
        end()
    elif mobile_pay > total:
        print("Amount paid exceeds total charged!")
        print("Amount to be refunded: ", mobile_pay - total)
        end()
    else:
        print("Insufficient mobile money")
        deficient = total - mobile_pay
        print("Amount to be added: ", deficient)
        end()

# End transaction message
def end():
    print("Thank you for shopping at Shukran Supermarkets!")
    display_register(register)  # Show the updated cash register status after each transaction

# Initialize the register and start the transaction
register = initialize_register()  # Initialize cash register
display_register(register)  # Display initial register status
payment_options(register)# Start the payment process