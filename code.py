from PIL import Image

# opening image1
img2 = Image.open('image2.jpg')

# viewing the original size of image
print(img2.width, img2.height)

# displaying the image
img2.show()

# resize the image with our required inputs
img2 = img2.resize((int(img2.width*20), int(img2.height*60)))

# viewing the resized image width and height
print(img2.width, img2.height)

# displaying the image after resized
# img2.show()
img2.save('resized_image.jpg')
