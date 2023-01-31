from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
folder_path = 'Names'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
# Read the Excel file containing the names
df = pd.read_excel("Names.xlsx")

# Open the PSD file
im = Image.open("photoshop-file.psd")

# Create a draw object
draw = ImageDraw.Draw(im)

# Specify the font and font size to be used
font = ImageFont.truetype("GreatVibes.ttf", 200)

# Iterate over the names in the Excel file
for index, row in df.iterrows():
    # Get the size of the text
    text_width, text_height = draw.textsize(row["Name"], font=font)

    # Calculate the center position of the text
    x = (im.width - text_width) / 2
    y = (im.height - text_height) / 2.68
    
    # Insert the name into the PSD file
    draw.text((x, y), row["Name"], fill='#404040', font=font)
    # Save the PSD file with the inserted name as a PNG file
    im.save(f"{folder_path}/{row['Name']}.jpg")
    # re-open the PSD file
    im = Image.open("photoshop-file.psd")
    draw = ImageDraw.Draw(im)
