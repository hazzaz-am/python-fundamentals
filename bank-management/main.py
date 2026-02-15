# Create Bank Account
# Deposit Money
# Withdraw Money
# Personal Details
# Update Personal Details
# Delete Account
import json
import random
import string
from pathlib import Path

class Bank:
  database = 'data.json'
  data = []

  try:
    if Path(database).exists():
      with open(database) as fs:
       data = json.load(fs.read())
    else:
      print("no such file exits")
  except Exception as err:
    print(f"an exception occurred as {err}")

  def create_account(self):
    data = {
      "name": input("What's your name? "),
      "age": int(input("What's your age? ")),
      "email": input("What's your email? "),
      "pin": int(input("Enter your 4 digit PIN: ")),
      "accountNo": 1234,
      "balance": 0
    }

    if data["age"] < 18 or data["pin"] != 4:
      print("Sorry you can't create your account")
    else:
      print("account created successfully")
      for i in data:
        print(f"{i} : {data[i]}")
      print("please note down your account number")


  def deposit_money(self):
    pass

  def withdraw_money(self):
    pass

  def see_account_details(self):
    pass

  def update_account_details(self):
    pass

  def delete_account(self):
    pass


user = Bank()

print("Press 1 for creating an account")
print("Press 2 for deposit money")
print("Press 3 for withdraw money")
print("Press 4 for see account details")
print("Press 5 for update account details")
print("Press 6 for delete an account")

check = int(input("Choose your choice: "))

if check == 1:
  user.create_account()
elif check == 2:
  user.deposit_money()
elif check == 3:
  user.withdraw_money()
elif check == 4:
  user.see_account_details()
elif check == 5:
  user.update_account_details()
elif check == 6:
  user.delete_account()
