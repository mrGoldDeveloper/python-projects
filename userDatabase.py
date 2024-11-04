import re
class user:
    def __init__(self,userid,username,email):
        self.userid=userid
        self.username=username
        self.email=email
    def __str__(self):
        return f'userID={self.userid}, userName={self.username}, email={self.email}'

class userDatabase:
    def __init__(self):
        self.userlist=[]

    def insert(self,data=None):
        # store user ascending order by name
        if data:
            index=0
            while index<len(self.userlist):
                if data.username < self.userlist[index].username:
                    break
                index+=1
            self.userlist.insert(index,data)
        else:
            #creating new user
            print("\nMain menu->Insert user")
            UID = self.userid_validate()
            if not UID:
                return
            UNAME = self.username_validate()
            UEMAIL = self.useremail_validate()
            if not UEMAIL:
                return
            new_user=user(UID,UNAME,UEMAIL)
            self.insert(new_user)
            print("(User successfully added to the database!)")

    def username_validate(self):
        while True:
            name = input("Enter your real name: ").strip()

            # Regex for alphabetic characters and spaces, between 2 to 50 characters
            if re.match("^[A-Za-z ]{2,50}$", name):
                return name
            else:
                print("(Invalid name. Please use only letters and spaces, and make sure it's 2-50 characters long.)")

    def userid_validate(self):
        while True:
            while not (userid := input("Enter your new userID: ").strip()):
                print("(User ID cannot be empty.)")
            if re.match("^[A-Za-z0-9@_.-]{3,15}$", userid):
                for valid_user in self.userlist:
                    if userid == valid_user.userid:
                        print(f"(User id '{userid}' already exists.Enter a unique user ID.)")
                        option = input("Enter any key to continue or type 'exit' to return to the main menu: ").strip().lower()
                        if option == 'exit':
                            return None
                        break
                else:
                    return userid
            else:
                print("(Invalid name. Please use only letters, digits, and characters (@,-,_,.) without space. and make sure it's 3-15 characters long.)")

    def useremail_validate(self):
        while True:
            while not (newEmail := input("Enter your new Email-ID:-")):
                print("(Email ID cannot be empty)")
            if re.match(r"^[a-zA-Z0-9]+(?:[._-][a-zA-Z0-9]+)*@[a-zA-Z]+(?:-[a-zA-Z]+)*\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$",newEmail):
                for val_user in self.userlist:
                    if val_user.email == newEmail:
                        print(f"(Email ID '{newEmail}' already exists. Enter a unique Email ID)")
                        option = input("Enter any key to continue or type 'exit' to return to the main menu: ").strip().lower()
                        if option == 'exit':
                            return None
                        break
                else:
                    return newEmail
            else:
                print("(Invalid email format. Please try again!)")
    def update(self):
        if self.userlist == []:
            print("(user Database is empty:!)")
            return
        for _ in range(1):
            purpose=input("\nMain Menu->Update\nEnter the option you want to Update:\n 1.userID\n 2.username\n 3.email\n 4.Main Menu\n Enter your choice>>>")
        #userID
        if purpose=="1":
            id_one=input("\nMain menu->Update->User ID\nEnter your userId:-")
            for i in self.userlist:
                if i.userid == id_one:
                    new=self.userid_validate()
                    if not new:
                        return
                    i.userid=new
                    print("(User Id updated!)")
                    return

            else:
                print("userID not found")

        #userName
        elif purpose=="2":
            id_two = input("\nMain menu->Update->User Name\nEnter your userId:-")
            for i in self.userlist:
                if i.userid == id_two:
                    new = self.username_validate()
                    i.username=new
                    print('(User Name updated!)')
                    break
            else:
                print("userID not found")
        #Email
        elif purpose=="3":
            id_three = input("\nMain menu->Update->Email\nEnter your userId:-")
            #loopbreaker=False
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

        elif int(purpose)>=4:
            return
    def delete(self):
        print("\nMain menu->Delete User")
        if self.userlist == []:
            print("(user Database is empty:!)")
            return
        if input(f"Enter the option\n 1.Delete all the user\n 2.Delete a particular user\n Enter your choice>>>") == "1":
            if input(f"(Are you sure? you want to delete all the users from user database?)\nEnter 1.Confirm or 2.Cancel>>>") == "2":
                print("(Action revoked!)")
                return
            self.userlist.clear()
            print("(Successfully deleted all user records. The Database is now empty.)")
            return
        id = input("Enter user ID:-")
        for user in self.userlist:
            if user.userid==id:
                if input(f"(Are you sure? you want to delete {user.userid} from user database?)\nEnter 1.Confirm or 2.Cancel>>>")=="2":
                    print("(Action revoked!)")
                    return
                self.userlist.remove(user)
                print("(User removed from Database!)")
                return
        else:
            print("(user ID not found)")

    def find(self):
        if self.userlist == []:
            print("(user Database is empty:!)")
            return
        data=input("\nMain menu->Find user\nEnter UserID:-")
        for i in self.userlist:
            if i.userid == data:
                print(i)
                break
        else:
            print("(user ID not Found)")
    def listall(self):
        print("\nMain menu->View user DataBase")
        if self.userlist == []:
            print("(user Database is empty:!)")
            return
        for i in self.userlist:
            print(i)
#preloaded users:
muthu=user("muthu@123","muthu","muthu@gmail.com")
sundar=user("sundar@123","sundar","sundar@gmail.com")
jeeva=user("jeeva@123","jeeva","jeeva@gmail.com")
us=userDatabase()
us.insert(sundar)
us.insert(muthu)
us.insert(jeeva)
#start line.
options={1:"us.insert()",2:"us.find()",3:"us.delete()",4:"us.update()",5:"us.listall()",6:"6"}
print(f'\nUser DataBase')
n="start"
while n!="6":
    print(f'\nMAIN MENU\nChoose the operation Below\n 1.Insert\n 2.Find\n 3.Delete\n 4.Update\n 5.View user DataBase\n 6.Exit')
    try:
        choice=int(input(" Enter your Choice>>>"))
        userchoice=options[choice]
        n = userchoice
        eval(userchoice)
    except:
        print("(Please! enter valid option)")