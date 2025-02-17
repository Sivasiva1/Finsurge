from PIL import Image 

img = Image.open("C:\\Users\\ELCOT\\Pictures\\Screenshots\\vi.png")
img.save("compressed.png","PNG",quality = 50) 

