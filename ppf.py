# defining functions for defining the path of bot from each vertex

class PositionFinder():
	def __init__(self):
		pass;

	def triangle_points(self,cnt):
		a=cnt[0];
		b=cnt[1];
		c=cnt[2];
		direction = self.checkTriangleCondition(a[0],b[0],c[0]);
		# print direction , a,b,c,'\n'
		return direction;


	def checkTriangleCondition(self,a,b,c):
		# defining directions for left and right
		pixeldiff = 5
		# print a,b,c
		if(abs(a[0]-b[0])<= 5):
			if(c[0]>a[0]):
				return "R";
			else:
				return "L";
		if(abs(a[0]-c[0])<=5):
			if(b[0]>a[0]):
				return "R";
			else:
				return "L";
		if(abs(b[0]-c[0])<=5):
			if(a[0]>b[0]):
				return "R";
			else:
				return "L";
		# defining directions for up and down
		if(abs(a[1]-b[1])<=5):
			if(c[1]>a[1]):
				return "D";
			else:
				return "U";
		if(abs(a[1]-c[1])<=5):
			if(b[1]>a[1]):
				return "D";
			else:
				return "U";
		if(abs(b[1]-c[1])<=5):
			if(a[1]>b[1]):
				return "D";
			else:
				return "U";
		else:
			return "N";


