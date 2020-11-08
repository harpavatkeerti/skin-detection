from skinDetection import change_skin
import cv2
import numpy as np
import argparse

if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("--img", help="Image to be changed")
	parser.add_argument("--col", help="Required skin color or the OTHER image")
	parser.add_argument("--res", help="Path where image is to be saved")
	args=parser.parse_args()

	with open(args.img,'rb') as inputImage:
	    a=args.col.strip('[] ')
	    b=a.split(',')
	    result=change_skin(inputImage,[int(b[0].strip()),int(b[1].strip()),int(b[2].strip())],args.res)
	with open(args.res,'wb') as resultFile:
		resultFile.write(result)
