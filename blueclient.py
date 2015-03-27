
import bluetooth
import time

# target_name = "HC-05"
# target_address = None

# nearby_devices = bluetooth.discover_devices()

# for bdaddr in nearby_devices:
#     if target_name == bluetooth.lookup_name( bdaddr ):
#         target_address = bdaddr
#         break

# if target_address is not None:
#     print "found target bluetooth device with address ", target_address
# else:
#     print "could not find target bluetooth device nearby"


class Send(object):
	def __init__(self):
		self.target_name = "HC-05"
		self.bd_addr = None
		self.target_address = None 

		nearby_devices = bluetooth.discover_devices()

		for self.bdaddr in nearby_devices:
		    if self.target_name == bluetooth.lookup_name( self.bdaddr ):
		        self.target_address = self.bdaddr
		        break

		if self.target_address is not None:
		    print "found target bluetooth device with address ", self.target_address
		else:
		    print "could not find target bluetooth device nearby"

		port = 1
		self.sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		self.sock.connect((self.target_address, port))

		path = ['d','s','w','s','a','s','w','s']
		for i in path:
			self.sendData(i)
			time.sleep(0.4)



	def sendData(self,x): 
		print "sending data",x,'\n'
		
		self.sock.send((str)(x))
			
			# sock.close()
		# print "data sent successfully"

	def end(self):
		print "Closing socket"
		self.sock.close()

if __name__ == '__main__':
	s = Send()
	# s.sendData()
	# s.end()
	while True:
		x = raw_input('Enter data')
		# x = (int)(x)
		if x is 'h':
			s.end()
			break
		else:
			s.sendData(x)
		

	# print "Finished"
