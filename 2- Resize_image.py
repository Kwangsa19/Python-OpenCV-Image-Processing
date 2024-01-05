import cv2

def resize(fname, width, height):
    image = cv2.imread(fname) # loads an image
    cv2.imshow('Original Image', image) # show the image 
    cv2.waitKey(0) # show and wait until we close it
    org_height, org_width = image.shape[0:2]
    print("width: ", org_width)
    print("height: ", org_height)

    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))
    
    return fname, new_image
filename, new_image = resize('bird.jpg', 800, 800)
cv2.imshow('Resized image', new_image)
cv2.waitKey(0)
