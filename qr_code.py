
import qrcode

class Myqr:

    def makeQr(self):
        # Get the link from the user
        self.qr_link = input("Enter Your Link to Generate QR Code: ")

        # Generate the QR code with custom settings
        self.qr_img = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5,
            error_correction=qrcode.constants.ERROR_CORRECT_M
        )

        self.qr_img.add_data(self.qr_link)
        self.qr_img.make(fit=True)

        # Create a black and white QR code
        self.qr_img = self.qr_img.make_image(
            fill_color="black",
            back_color="white"
        )


    def fetchQr(self):
        # Save the QR code as an image
        self.qr_img.save("qr.png")

        print("QR Code generated successfully!")

obj = Myqr()
obj.makeQr()
obj.fetchQr()
