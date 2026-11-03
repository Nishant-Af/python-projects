import os
from PIL import Image, ImageDraw, ImageFont

class TextToHandWriting:

    def GetData(self):
        # Prompt user to input the file name or path
        file = input("Enter File Name or Absolute Path of Your File : ")
        
        # Using a 'with' block ensures the file safely closes on your computer after reading
        with open(file, "r", encoding="utf-8") as handle:
            self.data = handle.read()

    def ConvertTextToWriting(self):
        try:
            # 1. Image Settings
            image_width = 1200
            image_height = 1600
            background_color = (255, 255, 255)  # White background
            text_color = (0, 15, 85)            # Dark blue ink
            
            # Create a blank image canvas
            image = Image.new("RGB", (image_width, image_height), color=background_color)
            draw = ImageDraw.Draw(image)
            
            # 2. Font Selection (Attempts Ubuntu or cursive fonts sequentially)
            font_size = 28
            font_paths = [
                "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",                   # Ubuntu Standard (Linux)
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",                # DejaVu (Linux alternative)
                "C:\\Windows\\Fonts\\segoesc.ttf",                                 # Segoe Script (Windows cursive)
                "C:\\Windows\\Fonts\\ubuntu.ttf",                                  # Ubuntu (Windows if installed)
                "/System/Library/Fonts/Supplemental/Comic Sans MS.ttf"            # Comic Sans (macOS alternative)
            ]
            
            font = None
            for path in font_paths:
                if os.path.exists(path):
                    font = ImageFont.truetype(path, font_size)
                    break
            
            if font is None:
                print("Custom font not found. Using default system font.")
                font = ImageFont.load_default()

            # 3. Draw Text with Margins and Line Spacing
            margin_x = 60
            margin_y = 60
            line_spacing = 15
            
            # Split the text into lines and render them
            lines = self.data.split('\n')
            current_y = margin_y
            
            for line in lines:
                # Use draw.textlen or getbbox to prevent text overflowing (optional enhancement)
                draw.text((margin_x, current_y), line, fill=text_color, font=font)
                
                # Dynamic line height calculation based on font size
                if hasattr(font, 'getbbox'):
                    bbox = font.getbbox(line if line else "A")
                    line_height = (bbox[3] - bbox[1]) + line_spacing
                else:
                    line_height = font_size + line_spacing
                    
                current_y += line_height
                
                # Prevent crashing if text is longer than the page height
                if current_y > image_height - margin_y:
                    print("Warning: Text was truncated because it exceeded the page height.")
                    break

            # 4. Save the Final Output
            output_name = "handwritten_output.png"
            image.save(output_name)
            print(f"Success! The text has been converted locally to '{output_name}'.")
            
        except Exception as e:
            print(f"\nProcessing Error: Failed to generate handwritten image.")
            print(f"Details: {e}")

# Initialize the class object
object = TextToHandWriting()

# Fetch data from the user's text file
object.GetData()

# Execute the handwriting conversion
object.ConvertTextToWriting()
