
FLAG = "XXXXXXXXX"


def xor():
	a = []
	[a.append(ord(x) ^ 0xdeadbeef) for x in FLAG]
	b = raw_input("Enter the password: ")
	if(checker(b)):
		print("Congratulations! You got the flag.")
	else:
		print("Not trying hard enough!")
		exit(-1)

def checker(b):
	return b == "XXXXXXXX"



def main():
	xor()


main()