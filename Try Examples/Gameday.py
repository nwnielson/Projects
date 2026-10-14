import Bank_Functions

balance = 100

try: 
    amount = int(input("Please enter the amount you would like to withdraw: $"))
    balance = Bank_Functions.withdraw(amount, balance)
    print(f"New Balance: ${balance}")
except :
    print("Invalid Amount")