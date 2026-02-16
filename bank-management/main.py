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
       data = json.loads(fs.read())
    else:
      print("no such file exits")
  except Exception as err:
    print(f"an exception occurred as {err}")

  @staticmethod
  def update():
    with open(Bank.database, 'w') as fs:
      fs.write(json.dumps(Bank.data))

  @classmethod
  def __create_account_number(cls):
    char = random.choices(string.ascii_letters, k = 3)
    int = random.choices(string.digits, k = 3)
    sp_char = random.choices("!@#$%^&*(){}[]'';?/", k = 1)
    id_num = char + int + sp_char
    random.shuffle(id_num)
    return "".join(id_num)

  def create_account(self):
    info = {
      "name": input("What's your name? "),
      "email": input("What's your email? "),
      "pin": int(input("Enter your 4 digit PIN: ")),
      "age": int(input("What's your age? ")),
      "accountNo": Bank.__create_account_number(),
      "balance": 0
    }

    if info["age"] < 18 or len(str(info["pin"])) != 4:
      print("Sorry you can't create your account")
    else:
      print("account created successfully")
      for i in info:
        print(f"{i} : {info[i]}")
      print("please note down your account number")

      Bank.data.append(info)
      Bank.update()

  def deposit_money(self):
    account_number = input("Please tell me your account number! ")
    pin = int(input("Enter your pin "))

    user_data = [i for i in Bank.data if i["accountNo"] == account_number and i["pin"] == pin]

    if user_data == False:
      print("Sorry your data not found")
    else:
      amount = int(input("Enter your deposit amount "))
      if amount > 10000 or amount < 500:
        print("Sorry the amount is too big or too low to deposit")
      else:
        user_data[0]["balance"] += amount
        Bank.update()
        print("Balance updated successfully")

  def withdraw_money(self):
    account_num = input("What is your account number ? ")
    pin = int(input("Enter your pin number- "))

    user_data = [i for i in Bank.data if i["accountNo"] == account_num and i["pin"] == pin]

    if user_data == False:
      print("Sorry, Your account not found")
    else:
      amount = int(input("Enter your withdraw amount- "))
      if amount > 10000 or amount < 500:
        print("Sorry, Your can't withdraw more than 10,000 and less than 500")
      else:
        print(user_data)
        user_data[0]["balance"] -= amount
        Bank.update()
        print(f"{amount} is deducted from your account successfully")



  def see_account_details(self):
    account_num = input("Enter your account number: ")
    pin = int(input("Enter your pin number: "))

    user_data = [i for i in Bank.data if i["accountNo"] == account_num  and i["pin"] == pin]

    if user_data == False:
      print("Account Not Found")
    else:
      print("This is your information: ")
      print("-------------------------------")
      print("-------------------------------\n\n\n")
      for i in user_data[0]:
        print(f"{i} is {user_data[0][i]}")

  def update_account_details(self):
    account_num = input("Enter your account number: ")
    pin = int(input("Enter your pin number: "))

    user_data = [i for i in Bank.data if i["accountNo"] == account_num  and i["pin"] == pin]
    
    if user_data == False:
      print("Account not found")
    else:
      print("You can't update your age, account number and balance")

      new_data = {
        "name": input("Enter your updated name or press ENTER to skip: "),
        "email": input("Enter your updated mail or press ENTER to skip: "),
        "pin": int(input("Enter your updated pin or press ENTER to skip: ")),
      }

      if new_data["name"] == "":
        new_data["name"] = user_data[0]["name"]
      if new_data["email"] == "":
        new_data["email"] = user_data[0]["email"]
      if new_data["pin"] == "":
        new_data["pin"] = user_data[0]["pin"]
      
      new_data["age"] = user_data[0]["age"]
      new_data["accountNo"] = user_data[0]["accountNo"]
      new_data["balance"] = user_data[0]["balance"]

      for i in new_data:
        if new_data[i] == user_data[0][i]:
          continue
        else:
          user_data[0][i] = new_data[i]
      
      Bank.update()
      print("Account updated successfully")



  def delete_account(self):
    account_num = input("Enter your account number: ")
    pin = int(input("Enter your pin number: "))

    user_data = [i for i in Bank.data if i["accountNo"] == account_num  and i["pin"] == pin]

    if user_data == False:
      print("Sorry, Your Account Not Found!")
    else:
      check = input("Pres Y/y for DELETE or Press N/n for SKIP: ")
      
      if check == "y" or check == "Y":
        index = Bank.data.index(user_data[0])
        Bank.data.pop(index)
        Bank.update()
        print("Your account deleted successfully")
      else:
        print("Skipped")
      


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
