from PIL import Image, ImageDraw

# Create a blank image with white background
width, height = 200, 200
image = Image.new('RGB', (width, height), (255, 255, 255))

# Initialize the drawing context
draw = ImageDraw.Draw(image)

# Draw a red rectangle
draw.rectangle([50, 50, 150, 150], fill='red')

# Save the image as a PNG file
image.save('example_image.png')
