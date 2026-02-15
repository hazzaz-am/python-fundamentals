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
      "age": int(input("What's your age? ")),
      "email": input("What's your email? "),
      "pin": int(input("Enter your 4 digit PIN: ")),
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
