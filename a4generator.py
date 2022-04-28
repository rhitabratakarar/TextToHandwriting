from PIL import Image

DIMENSIONS = (2480, 3508)
COLOR = "white"
a4= Image.new("RGB", DIMENSIONS, COLOR)
a4.save("a4.jpg")
