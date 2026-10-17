print("Welcome")

def deposit(username, amt): 
    balance = 0
    balance += amt  #add the balance to the amount
    print(f"Hello {username}, your new balance is {balance}")

"""
user= input("Enter your username: ")
amount= int(input("Enter the amount to deposit: ")) #parse the information into an integer
deposit(user, amount)
"""

try:
    user= input("Enter your username: ")
    amount= int(input("Enter the amount to deposit: "))
    deposit(user, amount)
except:
    print("Invalid input")
#print("50" + "50") #concatenates two strings

