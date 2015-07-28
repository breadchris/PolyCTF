# Oscar the Grouch

## Problem
The md5 hash of the key is `9b9ce520ab2653c129c346bc44dac9cb`. The format of each character of the 10 character key is: 
 - a lowercase letter from j-m inclusive
 - an uppercase letter from A-Z inclusive
 - a number from 0-9 inclusive
 - a number from 0-9 inclusive
 - "d"
 - a number from 0-9 inclusive
 - a lowercase letter from o-t inclusive
 - a number from 0-9 inclusive
 -"u"
 - a number from 0-9 inclusive

## Answer
`9b9ce520ab2653c129c346bc44dac9cb` = `mA10d0r0u5` (using the Python hashlib.md5 function)

Time to bruteforce: 136.741879s

### My Solution
```
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
```
