import pywhatkit as pw

class TextToHandWriting:

    def GetData(self):
        # Prompt user to input the file name or path
        file = input("Enter File Name or Absolute Path of Your File : ")
        
        # FIXED: Using a 'with' block ensures the file safely closes on your computer after reading
        with open(f"{file}", "r") as handle:
            self.data = handle.read()

    def ConvertTextToWriting(self):
        # Try block prevents the program from crashing if PyWhatKit's API server is offline
        try:
            # Call PyWhatKit to convert text and save it as an image
            pw.text_to_handwriting(self.data)
            print("Success! The text has been converted to 'pywhatkit.png'.")
        except Exception as e:
            # Clear error handling if the external PyWhatKit server fails to respond
            print(f"\nAPI Error: PyWhatKit's handwriting server is currently offline or blocking requests.")
            print(f"Details: {e}")


# Initialize the class object
object = TextToHandWriting()

# Fetch data from the user's text file
object.GetData()

# Execute the handwriting conversion
object.ConvertTextToWriting()
