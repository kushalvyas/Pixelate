#  modules
import numpy as np 
import cv2
from ppf import PositionFinder
import copy
import yaml



class Threshold(object):
	"""docstring to be added"""
	def __init__(self):
		self.kernel = np.ones((1,1),np.uint8) # marks a unit martix for white - denoising
		self.ret = True;
		self.img = None;
		self.triangle_list=[];
		self.red_square_list=[];
		self.quad_list=[];
		self.black_square_list=[];
		self.blue_square_list=[];
		self.white_square_list=[];
		self.start_list=[];
		self.end_list=[];
		self.mainlist=[];
		self.ppfobject = PositionFinder();
		self.f = open("values.yaml")
		self.data =yaml.safe_load(self.f)
		self.f.close()
		self.r01 =  self.data['r01'];self.r02 =  self.data['r02'];
		self.g01 =  self.data['g01'];self.g02 =  self.data['g02'];
		self.b01 =  self.data['b01'];self.b02 =  self.data['b02'];

		self.r11 =  self.data['r11'];self.r12 =  self.data['r12'];
		self.g11 =  self.data['g11'];self.g12 =  self.data['g12'];
		self.b11 =  self.data['b11'];self.b12 =  self.data['b12'];
		
		self.r21 =  self.data['r21'];self.r22 =  self.data['r22'];
		self.g21 =  self.data['g21'];self.g22 =  self.data['g22'];
		self.b21 =  self.data['b21'];self.b22 =  self.data['b22'];
		
		self.r31 =  self.data['r31'];self.r32 =  self.data['r32'];
		self.g31 =  self.data['g31'];self.g32 =  self.data['g32'];
		self.b31 =  self.data['b31'];self.b32 =  self.data['b32'];

		self.r41 =  self.data['r41'];self.r42 =  self.data['r42'];
		self.g41 =  self.data['g41'];self.g42 =  self.data['g42'];
		self.b41 =  self.data['b41'];self.b42 =  self.data['b42'];

		self.r51 =  self.data['r51'];self.r52 =  self.data['r52'];
		self.g51 =  self.data['g51'];self.g52 =  self.data['g52'];
		self.b51 =  self.data['b51'];self.b52 =  self.data['b52'];



		self.deltamodulation = 1900;


	def readImage(self,imagename):
		# print 'Reading Image'
		img = cv2.imread(imagename);
		self.img = img;
		img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV);
		return img



	def threshold_by_blue(self,imhsv):
		print "here in blue threshold"
		kernel = np.ones((2,2),np.uint8)
		kernel1 = np.ones((2,2),np.uint8)
		# lower_blue = np.array([120, 111,  105], dtype=np.uint8);
		# upper_blue = np.array([155,255,255], dtype=np.uint8);
		lower_blue = np.array([self.b21,self.g21,self.r21],dtype=np.uint8);
		upper_blue = np.array([self.b22,self.g22,self.r22],dtype=np.uint8);
		print lower_blue,upper_blue
		# cv2.imshow()
		bluemask = cv2.inRange(imhsv, lower_blue, upper_blue);
		# cv2.imshow("sfd",bluemask)
		# cv2.waitKey()
		bluemask = cv2.morphologyEx(bluemask,cv2.MORPH_OPEN,kernel) # morphs the image as per the matrix
		# print 'Writing Blue Image';
		cv2.imwrite("images/blue.png",bluemask);
		# thresh = bluemask
		contours,heir = cv2.findContours(bluemask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) 
		for cnt in contours:
			cnt = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True) # approximates the contours into 3 and 4
			if len(cnt) == 4 :
				print "kjnjknfkjznfkjsfn"
				moments = cv2.moments(cnt);
				cv2.drawContours(self.img,[cnt],0,(255,255,255),1)
				print len(cnt)
				# marks the center coordinates 
				if moments['m00']!=0:
					# cx and cy are centroids of the respective shapes
					cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
					cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
					# cv2.drawContours(self.img,[cnt],0,(255,255,255),1) ; 
					# cv2.circle(self.img,(cx,cy),5,(127,127,127),-1) ;    # marks centroid with red color
					self.blue_square_list.append(((cx,cy),("Blue","S")));
					self.mainlist.append(([cx,cy],["Blue","S"]));
					print "yesss"
				else:
					print "Error in blue"
			else:
				print "Error in blue"
		return bluemask;

	def tbr(self):
		imgb = cv2.imread('test.png',0);
		# imgw = imgw[0:490,0:464]
		kernel = np.ones((3,3),np.uint8)
		__,imgw = cv2.threshold(imgw,240,255,0)
		imgw = cv2.morphologyEx(imgw,cv2.MORPH_OPEN,kernel);
		# print 'Writing black Image';
		cv2.imwrite("images/black.png",imgw);
		thresh = imgw;
		contours,heir = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) 
		for cnt in contours:
			cnt = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True) # approximates the contours into 3 and 4
			if len(cnt) == 4 :
				moments = cv2.moments(cnt);
				cv2.drawContours(self.img,[cnt],0,(255,255,255),1)
				print len(cnt)
				# marks the center coordinates 
				if moments['m00']!=0:
					# cx and cy are centroids of the respective shapes
					cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
					cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
					# cv2.drawContours(self.img,[cnt],0,(255,255,255),1) ; 
					# cv2.circle(self.img,(cx,cy),5,(127,127,127),-1) ;    # marks centroid with red color
				
					# if len(cnt) ==4 :
					self.black_square_list.append(((cx,cy),("Black","S")));
					self.mainlist.append(([cx,cy],["Black","S"]));
			else:
				print "Error in white"
		return imgb

	def threshold_by_black(self,imhsv):

		kernel = np.ones((5,5),np.uint8)
		kernel1 = np.ones((4,4),np.uint8)
		# lower_black = np.array([0,0,0],dtype=np.uint8);
		# upper_black = np.array([200, 255, 50],dtype=np.uint8);
		lower_black = np.array([self.b11,self.g11,self.r11],dtype=np.uint8);
		upper_black = np.array([self.b12,self.g12,self.r12],dtype=np.uint8);

		blackmask = cv2.inRange(imhsv, lower_black, upper_black);
		blackmask = cv2.bitwise_not(blackmask)
		# blackmask = cv2.morphologyEx(blackmask,cv2.MORPH_OPEN,kernel);
		# blackmask = cv2.dilate(blackmask,kernel1,iterations = 2)
		blacknask = cv2.erode(blackmask,kernel,iterations = 4)
		
		blackmask = cv2.morphologyEx(blackmask,cv2.MORPH_OPEN,kernel) ;# morphs the image as per the matrix
		blackmask = cv2.dilate(blackmask,kernel1,iterations = 3)
		# print 'Writing Black Image';
		
		cv2.imwrite("images/black.png",blackmask);
		thresh = blackmask

		contours,heir = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) 
		areaList=[];
		for cnt in contours:
			cnt = cv2.convexHull(cnt)
			cnt = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True) # approximates the contours into 3 and 4
			if len(cnt) == 3 :
				moments = cv2.moments(cnt);
				cv2.drawContours(self.img,[cnt],0,(255,255,255),1)
				print len(cnt)
				# marks the center coordinates 
				if moments['m00']!=0:
					# cx and cy are centroids of the respective shapes
					cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
					cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
					# cv2.drawContours(self.img,[cnt],0,(255,255,255),1) ; 
					# cv2.circle(self.img,(cx,cy),5,(127,127,127),-1) ;    # marks centroid with red color
					# for triangle
					cv2.circle(self.img,(cx,cy),5,(255,255,255),-1)

					direction = self.ppfobject.triangle_points(cnt);
					self.triangle_list.append(((cx,cy),("Black",direction)));
					self.mainlist.append(([cx,cy],["Black",direction]));
		
			elif len(cnt) >= 4:
				moments = cv2.moments(cnt)
				if moments['m00']!=0:
					# cx and cy are centroids of the respective shapes
					cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
					cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
				# cnt = cv2.convexHull(cnt)
					area = cv2.contourArea(cnt)
					areaList.append(area)
					# temporary approach
					cv2.circle(self.img,(cx,cy),5,(255,255,255),-1)

					if area >= self.deltamodulation:
						self.quad_list.append(([cx,cy],["Black","Q"]));
						self.mainlist.append(([cx,cy],["Black","Q"]));
					else:
						self.black_square_list.append(([cx,cy],["Black","S"]));
						self.mainlist.append(([cx,cy],["Black","S"]))

					cv2.drawContours(self.img,[cnt],0,(0,255,255),1)
					pass;
			else:
				print "Error in Black"	
		# segregating into square and quad
		areaList.sort()
		print areaList

		return blackmask;


	def threshold_by_white(self):
		imgw = cv2.imread('test.png',0);
		# imgw = imgw[0:490,0:464]
		kernel = np.ones((3,3),np.uint8)
		__,imgw = cv2.threshold(imgw,200,255,0)
		imgw = cv2.morphologyEx(imgw,cv2.MORPH_OPEN,kernel);
		# print 'Writing White Image';
		cv2.imwrite("images/white.png",imgw);
		thresh = imgw;
		contours,heir = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) 
		for cnt in contours:
			cnt = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True) # approximates the contours into 3 and 4
			if len(cnt) == 4 :
				moments = cv2.moments(cnt);
				cv2.drawContours(self.img,[cnt],0,(255,255,255),1)
				print len(cnt)
				# marks the center coordinates 
				if moments['m00']!=0:
					# cx and cy are centroids of the respective shapes
					cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
					cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
					# cv2.drawContours(self.img,[cnt],0,(255,255,255),1) ; 
					# cv2.circle(self.img,(cx,cy),5,(127,127,127),-1) ;    # marks centroid with red color
				
					# if len(cnt) ==4 :
					self.white_square_list.append(((cx,cy),("White","S")));
					self.mainlist.append(([cx,cy],["White","S"]));
			else:
				print "Error in white"
		return imgw

	def threshold_by_red(self,imhsv):
		kernel = np.ones((5,5),np.uint8)
		kernel1 = np.ones((5,5),np.uint8)
		# lower_red = np.array([0,160,120],dtype=np.uint8);
		# upper_red = np.array([10,255,255],dtype=np.uint8);
		lower_red = np.array([self.b01,self.g01,self.r01],dtype=np.uint8);
		upper_red = np.array([self.b02,self.g02,self.r02],dtype=np.uint8);
		redmask = cv2.inRange(imhsv, lower_red, upper_red);

		rednask = cv2.erode(redmask,kernel,iterations = 1)
		redmask = cv2.morphologyEx(redmask,cv2.MORPH_OPEN,kernel);
		redmask = cv2.dilate(redmask,kernel1,iterations = 6)
		# print 'Writing Red Image';
		cv2.imwrite("images/red.png",redmask);
		thresh = redmask;
		contours,heir = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) 
		for cnt in contours:
			cnt = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True) # approximates the contours into 3 and 4
			if len(cnt) == 4 :
				moments = cv2.moments(cnt);
				cv2.drawContours(self.img,[cnt],0,(255,255,255),1)
				print len(cnt)
				# marks the center coordinates 
				if moments['m00']!=0:
					# cx and cy are centroids of the respective shapes
					cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
					cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
					# cv2.drawContours(self.img,[cnt],0,(255,255,255),1) ; 
					# cv2.circle(self.img,(cx,cy),5,(127,127,127),-1) ;    # marks centroid with red color
					
					self.red_square_list.append(((cx,cy),("Red","N"))); 
					self.mainlist.append(([cx,cy],["Red","N"]));
					# cv2.circle(self.img,(cx,cy),5,(255,255,255),-1)
			else:
				print "Error in Red detection"
				pass;
				
		return redmask

	def threshold_by_yellow(self,imhsv):
		kernel = np.ones((5,5),np.uint8)
		kernel1 = np.ones((2,2),np.uint8)
		#  to do yellowe colde here
		# lower_yellow  = np.array([140,255,255],dtype = np.uint8);
		# upper_yellow  = np.array([160,255,255],dtype = np.uint8);
		lower_yellow = np.array([self.b41,self.g41,self.r41],dtype=np.uint8);
		upper_yellow = np.array([self.b42,self.g42,self.r42],dtype=np.uint8);

		yellowmask = cv2.inRange(imhsv, lower_yellow, upper_yellow);
		yellowmask = cv2.morphologyEx(yellowmask,cv2.MORPH_OPEN,kernel);
		cv2.imwrite("images/yellow.png",yellowmask)
		thresh = yellowmask
		contours,heir = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) 
		for cnt in contours:
			cnt = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True) # approximates the contours into 3 and 4
			if len(cnt) ==4 :
				moments = cv2.moments(cnt);
				cv2.drawContours(self.img,[cnt],0,(255,255,255),1)
				print len(cnt)
				# marks the center coordinates 
				if moments['m00']!=0:
					# cx and cy are centroids of the respective shapes
					cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
					cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
					# cv2.drawContours(self.img,[cnt],0,(255,255,255),1) ; 
					# cv2.circle(self.img,(cx,cy),5,(127,127,127),-1) ;    # marks centroid with red color
					if len(cnt) == 4:
						self.start_list.append(([cx,cy],["END","END"]))
						self.mainlist.append(([cx,cy],["END","END"]))
					else:
						print "Error in detection of Start and End"
				
		return yellowmask

	def threshold_by_pink(self,imhsv):
		kernel = np.ones((3,3),np.uint8)
		kernel1 = np.ones((2,2),np.uint8)
		# do yellow thresholding here
		# lower_pink  = np.array([32,255,239],dtype = np.uint8);
		# upper_pink  = np.array([42,255,255],dtype = np.uint8);
		cx,cy=0,0
		lower_pink = np.array([self.b51,self.g51,self.r51],dtype=np.uint8);
		upper_pink = np.array([self.b52,self.g52,self.r52],dtype=np.uint8);
		pinkmask = cv2.inRange(imhsv, lower_pink, upper_pink);
		pinkmask = cv2.erode(pinkmask , kernel1,iterations=1)
		cv2.imwrite("images/pink.png",pinkmask)
		# pinkmask = cv2.morphologyEx(pinkmask,cv2.MORPH_OPEN,kernel);
		pinkmask = cv2.dilate(pinkmask , kernel1,iterations=3)
		contours , hier = cv2.findContours(pinkmask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contours:
			cnt = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True) # approximates the contours into 3 and 4
			if len(cnt) :
				moments = cv2.moments(cnt);
				cv2.drawContours(self.img,[cnt],0,(255,255,255),1)
				print len(cnt)
				# marks the center coordinates 
				if moments['m00']!=0:
					# cx and cy are centroids of the respective shapes
					cx = int(moments['m10']/moments['m00'])         # cx = M10/M00
					cy = int(moments['m01']/moments['m00'])         # cy = M01/M00
					# cv2.drawContours(self.img,[cnt],0,(255,255,255),1) ; 
					# cv2.circle(self.img,(cx,cy),5,(127,127,127),-1) ;    # marks centroid with red color
					if len(cnt) :
						self.start_list.append(([cx,cy],["START","START"]))
						self.mainlist.append(([cx,cy],["START","START"]))
					else:
						print "Error in detection of Start and End"
		
		return pinkmask


	# append start for pink detection

						# elif (((self.img[cy][cx][0]>=self.b11)and (self.img[cy][cx][0]<=self.b12)) and ((self.img[cy][cx][1]>=self.g11)and(self.img[cy][cx][1]<=self.g12))and((self.img[cy][cx][2]>=self.r11)and(self.img[cy][cx][2]<=self.r12))):
						# 	if ((((self.img[cy+delta][cx][0]>=self.b11)and (self.img[cy+delta][cx][0]<=self.b12)) and ((self.img[cy+delta][cx][1]>=self.g11)and(self.img[cy+delta][cx][1]<=self.g12))and((self.img[cy+delta][cx][2]>=self.r11)and(self.img[cy+delta][cx][2]<=self.r12)))and ((self.img[cy-delta][cx][0]>=self.b11)and (self.img[cy-delta][cx][0]<=self.b12)) and ((self.img[cy-delta][cx][1]>=self.g11)and(self.img[cy-delta][cx][1]<=self.g12))and((self.img[cy-delta][cx][2]>=self.r11)and(self.img[cy-delta][cx][2]<=self.r12))):
						# 		self.quad_list.append(([cx,cy],["Black","Q"]));
						# 		self.mainlist.append(([cx,cy],["Black","Q"]));
						# 		cv2.circle(self.img,(cx,cy),5,(255,255,0),-1);
						# 	else:
						# 		self.black_square_list.append(([cx,cy],["Black","S"]));
						# 		self.mainlist.append(([cx,cy],["Black","S"]))
						# 		cv2.circle(self.img,(cx,cy),5,(255,0,255),-1);


	def verify(self):
	

		print "Black Square =>",len(self.black_square_list),'\n'
		print "Blue Square =>",len(self.blue_square_list),'\n'
		print "Red Square =>",len(self.red_square_list),'\n'
		print "Quad =>",len(self.quad_list),'\n'
		print "White Square=>",len(self.white_square_list),'\n'
		print "Triangle=>",len(self.triangle_list),'\n'
		print "Start=>",len(self.start_list),'\n'
		print "End =>",len(self.end_list),'\n',
		# print self.start_list
		print self.start_list
		# cv2.imshow("asd",self.img)
		# cv2.waitKey()
		self.referrenceList = copy.copy(self.mainlist)
		print self.referrenceList
		return 	self.img,self.referrenceList


	



