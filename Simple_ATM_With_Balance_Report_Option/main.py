# Simple ATM With Amount Balance Report for Student Practice
import re

balance = 0.00
# Creating file that will store our amount balance
filename = open("recept.txt", "w")
filename.write("YOUR RECEPT\n")
filename.write("Your Balance\t\t:" + str(balance) + "\n")
filename.close()
# Creating Password
new_password = input("Enter New Password\n")
print("You password has successful changed")
main_selection = input("Press \n1.Login\n2.Exit")
if int(main_selection) == 1:
    password = input("Enter Password")
    # Checking for password match
    entry_pass = re.fullmatch(new_password, password)
    if entry_pass:
        while True:
            # Selection Menu
            selection = int(
                input(
                    "WELCOME TO ATM  SERVICES\nPRESS TO\n1.DEPOSIT\n2.WITHDRAW\n3.CHECK BALANCE\n4.EXIT\n5.Full report Balance\n"))
            if selection == 1:
                amount = float(input("Enter Amount\n"))
                balance += amount
                # Saving data into the recept file
                filename = open("recept.txt", "a")
                filename.write("________________________________\n" + "Your Balance\t\t:" + str(balance) + "\n")
                filename.close()
            elif selection == 2:
                sub_amount = float(input("Enter Amount\n"))
                if sub_amount > balance:
                    print("YOU HAVE INSUFFICIENT AMOUNT\nYOUR ACCOUNT BALANCE :", balance, "\n")
                else:
                    balance -= sub_amount
                    print("YOU HAVE WITHDRAW :", sub_amount, "YOUR BALANCE :", balance, "\n")
                    # Updating data into the recept file
                    filename = open("recept.txt", "a")
                    filename.write("Sub_Amount\t\t:" + str(
                        sub_amount) + "\n" + "________________________________\n" + "New_Balance\t\t:" + str(
                        balance) + "\n" + "________________________________\n")
                    filename.close()
            elif selection == 3:
                print("YOUR BALANCE :", balance, "\n")
            elif selection == 5:
                # Opening file and reading it line by line using loop
                filename = open("recept.txt", "r")
                for i in filename:
                    print(i)
                filename.close()
            elif selection == 4:
                exit()
            else:
                exit()
    else:
        print("Wrong Password\n Goodbye")
# TODO 1.Password Storage/Cold boot Session Validation 2.Data input Validation 3.Session info
