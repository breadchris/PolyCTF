import sys, os

def encrypt(data, key):
    out = ""
    for char in data:
        out += chr(ord(char) ^ key)
    return out

def decrypt(data, key):
    return encrypt(data, key)

def read_file(filename):
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            return f.read().strip()
    else:
        raise Exception("File: %s does not exist" % filename)

def main(argv):
    if len(argv) != 4:
        print "Usage: %s ([encrypt] [decrypt]) [filename] [xor key]" % argv[0]
        sys.exit(1)

    xor_key = int(argv[3])
    file_data = read_file(argv[2])

    if argv[1] == "decrypt":
        print "[*] Decrypting file with xor key 0x%x" % xor_key
        print decrypt(file_data.decode("hex"), xor_key)
        print "[+] Decryption Finished"
    elif argv[1] == "encrypt":
        print "[*] Encrypting file with xor key 0x%x" % xor_key
        print encrypt(file_data, xor_key).encode("hex")
        print "[+] Encryption Finished (data encoded in hexidecimal format)"

if __name__ == "__main__":
    main(sys.argv)
