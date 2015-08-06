
FLAG = NOTHING IS FREE.SOLVE IT!

def xor():
	a = []
	[a.append(ord(x) ^ 0xdeadbeef) for x in FLAG]
	#[3735928457, 3735928451, 3735928462, 3735928456, 3735928468, 3735928503, 3735928480, 3735928509, 3735928496, 3735928503, 3735928480, 3735928509, 3735928496, 3735928503, 3735928480, 3735928509, 3735928466]
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
