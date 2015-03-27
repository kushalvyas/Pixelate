# from ete2 import Tree


import networkx as nx
import matplotlib.pyplot as plt

from blueclient import Send

from tracker1 import Track


class pixy(object):
	def __init__(self):
		# global prevnode;
		
		# self.t = Tree()
	
		# self.dictlist = ['AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW','AX','AY','AZ','BA','BB','BC','BD','BE','BF','BG','BH','BI','BJ'];

		self.dictlist = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35'];
		self.graphlist=[];
		self.mypaths=[];
		self.pathlist=[];
		self.pM = None
		self.shortestpath=None;
		
		

	# def search_and_traverse(self,l):
	# 	startindex,endindex = [],[];
	# 	for i in range(len(l)):
	# 		for j in range(len(l)):
	# 			if(l[i][j]=='START'):
	# 				print "START is at: ",i,j
	# 				startindex.append(i)
	# 				startindex.append(j)
	# 			if(l[i][j]=='END'):
	# 				print "End is at: ",i,j
	# 				endindex.append(i)
	# 				endindex.append(j)


	# 	# assuming the first motion from start is upward
	# 	self.node  = [startindex]

	# 	# adds start to child also
	# 	self.ms.add_child(self.node[0])

	# 	# pop child
	# 	child  = self.ms.pop_child()

	# 	# add the popped to parent
	# 	self.ms.add_parent(child)

	# 	# added start to tree
	# 	self.tnode = self.t.add_child(name = child)
		
	# 	#  traverse the popped node and result is stored in self.node
	# 	self.node = self.traverse(self.ms.pop_parent())

	# 	# add every child seperately into child list
	# 	for each in self.node:
	# 		self.ms.add_child(each);
	# 		self.ms.add_parent(each);

	# 		# self.tnode.add_child(name=child);
	# 		if(l[each[0]][each[1]] == 'END'):
	# 			print "Completed"
	# 			break;
	# 	parentpop = self.ms.pop_parent()
	# 	self.tnode.add_child(name=parentpop)
	# 	# print self.ms.parentStack,self.ms.childStack,parentpop
	# 	self.tnode = parentpop
	# 	while  True:
	# 		try:
				
	# 			child = self.ms.pop_child();
	# 			self.tnode = parentpop
				
	# 			self.node = self.traverse(child)

	# 			print "parent pop is :", parentpop
	# 			for each in self.node:
	# 				self.ms.add_child(each);
	# 				#  whatever goes in the tree goes in parent
	# 				self.ms.add_parent(each)
	# 				self.tnode.add_child(name=each)
					
	# 			parentpop = self.ms.pop_parent()
	# 			print self.ms.parentStack ,'\n',self.ms.childStack,'\n'
	# 		except:
	# 			parentpop = self.ms.pop_parent()
	# 			print "break"
	# 			# break
	# 		finally:
	# 			# pass;
	# 			print self.t #,'\n',self.ms.parentStack,'\n',self.ms.childStack
			

			


		
		
		


	# def traverse(self,node):
	# 	global myarray,find;
		
	# 	self.currentnode = node#1-D list
	# 	shape = myarray[self.currentnode[0]][self.currentnode[1]]
	# 	if(shape=='START' or shape == 'U'):
	# 		newnode = find.goUP(self.currentnode);
	# 	elif(shape=='R'):
	# 		newnode = find.goRight(self.currentnode)
	# 	elif(shape == 'S'):
	# 		newnode = find.square(self.prevnode,self.currentnode)
	# 	elif (shape=='Q'):
	# 		newnode = find.quad(self.prevnode,self.currentnode)
	# 	else : 
	# 		pass;
	# 	self.prevnode = self.currentnode
	# 	# print newnode
	# 	for i in newnode:
	# 		if i is None:
	# 			newnode.remove(i)

	# 	self.finalnewnode = []
	# 	for i in newnode:
	# 		if i is not None:
	# 			if((i[0]>=0 and i[0]<=3) and i[1]>=0 and i[1]<=3):
	# 				self.finalnewnode.append(i)
	# 	return self.finalnewnode


	def makeAM(self,l ,pm,r,c):
		self.pM = pm
		self.mainlist = [];
		self.r=r
		self.c=c
		for i in l:
			for j in i:
				self.mainlist.append(j)

		print self.mainlist
		self.length = len(self.mainlist)
		print self.length
		print "length = ",len(l)

		self.adjmtx = [[0 for x in range(self.length)] for y in range(self.length)]
		
		for i in range(len(l)):
			for j in range(len(l)):
				print l[i][j],i,j,
				if l[i][j] == 'S':
					if ( (i<5 and i >0) and (j<5 and j>0) ):
						self.adjmtx[i*6 + j][(i+1)*6 +j]=1
						self.adjmtx[i*6 + j][(i)*6 +(j+1)]=1
						self.adjmtx[i*6 + j][(i)*6 +(j-1)]=1
						self.adjmtx[i*6 + j][(i-1)*6 +j]=1
					else:
						if ((i == 0) and (j == 0)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i+1)*6 + j]=1
						elif ( (i == 0) and (j == 5) ):
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
						elif ( (i == 5 ) and (j == 0) ):
							self.adjmtx[i*6 +j][(i)*6 + (j+1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						elif ( (i == 5) and (j == 5) ):
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + (j)]=1
						# 
						elif ( (i == 0) and (j>0 and j<5)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i+1)*6 + j]=1
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
						elif ( (i == 5)and(j>0 and j<5)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i-1)*6 + j]=1
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
						elif ((j == 0) and (i>0 and i<5)):
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
							self.adjmtx[i*6 + j][(i)*6 + (j+1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						elif ((j == 5) and (i<5 and i>0)):
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
							self.adjmtx[i*6 + j][(i)*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1



				# for Quad
				elif l[i][j] == 'Q':
					if ( (i<5 and i >0) and (j<5 and j>0) ):
						self.adjmtx[i*6 + j][(i+1)*6 +j]=1
						self.adjmtx[i*6 + j][(i)*6 +(j+1)]=1
						self.adjmtx[i*6 + j][(i)*6 +(j-1)]=1
						self.adjmtx[i*6 + j][(i-1)*6 +j]=1
					else:
						if ((i == 0) and (j == 0)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i+1)*6 + j]=1
						elif ( (i == 0) and (j == 5) ):
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
						elif ( (i == 5 ) and (j == 0) ):
							self.adjmtx[i*6 +j][(i)*6 + (j+1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						elif ( (i == 5) and (j == 5) ):
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + (j)]=1
						# 
						elif ( (i == 0) and (j>0 and j<5)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i+1)*6 + j]=1
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
						elif ( (i == 5)and(j>0 and j<5)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i-1)*6 + j]=1
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
						elif ((j == 0) and (i>0 and i<5)):
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
							self.adjmtx[i*6 + j][(i)*6 + (j+1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						elif ((j == 5) and (i<5 and i>0)):
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
							self.adjmtx[i*6 + j][(i)*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						else:
							print 'tp\n';



				elif l[i][j] == 'START':
					# since start == same as a square it'll follow all the properties
					# print (i*6 + j),((i-1)*4 + j)
					# self.adjmtx[i*6 + j][(i-1)*6 + j] =1
					if ( (i<5 and i >0) and (j<5 and j>0) ):
						self.adjmtx[i*6 + j][(i+1)*6 +j]=1
						self.adjmtx[i*6 + j][(i)*6 +(j+1)]=1
						self.adjmtx[i*6 + j][(i)*6 +(j-1)]=1
						self.adjmtx[i*6 + j][(i-1)*6 +j]=1
					else:
						if ((i == 0) and (j == 0)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i+1)*6 + j]=1
						elif ( (i == 0) and (j == 5) ):
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
						elif ( (i == 5 ) and (j == 0) ):
							self.adjmtx[i*6 +j][(i)*6 + (j+1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						elif ( (i == 5) and (j == 5) ):
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + (j)]=1
						# 
						elif ( (i == 0) and (j>0 and j<5)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i+1)*6 + j]=1
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
						elif ( (i == 5)and(j>0 and j<5)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i-1)*6 + j]=1
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
						elif ((j == 0) and (i>0 and i<5)):
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
							self.adjmtx[i*6 + j][(i)*6 + (j+1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						elif ((j == 5) and (i<5 and i>0)):
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
							self.adjmtx[i*6 + j][(i)*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						else:
							print "pass",l[i][j]

				elif l[i][j] == 'END':
					# same as a square
					if ( (i<5 and i >0) and (j<5 and j>0) ):
						self.adjmtx[i*6 + j][(i+1)*6 +j]=1
						self.adjmtx[i*6 + j][(i)*6 +(j+1)]=1
						self.adjmtx[i*6 + j][(i)*6 +(j-1)]=1
						self.adjmtx[i*6 + j][(i-1)*6 +j]=1
					else:
						if ((i == 0) and (j == 0)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i+1)*6 + j]=1
						elif ( (i == 0) and (j == 5) ):
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
						elif ( (i == 5 ) and (j == 0) ):
							self.adjmtx[i*6 +j][(i)*6 + (j+1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						elif ( (i == 5) and (j == 5) ):
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + (j)]=1
						# 
						elif ( (i == 0) and (j>0 and j<5)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i+1)*6 + j]=1
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
						elif ( (i == 5)and(j>0 and j<5)):
							self.adjmtx[i*6 +j][i*6 + (j+1)]=1
							self.adjmtx[i*6 + j][(i-1)*6 + j]=1
							self.adjmtx[i*6 +j][i*6 + (j-1)]=1
						elif ((j == 0) and (i>0 and i<5)):
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
							self.adjmtx[i*6 + j][(i)*6 + (j+1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						elif ((j == 5) and (i<5 and i>0)):
							self.adjmtx[i*6 +j][(i+1)*6 + j]=1
							self.adjmtx[i*6 + j][(i)*6 + (j-1)]=1
							self.adjmtx[i*6 +j][(i-1)*6 + j]=1
						else:
							print "passes",l[i][j]

				# for triangle

				elif l[i][j] == 'R':
					# right pointing triangle
					if j < 5:
						self.adjmtx[i*6 + j][i*6 + (j+1)]=1
						# removing link connection in reverse direction
						# if self.adjmtx[i*6 + (j+1)][i*6 + j] == 1:
						self.adjmtx[i*6 + (j+1)][i*6 + j]=0

					else:
						print 'tp\n';

				elif l[i][j] == 'L':
					# left pointing triangle
					if j > 0:
						self.adjmtx[i*6 + j][i*6 + (j-1)]=1
						# removing link connection in reverse direction
						# if self.adjmtx[i*6 + (j-1)][i*6 + j] == 1:
						self.adjmtx[i*6 + (j-1)][i*6 + j]=0
					else:
						print 'tp\n';

				elif l[i][j] == 'U':
					# UP pointing triangle
					if i>0:
						self.adjmtx[i*6 + j][(i-1)*6 + j]=1
						# removing link connection in reverse direction
						# if self.adjmtx[(i-1)*6 + j][i*6 + j] == 1:
						self.adjmtx[(i-1)*6 + j][i*6 + j]=0
					else:
						print 'tp\n';

				elif l[i][j] == 'D':
					# down pointing triangle
					if i < 5:
						self.adjmtx[i*6 + j][(i+1)*6 + j]=1
						# removing link connection in reverse direction
						# if self.adjmtx[(i+1)*6 + j][i*6 + j] == 1:
						self.adjmtx[(i+1)*6 + j][i*6 + j]=0
					else:
						print 'tp\n';


				# cancelling links for invalid blocks
				elif l[i][j] == 'N':
					# breaking all links for restricted blocks
					if ( (i<5 and i >0) and (j<5 and j>0) ):
						#  links from N to others == zero
						self.adjmtx[i*6 + j][(i+1)*6 +j]=0
						self.adjmtx[i*6 + j][(i)*6 +(j+1)]=0
						self.adjmtx[i*6 + j][(i)*6 +(j-1)]=0
						self.adjmtx[i*6 + j][(i-1)*6 +j]=0
						# links from others to N == zero
						self.adjmtx[(i+1)*6 + j][i*6 +j]=0
						self.adjmtx[(i-1)*6 + j][(i)*6 +(j)]=0
						self.adjmtx[i*6 + (j+1)][(i)*6 +(j)]=0
						self.adjmtx[i*6 + (j-1)][(i)*6 +j]=0

					else:
						if ((i == 0) and (j == 0)): # the corner block
							# links from N
							self.adjmtx[i*6 +j][i*6 + (j+1)]=0
							self.adjmtx[i*6 + j][(i+1)*6 + j]=0
							# links from others to N
							self.adjmtx[i*6 +(j+1)][i*6 + (j)]=0
							self.adjmtx[(i+1)*6 + j][(i)*6 + j]=0

						elif ( (i == 0) and (j == 5) ):
							# links from N
							self.adjmtx[i*6 +j][i*6 + (j-1)]=0
							self.adjmtx[i*6 +j][(i+1)*6 + j]=0
							# links from others to N
							self.adjmtx[i*6 +(j-1)][i*6 + (j)]=0
							self.adjmtx[(i+1)*6 +j][(i)*6 + j]=0

						elif ( (i == 5 ) and (j == 0) ):
							# links from N
							self.adjmtx[i*6 +j][(i)*6 + (j+1)]=0
							self.adjmtx[i*6 +j][(i-1)*6 + j]=0
							#  links to N
							self.adjmtx[i*6 +(j+1)][(i)*6 + (j)]=0
							self.adjmtx[(i-1)*6 +j][(i)*6 + j]=0

						elif ( (i == 5) and (j == 5) ):
							# links from N
							self.adjmtx[i*6 +j][i*6 + (j-1)]=0
							self.adjmtx[i*6 +j][(i-1)*6 + (j)]=0
							# links to N
							self.adjmtx[i*6 +(j-1)][i*6 + (j)]=0
							self.adjmtx[(i-1)*6 +j][(i)*6 + (j)]=0
						# 
						elif ( (i == 0) and (j>0 and j<5)):
							# links from N
							self.adjmtx[i*6 +j][i*6 + (j+1)]=0
							self.adjmtx[i*6 + j][(i+1)*6 + j]=0
							self.adjmtx[i*6 +j][i*6 + (j-1)]=0
							# links to N
							self.adjmtx[i*6 +(j+1)][i*6 + (j)]=0
							self.adjmtx[(i+1)*6 + j][(i)*6 + j]=0
							self.adjmtx[i*6 +(j-1)][i*6 + (j)]=0

						elif ( (i == 5)and(j>0 and j<5)):
							# links from N
							self.adjmtx[i*6 +j][i*6 + (j+1)]=0
							self.adjmtx[i*6 + j][(i-1)*6 + j]=0
							self.adjmtx[i*6 +j][i*6 + (j-1)]=0
							# link to N
							self.adjmtx[i*6 +(j+1)][i*6 + (j)]=0
							self.adjmtx[(i-1)*6 + j][(i)*6 + j]=0
							self.adjmtx[i*6 +(j-1)][i*6 + (j)]=0

						elif ((j == 0) and (i>0 and i<5)):
							# links from N
							self.adjmtx[i*6 +j][(i+1)*6 + j]=0
							self.adjmtx[i*6 + j][(i)*6 + (j+1)]=0
							self.adjmtx[i*6 +j][(i-1)*6 + j]=0
							# links to N
							self.adjmtx[(i+1)*6 +j][(i)*6 + j]=0
							self.adjmtx[i*6 + (j+1)][(i)*6 + (j)]=0
							self.adjmtx[(i-1)*6 +j][(i)*6 + j]=0


						elif ((j == 5) and (i<5 and i>0)):
							# links from N
							self.adjmtx[i*6 +j][(i+1)*6 + j]=0
							self.adjmtx[i*6 + j][(i)*6 + (j-1)]=0
							self.adjmtx[i*6 +j][(i-1)*6 + j]=0
							# links to N
							self.adjmtx[(i+1)*6 +j][(i)*6 + j]=0
							self.adjmtx[i*6 + (j-1)][(i)*6 + (j)]=0
							self.adjmtx[(i-1)*6 +j][(i)*6 + j]=0
						else:
							print 'tp\n';

				

				else:
					print "Pass in adjmtx",l[i][j];



		# count=0
		# for i in range(16):
		# 	for j in range(16):
				
		# 		print self.adjmtx[i][j],'\t',
		# 		if self.adjmtx[i][j] is 1:
		# 			count+=1
		# 		if j is 15:
		# 			print ''
		# 			break
				
		# 	print '\n'
				
		# print count

		self.makeGraph()


	def makeGraph(self):
		print len(self.adjmtx)
		for i in range(len(self.adjmtx)):
			for j in range(len(self.adjmtx)):
				if self.adjmtx[i][j] ==1:
					# print i,j
					self.graphlist.append((self.dictlist[i],self.dictlist[j]))

		# print self.graphlist
		# setting the values of START and END according to Graph Letters
		indexStart = self.mainlist.index('START')
		self.start = self.dictlist[indexStart]
		print self.start

		indexEnd = self.mainlist.index('END')
		self.end = self.dictlist[indexEnd]
		print self.end

		self.draw_graph(self.graphlist)


	def draw_graph(self,graph, labels=None, graph_layout='shell',
               node_size=1600, node_color='blue', node_alpha=0.3,
               node_text_size=8,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

	    # create networkx graph
	    G=nx.Graph()

	    # add edges
	    for edge in graph:
	        G.add_edge(edge[0], edge[1])

	    
	    graph_pos=nx.shell_layout(G)

	    # draw graph
	    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
	                           alpha=node_alpha, node_color=node_color)
	    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
	                           alpha=edge_alpha,edge_color=edge_color)
	    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
	                            font_family=text_font)

	    if labels is None:
	        labels = range(len(graph))

	    edge_labels = dict(zip(graph, labels))
	    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
	                                 label_pos=edge_text_pos)

	    
	    self.p =nx.all_simple_paths(G,self.start,self.end)
	    self.mypaths =  list(self.p)
	    print len(self.mypaths) , "paths available"
	    print "Calculating Valid paths"
	    # print self.mypaths[69]
	    # count=0
	    # for each in  (list(self.p)):
	    # 	count+=1
	    # 	print each ,'\n'

	    
	    # retval =  nx.has_path(G,'A','C')
	    # if retval:
	    # 	print([p for p in nx.all_simple_paths(G,'I','C')])

	    # show graph

		          
	    # plt.show()
	    print '';
	    self.checkpath();
	    # self.cmpp()

	# now making a function which will check the truthfulness of the path
	def checkpath(self):
		
		print "entered checkpath func";
		# print self.mypaths;
		for each in self.mypaths:
			checked=0
			for i in range(len(each)-1):
				# get the index position of the Symbol from dictlist
				idx = self.dictlist.index(each[i])
				# print self.mainlist[idx],idx,'\n'
				# now make a function to write all conditions
				# in case of START
				if self.mainlist[idx] is 'START':
					
					next =each[i+1]
					currentidx = idx;
					ni =  self.dictlist.index(next)
					if ((abs(currentidx-ni) == 6) or (abs(currentidx-ni) == 1)) : # 8,2
						checked=1
						# print 'here'
					else:
						# print "break S " , self.mypaths.index(each),"at",i
						checked=0;
						break

				# for square
				elif self.mainlist[idx] is 'S':
					prev = each[i-1]
					next = each[i+1]
					pi = self.dictlist.index(prev)
					ni = self.dictlist.index(next)
					if ((abs(pi-ni) == 12) or (abs(pi-ni) == 2)) : # 8,2
						checked=1
						# print 'here'
					else:
						# print "break S " , self.mypaths.index(each),"at",i
						checked=0;
						break

				# for upward triangle
				elif self.mainlist[idx] is 'U':
					next = each[i+1]
					ni = self.dictlist.index(next)
					if(idx-ni == 6): # 4
						checked=1;
					else:
						# print "break U " , self.mypaths.index(each),"at",i
						checked=0
						break

				# for downward triangle
				elif self.mainlist[idx] is 'D':
					next = each[i+1]
					ni = self.dictlist.index(next)
					if((idx-ni) == (-6)): # -4
						checked=1;
					else:
						# print "break D " , self.mypaths.index(each),"at",i
						checked=0
						break

				# for right triangle
				elif self.mainlist[idx] is 'R':
					next = each[i+1]
					ni = self.dictlist.index(next)
					if((idx-ni) == -1): # -1
						checked=1;
					else:
						# print "break R " , self.mypaths.index(each),"at",i
						checked=0
						break

				# for left triangle
				elif self.mainlist[idx] is 'L':
					next = each[i+1]
					ni = self.dictlist.index(next)
					print ni,next
					if(idx-ni == 1): #1
						checked=1;
					else:
						# print "break L " , self.mypaths.index(each),"at",i
						checked=0
						break

				# for quad
				elif self.mainlist[idx] is 'Q':
					prev = each[i-1]
					next = each[i+1]
					pi = self.dictlist.index(prev)
					ni = self.dictlist.index(next)
					# print prev,pi,next,ni
					if ((abs(pi-ni) == 12) or (abs(pi-ni) == 7) or (abs(pi-ni) == 5) or (abs(pi-ni) == 2)) : # 8,3,5,2
						checked=1
						
						# print checked
					else:
						# print "break Q " , self.mypaths.index(each),"at",i
						checked=0;
						break
				else:
					# print 'here'
					checked=0
					break


			# print checked
			if checked :
				self.pathlist.append(each)

		print self.pathlist
		# print self.mypaths
		self.cmpp()
		self.find_shortest();
		self.trackerobj = Track(self.shortestpath,self.pM,self.dictlist)
		# self.trackerobj = Track(self.mypaths[0],self.pM,self.dictlist);
		self.trackerobj.setcommands();
		self.trackerobj.run();



		
	def cmpp(self):
		# p = ['31','25','19','13','7','1','2','3','9','15','16','22','28','34','33','32','26','20']
		p=['31','32','26','20']
		for each in self.mypaths:
			x = cmp(p,each)
			if x is 0:
				print "Desired path is present at ",self.mypaths.index(each)
				break;



	def find_shortest(self):
		l = len(self.pathlist)
	
		if l == 1:
			self.shortestpath = self.pathlist[0]
		else:
			# calculating number of white squares
			whitelist = [];
			for everypath in self.pathlist:
				whitecount = 0;
				for node in everypath:
					# print node,
					idx = self.dictlist.index(node)
					# print idx
					row = idx/6;
					col = idx%6;
					# print row,col,
					attr = self.pM[row][col][1][0]
					# print attr ,'\n'
					if attr == "White":
						# print "White detected"
						whitecount+=1;
				whitelist.append(whitecount);

			print whitelist , min(whitelist)
			minid = whitelist.index(min(whitelist))
			self.shortestpath = self.pathlist[minid]

		print "Shortest Path = ",self.shortestpath



		
# if __name__ == '__main__':

# 	find = Finder();
# 	myarray = [];
# 	myarray.append(['Q','R','S','S']);
# 	myarray.append(['S','S','D','END']);
# 	myarray.append(['R','Q','S','U']);
# 	myarray.append(['S','START','U','S']);
	

# 	# myarray.append(['Q','Q','END','Q']);
# 	# myarray.append(['Q','Q','S','Q']);
# 	# myarray.append(['START','Q','Q','Q']);
# 	# myarray.append(['Q','Q','Q','Q']);

	# p = pixy()

	# # p.search_and_traverse(myarray)
	# p.makeAM(myarray)
	# print paths
	# p.checkpath(paths)