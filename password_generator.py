import random 

class PasswordManager:

    def Gen_Password(self):
        self.random_passowrd = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY9876543Z0123456789!@#$%^&*")
        return self.random_passowrd

    def get_random_paaswd(self, max_size):
        generated_password  = ""
        for i in range(max_size):
            generated_password += self.Gen_Password()
        return generated_password

size_of_passwd = int(input("Enter Password Length (8-16) for Strong Passowrd : "))
object = PasswordManager()
strong_passowrd = object.get_random_paaswd(size_of_passwd)
print("                              |_______________________|")
print("Your Generated Password is :  | ", strong_passowrd.center(18),"  |")
print("                              |-----------------------|")

