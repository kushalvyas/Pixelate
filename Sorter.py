import copy
import numpy as np 


class Sort(object):
	def __init__(self):
		self.xList=[];
		self.yList = [];
		self.delta=30;
		self.uniList=[];
		self.maxrow=0;
		self.maxcol=0;
		self.newList=[];
		# self.pM=None;

	def optimize(self,l):
	
	# this method will create a approximated value for centroid matrix
		for x in l:
			self.xList.append(x[0][0]);
			self.yList.append(x[0][1]);

		# # print '$$'*100
		# # print '\n\n'
		# # print self.xList,self.yList,'\n\n'
		# # print '$$'*100
		# self.xList = [290,239,289,287,12,324,42,32,286,287,285];
		self.counter = len(self.xList) 
		# self.newList = copy.copy(self.xList)
		# # print hex(id(self.newList)),hex(id(self.xList))
		# self.xList.sort()
		##################################################
				# FRAGMENT TO OPTIMIZE

		# self.xList = list(set(self.xList))
		self.xList.sort()
		print self.xList

		# self.yList = list(set(self.yList))
		self.yList.sort()
		# print self.yList
		for x in range(len(self.xList)-1):
			for y in range(len(self.xList)-1):
				if(abs(self.xList[y]-self.xList[y+1])<=self.delta):
					varx = min(self.xList[y],self.xList[y+1])
					self.xList[y],self.xList[y+1]=varx,varx

		# print self.xList

		for x in range(len(self.yList)-1):
			for y in range(len(self.yList)-1):
				if(abs(self.yList[y]-self.yList[y+1])<=self.delta):
					varx=min(self.yList[y],self.yList[y+1])
					self.yList[y],self.yList[y+1]=varx,varx

		print "Optimized list is \n",self.xList,"\n",self.yList,"\n"


		#################################################
		if (self.counter== len(self.yList)):
			pass;

		else:	
			pass
			# for x in range(len(self.xList)) :
			# 	for y in range(len(self.xList)-1):
			# 		if(abs(self.xList[y]-self.xList[y+1])<=self.delta):
			# 			self.xList[y]=self.xList[y+1] = min(self.xList[y],self.xList[y+1]);
			# for x in range(len(self.yList)) :
			# 	for y in range(len(self.yList)-1):
			# 		if(abs(self.yList[y]-self.yList[y+1])<=self.delta):
			# 			self.yList[y]=self.yList[y+1] = min(self.yList[y],self.yList[y+1]);

		# # print '*'*50,'\n',self.xList,'\n\n',self.yList;
		# self.uniList = list(zip(self.xList,self.yList))
		# self.uniList.sort(key=lambda x:(x[1],x[0]))
		# # print 'Sorted Universal List';
		# # print self.uniList;

	def rearrange(self,l):

		# for sorting the list in the 2D way
		print "length of list is ",len(l);
		for x in range(len(l)):
			for y in range(len(self.xList)):
				if(abs(l[x][0][0]-self.xList[y])<=self.delta):
					l[x][0][0] = self.xList[y];
			for y in range(len(self.yList)):
				if(abs(l[x][0][1]-self.yList[y])<=self.delta):
					l[x][0][1] = self.yList[y]
	

		l.sort(key=lambda x:(x[0][1],x[0][0]))
	
		# sorting as per y - coordinate and then according to x
		return l;



	def findMaxRC(self):
		self.xSet = list(set(self.xList))
		self.ySet = list(set(self.yList))
		self.xSet.sort();self.ySet.sort()
		
		# print 'Sorted set of coordinates:',self.xSet,self.ySet;
		self.maxrow = len(self.ySet)
		self.maxcol = len(self.xSet)
		# for x in self.xSet:
		# 	count =0;
		# 	for y in self.xList:
		# 		if x is y:
		# 			count+=1;
		# 	if(count>self.maxcol):
		# 		self.maxcol=count;

		# for x in self.ySet:
		# 	count=0;
		# 	for y in self.yList:
		# 		if x is y:
		# 			count+=1;

		# 	if(count>self.maxrow):
		# 		self.maxrow = count;

		print "Rows and columns are:",self.maxrow,self.maxcol



	def makeMatrix(self,l):
		# positionMatrix=[];
		# for i in range(self.maxrow):
		# 	positionMatrix.append([])
		positionMatrix = [[0 for x in range(self.maxcol)] for y in range(self.maxrow)]
		# print positionMatrix
		# positionMatrix = np.array(positionMatrix)
		# print l
		for x in range(len(l)):

			a=l[x][0][0] #x coordinate
			b=l[x][0][1] #y coordinate
		
			xindex = [i for i,element in enumerate(self.xSet) if element == a]
			yindex = [i for i ,element in enumerate(self.ySet) if element == b]
			# print xindex,yindex
			if len(yindex) is not 0:
				positionMatrix[yindex[0]].pop(xindex[0])
				positionMatrix[yindex[0]].insert(xindex[0], l[x])
			
		# print positionMatrix
		self.pM = positionMatrix
		return self.maxrow,self.maxcol,positionMatrix