# from thresholding import Threshold
from Sorter import Sort 
from ppf import PositionFinder
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import numpy as np 
import cv2
from trytree import *
from testthresh import *
from blueclient import Send
import time




if __name__ == '__main__':
	objectThreshold = Threshold();
	img = objectThreshold.readImage("IMAGENAME");
	# img = img[0:490,0:464]
	# br = objectThreshold.tbr()

	blackmask = objectThreshold.threshold_by_black(img);
	redmask = objectThreshold.threshold_by_red(img);
	yellowmask = objectThreshold.threshold_by_yellow(img);
	pinkmask  = objectThreshold.threshold_by_pink(img)
	whitemask = objectThreshold.threshold_by_white();
	bluemask = objectThreshold.threshold_by_blue(img);
	# imgX = objectThreshold.add_images(bluemask,blackmask,redmask,yellowmask,whitemask);
	# contourimage,referrenceList = objectThreshold.markContours(imgX);
	# print objectThreshold.mainlist

	# s = Send()	
	# path = ['d','s','w','s','a','s','w','s','w','s']
	# for i in path:
	# 	s.sendData(i)
	# 	time.sleep(0.4)


	
	contourImage,referrenceList=objectThreshold.verify();
	# plt.imshow(contourImage)
	
	# plt.show()
	
	# cv2.imshow("Centeroid Image",contourImage);
	# cv2.waitKey();
	# cv2.destroyAllWindows();
	print referrenceList

	"""Now here"""
	# print "here"
	print "Re-arranging the list to map image:\n";
	sortme = Sort();
	sortme.optimize(objectThreshold.mainlist)
	imageMap = sortme.rearrange(objectThreshold.mainlist)
	sortme.findMaxRC();
	# print imageMap
	r,c,positionMatrix = sortme.makeMatrix(imageMap);
	print "positioin matx =",'\n',positionMatrix

	shapelypositionmatrix = [[0 for x in range(c)] for y in range(r)]
	
	for i in range(r):	
		for j in range(c):

			# print positionMatrix[i][j][1][1]
			if(positionMatrix[i][j] is 0):
				shapelypositionmatrix[i][j] = 'N'
				# print positionMatrix[i][j+1][1][1]
			elif((positionMatrix[i][j][1][1] == "L") or (positionMatrix[i][j][1][1] == "R") or (positionMatrix[i][j][1][1] == "U") or (positionMatrix[i][j][1][1] == "D")):
				shapelypositionmatrix[i][j] = positionMatrix[i][j][1][1]

			elif(positionMatrix[i][j][1][1] == 'S'):
				if(positionMatrix[i][j][1][0] == 'Black'):
					shapelypositionmatrix[i][j] = 'S'
				elif(positionMatrix[i][j][1][0] == 'Blue'):
					shapelypositionmatrix[i][j] = 'S'
				elif(positionMatrix[i][j][1][0] =='White'):
					shapelypositionmatrix[i][j] = 'S'
				elif(positionMatrix[i][j][1][0] =='Red'):
					shapelypositionmatrix[i][j] = 'N'

			elif(positionMatrix[i][j][1][1] == 'Q'):
				shapelypositionmatrix[i][j] = positionMatrix[i][j][1][1]
		
			
			elif(positionMatrix[i][j][1][1] == "START"):
				shapelypositionmatrix[i][j] = "START"
			elif(positionMatrix[i][j][1][1] == "END"):
				shapelypositionmatrix[i][j] = "END"
			else:
				shapelypositionmatrix[i][j] = 'N'
				pass;

	shapelypositionmatrix[2][0] = "N"
	print "Final Image Mapped Matrix";
	for i in range(r):
		for j in range(c):
			print shapelypositionmatrix[i][j] , 
			if(j is (5)):
				print '\n'
		print '\n'

	

	# shapelypositionmatrix[0]=[]
	# shapelypositionmatrix[1]=[]
	# shapelypositionmatrix[2]=[]
	# shapelypositionmatrix[3]=[]
	# shapelypositionmatrix[4]=[]
	# shapelypositionmatrix[5]=[]
	
	p=pixy()
	p.makeAM(shapelypositionmatrix,positionMatrix,r,c)

