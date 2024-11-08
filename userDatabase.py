import re
class User:
    def __init__(self,userid,username,email):
        self.userid=userid
        self.username=username
        self.email=email
    def __str__(self):
        return f'UserID={self.userid}, Username={self.username}, Email={self.email}'

class Userdatabase:
    def __init__(self):
        self.userlist=[]

    def insert(self,data=None):
        # Insert user in ascending order by username
        if data:
            index=0
            while index<len(self.userlist):
                if data.username.lower() < self.userlist[index].username.lower():
                    break
                index+=1
            self.userlist.insert(index,data)
        else:
            #creating a new user
            print("\nMain menu->Insert user")
            user_id = self.userid_validate()
            if not user_id:
                return
            user_name = self.username_validate()
            user_email = self.useremail_validate()
            if not user_email:
                return
            new_user=User(user_id,user_name,user_email)
            self.insert(new_user)
            print("(User successfully added to the database!)")

    def username_validate(self):
        while True:
            name = input("Enter your real name: ").strip()

            if re.match("^[A-Za-z ]{2,50}$", name):
                name = ["".join(i.capitalize()) for i in name.split(" ")]
                return " ".join(name)
            else:
                print("(Invalid name. Please use only letters and spaces, and make sure it's 2-50 characters long.)")

    def userid_validate(self):
        while True:
            while not (userid := input("Enter your new userID: ").strip()):
                print("(User ID cannot be empty.)")
            if re.match("^[A-Za-z0-9@_.-]{3,15}$", userid):
                if any(user.userid == userid for user in self.userlist):
                    print(f"(User id '{userid}' already exists. Please Enter a unique user ID.)")
                    if input("Enter any key to continue or type 'exit' to return to the main menu: ").strip().lower() == 'exit':
                        print("(Returning to main menu.)")
                        return None
                else:
                    return userid
            else:
                print("(Invalid User ID. Please use only letters, digits, and characters (@,-,_,.) without spaces. and ensure it is 3-15 characters long.)")

    def useremail_validate(self):
        while True:
            while not (newEmail := input("Enter your new Email ID:-")):
                print("(Email ID cannot be empty)")
            if re.match(r"^[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*@[a-zA-Z]+(?:-[a-zA-Z]+)*\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$",newEmail):
                if any(user.email == newEmail for user in self.userlist):
                    print(f"(Email ID '{newEmail}' already exists. Please Enter a unique Email ID)")
                    if input("Enter any key to continue or type 'exit' to return to the main menu: ").strip().lower() =='exit':
                        print("(Returning to main menu.)")
                        return None
                else:
                    return newEmail
            else:
                print("(Invalid email format. Please try again!)")

    def update(self):
        if not self.userlist:
            print("(user Database is empty:!)")
            return
        purpose=input("\nMain Menu->Update\nSelect what you want to update:\n 1.User ID\n 2.Username\n 3.Email\n 4.Main Menu\n Enter your choice>>>")
        #userID
        if purpose=="1":
            id_one=input("\nMain menu->Update->User ID\nEnter current userId to update userID:-")
            for i in self.userlist:
                if i.userid == id_one:
                    new=self.userid_validate()
                    if not new:
                        return
                    i.userid=new
                    print("(User Id updated!)")
                    return
            else:
                print("(User ID not found.)")
        #userName
        elif purpose=="2":
            id_two = input("\nMain menu->Update->User Name\nEnter userId to update name:-")
            for i in self.userlist:
                if i.userid == id_two:
                    i.username = self.username_validate()
                    print('(Username updated!)')
                    return
            else:
                print("userID not found")
        #Email
        elif purpose=="3":
            id_three = input("\nMain menu->Update->Email\nEnter userId to update email:-")
            for i in self.userlist:
                if i.userid == id_three:
                    new=self.useremail_validate()
                    if not new:
                        return
                    i.email=new
                    print("(Email ID updated!)")
                    return
            else:
                print("(user id not found)")

        elif purpose=="4":
            return
        else:
            print("(Invalid option. Returning to the main menu.)")

    def delete(self):
        print("\nMain menu->Delete User")
        if not self.userlist:
            print("(user Database is empty:!)")
            return
        options= input(f"Enter the option\n 1.Delete all users\n 2.Delete a specific user\n Enter your choice>>>")
        if options=="1":
                opt = input(f"(Are you sure you want to delete all users from the database?)\nEnter 1.Confirm or 2.Cancel>>>")
                if opt=="1":
                    self.userlist.clear()
                    print("(Successfully deleted all user records. The Database is now empty.)")
                elif opt=="2":
                    print("(Action revoked!)")
                else:
                    print("(Invalid option. Returning to main menu.)")

        elif options=="2":
            user_id = input("Enter the user ID to delete:-")
            for user in self.userlist:
                if user.userid==user_id:
                    op= input(f"(Are you sure you want to delete '{user.userid}' from the database?)\nEnter 1.Confirm or 2.Cancel>>>")
                    if op=="1":
                        self.userlist.remove(user)
                        print("(User removed from Database!)")
                    elif op=="2":
                        print("(Action revoked!)")
                    else:
                        print("(Invalid option. Returning to Main menu.)")
                    return
            else:
                print("(user ID not found)")
        else:
            print("(invalid option. Returning to the main menu.)")

    def find(self):
        if not self.userlist:
            print("(user Database is empty:!)")
            return
        data=input("\nMain menu->Find user\nEnter UserID to find:-")
        for i in self.userlist:
            if i.userid == data:
                print(i)
                break
        else:
            print("(user ID not Found)")

    def listall(self):
        print("\nMain menu->View user DataBase")
        if not self.userlist:
            print("(user Database is empty!)")
            return
        for i in self.userlist:
            print(i)


#preloaded users:
muthu=User("muthu@123","Muthu","muthu@gmail.com")
sundar=User("sundar@123","Sundar","sundar@gmail.com")
jeeva=User("jeeva@123","Jeeva","jeeva@gmail.com")
us=Userdatabase()
us.insert(sundar)
us.insert(muthu)
us.insert(jeeva)

#start line.
options={1:us.insert,2:us.find,3:us.delete,4:us.update,5:us.listall}
print(f'\nSimple User DataBase')

while True:
    print(f'\nMAIN MENU\nChoose the operation below:\n 1.Insert\n 2.Find\n 3.Delete\n 4.Update\n 5.View user DataBase\n 6.Exit')
    try:
        choice=int(input(" Enter your Choice(1 to 6)>>>"))
        if choice==6:
            print("(Exiting program.)")
            break
        elif choice in options:
            options[choice]()
        else:
            print("(please enter a valid option.)")
    except ValueError:
        print("(Please! enter a valid integer option)")