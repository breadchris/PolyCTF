import hashlib
import time
import string
def bruteforce(tehHash):
	for zero in list(string.ascii_lowercase[9:13]):
		for one in list(string.ascii_uppercase):
			for two in range(0,10):
				for three in range(0,10):
					for five in range(0,10):
						for six in list(string.ascii_lowercase[14:20]):
							for seven in range(0,10):
								for nine in range(0,10):
									if(hashlib.md5(zero+one+str(two)+str(three)+"d"+str(five)+six+str(seven)+"u"+str(nine)).hexdigest()==tehHash):
										return zero+one+"1"+str(three)+"d"+str(five)+six+str(seven)+"u"+str(nine)

t0 = time.clock()
a = bruteforce('9b9ce520ab2653c129c346bc44dac9cb')
print "Time: "+str(time.clock()-t0)+"s"
print a
