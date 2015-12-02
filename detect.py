#thanks to http://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
#sudo apt-get install python-numpy
#sudo apt-get install libopencv-dev python-opencv
#wavelength of atomic oxygen emissions in aurora is 558nm, which is rgb189,255,0 (or #bdff00)
#test aurora image has rgb177,166,13

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries - BGR (NOT RGB!!!)
boundaries = [
	([0,180,0], [255,255,255]),
	([0,150,0], [200,255,200])
]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
	
	
