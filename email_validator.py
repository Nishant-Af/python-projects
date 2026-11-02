class Email:

    def Setemail(self):
        self.email = input("Enter email : ")    # g@g.in or gamer@gmail.com

    def chk_email(self):

        if(len(self.email) >= 6):
            if(self.email[0].isdigit()):
                print("Invalid email")
            else:
                if('@' in self.email) and (self.email.count('@') == 1):
                    if((self.email[-3] == '.') ^ (self.email[-4] == '.')):
                         for i in self.email:
                            if i == " ":
                                print("Invalid email")
                                return  
                            elif not i.islower():
                                print("Inlvalid email")
                                return
                            elif i.isalnum() or i in ["_", "@", "."]:
                                continue  
                            else:
                                print("Invalid email")  
                                return  
                                
                         print("Email is valid")      
                else:
                    print("Invalid email")
        else:
            print("Invalid email")

obj = Email()
obj.Setemail()
obj.chk_email()
