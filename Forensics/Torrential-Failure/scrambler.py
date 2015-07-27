import random
import struct 

with open('flag.txt.torrent') as f:
    contents = f.readlines()[0]

hashes_start = 0xD0
hashes_len = 0x9C

fake_hashes = ''.join([struct.pack('B', random.randint(0x0, 0xFF)) for x in xrange(hashes_len)])

out = contents[:hashes_start] + fake_hashes + contents[hashes_start+hashes_len:]

with open('solveme.torrent', 'w') as f:
    f.write(out)
    print "Wrote output to solveme.torrent"
