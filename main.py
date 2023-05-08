from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
folder_path = 'C:/Users/nepal_1681bji/OneDrive/Desktop/pythonpro/rough'
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
# Read the Excel file containing the names
df = pd.read_excel("C:/Users/nepal_1681bji/OneDrive/Desktop/pythonpro/vg.xlsx")

# Convert the names to upper case
df["Name"] = df["Name"].str.upper()

# Open the PSD file
im = Image.open("C:/Users/nepal_1681bji/OneDrive/Desktop/pythonpro/volleyballrunner.psd")

# Create a draw object
draw = ImageDraw.Draw(im)

# Specify the font and font size to be used
font = ImageFont.truetype("swiss.ttf", 150)

# Iterate over the names in the Excel file
for index, row in df.iterrows():
    # Get the size of the text
    text_width, text_height = draw.textsize(row["Name"], font=font)

    # Calculate the center position of the text
    x = (im.width - text_width) / 2
    y = (im.height - text_height) / 2.25
    
    # Insert the name into the PSD file
    draw.text((x, y), row["Name"], fill='#c92812', font=font)
    # Save the PSD file with the inserted name as a PNG file
    im.save(f"{folder_path}/{row['Name']}.png")
    # re-open the PSD file
    im = Image.open("C:/Users/nepal_1681bji/OneDrive/Desktop/pythonpro/volleyballrunner.psd")
    draw = ImageDraw.Draw(im)
