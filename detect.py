#thanks to http://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
#sudo apt-get install python-numpy
#sudo apt-get install libopencv-dev python-opencv
#wavelength of atomic oxygen emissions in aurora is 558nm, which is rgb189,255,0 (or #bdff00)
#test aurora image has rgb177,166,13

# import the necessary packages
import numpy as np
#import argparse
import cv2

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
#args = vars(ap.parse_args())
 
# load the image
imagenames = ["test0","test1","test2","test3","test4","test5","test6","test7","test8","test9","test10","testnone1","testnone2","testnone3","testnone4"]
for (imagename) in imagenames:
	image = cv2.imread(imagename + ".jpg")

	#Split into rgb channels for easier manipulation (until I sussout the matrix functions more!)	
	b,g,r = cv2.split(image)

	#Create a mask where green and one other colour only are almost 1:1
	r1 = r * 1.0
	g1 = g * 1.0
	b1 = b * 1.0
	#green:blue        
	gbratio = cv2.divide(b1,g1)
        maskgbratio = cv2.inRange(gbratio,0.7,1.3)
        #green:red
        grratio = cv2.divide(r1,g1)
        maskgrratio = cv2.inRange(grratio,0.7,1.3)
	#only g/r or g/b should be near 1, if both then it is whitish, which we don't want
#	maskgreenish = cv2.bitwise_xor(maskgrratio,maskgbratio)

	#Create a mask for pixels that are green dominant
        #ADJUST THIS SO THAT IT IS MORE THAN JUST SLIGHTLY GREEN DOMINANT, BUT IS DEFINATELY A GOOD BIT HIGHER THAN THE OTHERS
	mask1 = cv2.compare(g,b,cv2.CMP_GT)
	mask2 = cv2.compare(g,r,cv2.CMP_GT)
	maskgreendominant = cv2.bitwise_and(mask1, mask2)
	verygreen = cv2.bitwise_and(maskgreendominant,cv2.bitwise_not(cv2.bitwise_and(maskgrratio,maskgbratio)))

	#Combine green dominant and greenish masks
#	colourmask = cv2.bitwise_or(verygreen, maskgreenish)
	
	#Create a mask that sets an intensity threshold
	total = cv2.add(cv2.add(r,g),b)
	intensitymask = cv2.inRange(total,200,765)
	
	#Combine colour and intensity masks
	finalmask = cv2.bitwise_and(verygreen, intensitymask)

	output = cv2.bitwise_and(image, image, mask = finalmask)
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)


