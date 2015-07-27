#!/usr/bin/env python
# run this file with socat TCP-LISTEN:1337,fork,readbytes=4096 EXEC:./runner.py,pty,stderr
# You can replace 1337 with whatever port you want to use
from tree import Tree
from random import shuffle

flag = "flag{m1ssing_th3_f0r3st_4_t43_t433z}"
num_challenges = 100

def generate_problem(difficulty):
    starting = range(difficulty)
    shuffle(starting)
    tree = Tree()
    for x in starting:
        tree.insert(x)
    return (starting, tree.post_order())

def main():
    for x in xrange(num_challenges):
        difficulty = 10 + (x)
        problem = generate_problem(difficulty)
        print "--- Print in post order (separated by ,'s): ---"
        print ", ".join(map(str, problem[0]))
        answer = raw_input()
        try:
            answer = map(int, answer.split(','))
            if answer != problem[1]:
                raise ValueError('nope')
            print 'Looks right to me, on to the next!'
        except ValueError:
            print "Sorry, that doesn't seem to be right"
            return
    print "Good work, you got them all. Here's the flag:",flag

if __name__ == '__main__':
    main()
