import numpy as np
import argparse
import imutils
import cv2


ap=argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True, help='path of file')
args=vars(ap.parse_args())


image=cv2.imread(args['image'])


 
# loop over the rotation angles again, this time ensuring
# no part of the image is cut off
for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Rotated (Correct)", rotated)
	cv2.waitKey(0)
