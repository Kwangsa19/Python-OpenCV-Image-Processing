import cv2

def blur(image):
    kernels = [3, 5, 9, 13]
    for idx, k in enumerate(kernels):
        image_bl = cv2.blur(image, ksize= (k,k))
        cv2.imshow(str(k), image_bl) # show
        cv2.waitKey(0) # show and wait until we close it
    return
    
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
# hide this cv2.imshow('Resized image', new_image)
# hide this cv2.waitKey(0)
blur(new_image)