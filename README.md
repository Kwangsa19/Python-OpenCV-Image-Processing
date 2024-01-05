# Python-OpenCV-Image-Processing

> This project is based on Coursera Project Course ("OpenCV Image Processing"). Please enroll to this course by visiting this [link](https://www.coursera.org/projects/image-processing-with-python). The file name starts with numerical value 1-5.
> For your convenience, I divided the tasks into 5 different files. 
## Description

This project will produce the following outputs: 
* Read Image
* Resize Image
* Blur Image
* Sharpen Image
* Batch Process Images

Please make sure you have installed the following modules: 
* opencv
* numpy
* os
* fnmatch
  
## Implementation 

* 1 - Read Image: This code will show the original file of "bird.jpg".
```
  def resize(fname, width, height):
    image = cv2.imread(fname) # Loads an image.
    cv2.imshow('Original Image', image) # Show the image. 
    cv2.waitKey(0) # Show and wait until we close it.
  resize('bird.jpg', 600, 600) # Still the original version first. 
```
![python_CnWvvVuZku](https://github.com/Kwangsa19/Python-OpenCV-Image-Processing/assets/135963482/50d93b3b-04ad-4381-844f-91d5552dec3f)

 * 2 - Resize Image: This code will produce two outputs: The original file of "bird.jpg" and the resized version of "bird.jpg". 
```
def resize(fname, width, height):
    image = cv2.imread(fname) # Loads an image.
    cv2.imshow('Original Image', image) # Show the image titled original image. 
    cv2.waitKey(0) # Show and wait until we close it.
    # Retrieves the original height and width of the image using its shape attribute, which provides a tuple of dimensions
    # (height, width, channels).

    org_height, org_width = image.shape[0:2] 
    print("width: ", org_width)
    print("height: ", org_height)

    # Checks if the image is wider than or equal to its height.
    if org_width >= org_height:
    # If wider or equal, resize the image to the specified width and heigth (openCV resize function), maintaining aspect ratio.
        new_image = cv2.resize(image, (width, height)) 
    else:
    # Resizes the image, swapping the order of width and height to ensure correct resizing while preserving aspect ratio.
        new_image = cv2.resize(image, (height, width)) 
    
    return fname, new_image
filename, new_image = resize('bird.jpg', 800, 800) # New resized version.
cv2.imshow('Resized image', new_image)
cv2.waitKey(0) # Show and wait until we close it.
```
![python_CnWvvVuZku](https://github.com/Kwangsa19/Python-OpenCV-Image-Processing/assets/135963482/50d93b3b-04ad-4381-844f-91d5552dec3f)
![python_y1u29Hh6mu](https://github.com/Kwangsa19/Python-OpenCV-Image-Processing/assets/135963482/4824003c-f9d8-4260-85cf-5f5b1e82842c)

* 3 - Blur image: Show the original image of "bird.jpg" and blurred version of it as many as 5 times in a new resized mode. 
```
def blur(image):
  # It will produce 5 results. The bigger the kernel, the stronger blur effects.
  # Add or reduce to adjust the number of blurry outputs. 
    kernels = [3, 5, 9, 13] 
    for idx, k in enumerate(kernels):
    # Applies a box blur to the input image using the current kernel size (k).
    # Box blur is a simple averaging technique for smoothing images.
        image_bl = cv2.blur(image, ksize= (k,k)) 
        cv2.imshow(str(k), image_bl) # Show.
        cv2.waitKey(0) # Show and wait until we close it.
    return
    
def resize(fname, width, height):
    image = cv2.imread(fname) # Loads an image.
    cv2.imshow('Original Image', image) # Show the image. 
    cv2.waitKey(0) # Show and wait until we close it.
    org_height, org_width = image.shape[0:2]
    print("width: ", org_width)
    print("height: ", org_height)

    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))
    
    return fname, new_image
filename, new_image = resize('bird.jpg', 800, 800)
blur(new_image)
```
![python_CnWvvVuZku](https://github.com/Kwangsa19/Python-OpenCV-Image-Processing/assets/135963482/50d93b3b-04ad-4381-844f-91d5552dec3f)
![python_WNynD3Ovdm](https://github.com/Kwangsa19/Python-OpenCV-Image-Processing/assets/135963482/b3b33981-5965-4d51-b6e5-a6aa5d2ee759)
![python_y0Y6t6NdgM](https://github.com/Kwangsa19/Python-OpenCV-Image-Processing/assets/135963482/0d93dc7c-bfd0-4eec-a867-9c534a5f1ccc) <br>
and so on...

* 4 - Sharpen image: Show the original image of "bird.jpg" and sharpened version of it in a new resized mode.
```
import cv2
import numpy as np

def sharpen(image):
    kernel = np.array([[0, -1, 0], [-1,5,-1], [0,-1,0]]) # Creates a 3x3 sharpening kernel using NumPy's array function.
    # This kernel highlights edges and details in the image.
    new_image = cv2.filter2D(image, -1, kernel) # Applies the sharpening filter to the input image using OpenCV's filter2D function:
    cv2.imshow('Sharpened', new_image) # Displays the sharpened image in a window titled "Sharpened".
    cv2.waitKey(0) # Show and wait until we close it.
    return

def resize(fname, width, height):
    image = cv2.imread(fname) # Loads an image.
    cv2.imshow('Original Image', image) # Show the image. 
    cv2.waitKey(0) # Show and wait until we close it.
    org_height, org_width = image.shape[0:2]
    print("width: ", org_width)
    print("height: ", org_height)

    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))
    
    return fname, new_image
filename, new_image = resize('bird.jpg', 800, 800)
image = sharpen(new_image)
```
![python_CnWvvVuZku](https://github.com/Kwangsa19/Python-OpenCV-Image-Processing/assets/135963482/50d93b3b-04ad-4381-844f-91d5552dec3f)
![python_Eq2n6BTj0C](https://github.com/Kwangsa19/Python-OpenCV-Image-Processing/assets/135963482/3430c7cc-dcbb-4750-84f5-6b6bb9a79737)

* 5 - Batch image:
```
def resize(fname, width, height):
    image = cv2.imread(fname) # Loads an image.
    cv2.imshow('Original Image', image) # Show the image. 
    cv2.waitKey(0) # Show and wait until we close it.
    org_height, org_width = image.shape[0:2]
    print("width: ", org_width)
    print("height: ", org_height)

    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))
    
    return fname, new_image

listofFiles =os.listdir('.') # Lists files in the current directory.
pattern = "*.jpg" # Pattern file: JPG.
n = len(sys.argv) # Gets the number of command-line arguments.
if n == 3: # Checks if width and height are provided as arguments.
    # If profided store them as integers.
     # Accesses the second argument (index 1) and converts it to an integer, storing the result in the variable width.
    width = int(sys.argv[1])
    # Accesses the third argument (index 2) and converts it to an integer, storing the result in the variable height.
    height = int(sys.argv[2]) 
else:
    # If not provided, sets default values.
    width = 1280
    height = 960
if not os.path.exists('new folder'): # Checks if a folder named "new_folder" exists.
    os.makedirs('new_folder') # if none, create new_folder folder.

for filename in listofFiles:
    if fnmatch.fnmatch(filename, pattern):
        filename, new_image = resize(filename, width, height) # Calls the resize function to resize the image.
        # Saves the resized image to the new_folder with the same filename. In this case it is 1280 x 960. 
        cv2.imwrite("new_folder\\" + filename, new_image) 
```
If you see in a repository, there's a ***new_folder*** of which all the new images in a new size are stored there.  

## Future Works

* Build the user interface.
* Implement the face detection on the several images and resize those file sizes.
* Consider building the photo apps. 

