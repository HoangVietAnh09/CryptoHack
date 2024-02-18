from PIL import Image, ImageChops
im1 = Image.open('C:\\Users\\Admin\\Downloads\\lemur.png')
im2 = Image.open('C:\\Users\\Admin\\Downloads\\flag.png')

im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))
im3.show()
