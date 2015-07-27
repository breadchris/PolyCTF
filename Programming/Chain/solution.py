import urllib2

def main():
    curr = 0
    while True:
        u = urllib2.urlopen('http://localhost:5000/' + str(curr))
        contents = u.readlines()
        if len(contents) > 1:
            print "Solution:",contents[-1]
            return
        else:
            curr = contents[0]

if __name__ == '__main__':
    main()
