from pywhatkit import image_to_ascii_art 
from ascii_magic import AsciiArt 

class AsciiImg:

    def getImgae(self):
        self.image = input("Enter Your Image Path for (ASCII Conversion) : ")

    def img_to_ascii(self):

        self.choice = int(input("Enter 1 for black-white, 2 for colourful art : \n"))

        if(self.choice == 1):
            try:
                image_to_ascii_art(self.image, "ascii_art")
            except FileNotFoundError:
                print("Chk File or rename Your file Image") # Fixed: Removed 'raise' before print
        elif(self.choice == 2):
            try:
                my_art = AsciiArt.from_image(self.image)
                
                # FIX: Use keyword arguments 'columns' instead of positional arguments
                my_art.to_file("ascii_art.txt", columns=100)
            except FileNotFoundError:
                print("Chk File or rename Your file Image") # Fixed: Removed 'raise' before print
        else:
            print("Invalid Option")

obj = AsciiImg()
obj.getImgae()
obj.img_to_ascii()
