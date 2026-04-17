class chatbook:
    __user_id = 0
    def __init__(self):
        self.__name = "default user"
        self.id = chatbook.__user_id
        chatbook.__user_id+=1
        # self.user_id+=1
        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    @staticmethod
    def get_id():
        return chatbook.__user_id
    def set_id(val):
        chatbook.__user_id = val
    def get_name(self):
        return self.__name
    def set_name(self, value):
        self.__name = value

    def menu(self):
        user_input = input("""Welcome to chatbook !! Hw would you like to proceed?" 
                            "1. Press 1 to singup" 
                            "2. Press 2 to signin" 
                            "3. Press 3 to write a Post" 
                            "4. Press 4 to message a friend" 
                            "5. Press any other key to exit -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("enter your password -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first by pressing 1 in main menu")
        else:
            username = input("enter your email/username here -> ")
            pwd = input("enter your password -> ")
            if self.username == username and self.password == pwd:
                print('You have signed in successfully')
                self.loggedin = True
            else:
                print('Please input the correct credentials')
        print("\n")
        self.menu()
    def my_post(self):
        if self.loggedin == True:
            txt = input('Enter your message here -> ')
            print("following content has been posted ->", txt)
        else:
            print('You need to signin first to post')
        print("\n")
        self.menu()
    def sendmsg(self):
        if self.loggedin == True:
            txt = input('Enter your message here -> ')
            frnd = input('whom to send message ->')
            print('Your message has been send to friend',frnd)
        else:
            print('You need to signin first to send message')
        print("\n")
        self.menu()  


# obj = chatbook()