import getpass
from pypdf import PdfReader, PdfWriter

class PDF: 

    def get_pdf(self):
        self.pdfile = input("Enter Name of Your PDF FILE : ")

    def encryption(self):
        self.passwd = getpass.getpass(prompt="Enter Paassword to Encrypt PDF FILE : ", echo_char="*")
        self.verify_passwd = getpass.getpass(prompt="Verify Password : ", echo_char="*")
        if( self.passwd == self.verify_passwd):
            self.reader = PdfReader(self.pdfile)
            self.writer = PdfWriter(clone_from=self.reader)
            self.writer.encrypt(self.passwd, algorithm="AES-256")
            self.writer.write("encrypted_" + self.pdfile)
        else: 
            print("failed to verify the password")

    def decryption(self):
        self.reader = PdfReader(self.pdfile)
        self.password_for_decrypting = input("Enter Password For Decrypting PDF FILE : ")
        if self.reader.is_encrypted:
            self.reader.decrypt(self.password_for_decrypting)
        else: 
            print("Invalid Password ")

        self.writer = PdfWriter(clone_from=self.reader)
        self.writer.write("decrypted_" + self.pdfile)

    def get_choice(self):
        self.choice = int(input("Choose Your Choice : \n\n1. For PDF ENCRYPTION\n2. For PDF DECRYPTION\nChoice : "))
        return self.choice


    def chk_choice(self):

        if (self.choice == 1):
            self.encryption()
        elif(self.choice == 2):
            self.decryption()
        else:
            print("Invalid Choice")


obj = PDF()

obj.get_pdf()
obj.get_choice()
obj.chk_choice()
