#import the necessary libraries
from PIL import Image
import pytesseract

#create a variable to store the image path
picture_path = r"C:\Users\PAVILION\Downloads/te.jpg"

#create a variable to store the opened image
picture = Image.open(picture_path)

text = pytesseract.image_to_string(picture)
print(text)