from skinDetection import change_skin
import cv2
import numpy as np
import argparse

if __name__ == "__main__":
	parser=argparse.ArgumentParser()
	parser.add_argument("--img", help="Image to be changed")
	parser.add_argument("--race", help="Required skin color race")
	parser.add_argument("--res", help="Path where image is to be saved")
	args=parser.parse_args()

	with open(args.img,'rb') as inputImage:
		if args.race=="Asian":
			b = [200, 170, 125]#b = [180, 103, 71]
		elif args.race=="European":
			b = [210, 199, 184]#b = [220, 209, 194]
		else:
			b = [96, 57, 9]#b = [111, 79, 29]
		result=change_skin(inputImage,b,args.res)
	with open(args.res,'wb') as resultFile:
		resultFile.write(result)
