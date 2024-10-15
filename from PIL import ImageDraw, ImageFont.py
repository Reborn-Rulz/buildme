from PIL import ImageDraw, ImageFont

# Load the image again to make modifications
image = Image.open(image_path)
draw = ImageDraw.Draw(image)

# Define the text and its positioning (as close as possible to original)
new_text = "FACADE"

# Placeholder font path and size (real font and size should match original)
# I'll use a default font as a placeholder since the specific font is not provided.
try:
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Default font
    font = ImageFont.truetype(font_path, 110)  # Example font size to match original as closely as possible
except IOError:
    font = ImageFont.load_default()

# Determine the position of the original "BORDER" text, and replace it with "FACADE"
# Estimating the coordinates for the new text to align well
text_position = (510, 260)  # Coordinates from observation, adjust based on final look

# Set the text color to match the original white-ish color
text_color = (255, 255, 255)

# Draw the new text "FACADE"
draw.text(text_position, new_text, font=font, fill=text_color)

# Save the modified image
edited_image_path = "/mnt/data/Blindfold_Facade.png"
image.save(edited_image_path)

# Display the new image
image.show()

# Return the path to the new image for download
edited_image_path
