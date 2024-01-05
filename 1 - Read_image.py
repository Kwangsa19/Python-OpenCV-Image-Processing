import cv2

def resize(fname, width, height):
    image = cv2.imread(fname) # loads an image
    cv2.imshow('Original Image', image) # show the image 
    cv2.waitKey(0) # show and wait until we close it

resize('bird.jpg', 600, 600)
