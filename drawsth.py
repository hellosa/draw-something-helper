#!/usr/bin/env python

import sys
import enchant
import itertools
import getopt

d = enchant.Dict("en_US")

def possible_word (letters, length) :
    rlength = int(length)
    for perm in itertools.permutations(letters, rlength):
        possible = ""
        for i in perm : 
            possible += i
        if d.check(possible):
            print possible


def usage():
    print "Example: python drawsth.py -l xxxxxx -L 3"
    return 1

def main() :
    try:
        opts, args = getopt.getopt(sys.argv[1:], "l:L:h", ["letters=","length=","help"])
    except getopt.GetoptError, err:
        print str(err) 
        usage()
        sys.exit(2)

    letters = None
    length = None

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-l", "--letters"):
            letters = a
        elif o in ("-L", "--length"):
            length = a
        else:
            assert False, "unhandled option"
    if letters is None:
        print "-l/--letters is none"
        usage()
        sys.exit(1)
    if length is None:
        print "-L/--length is none"
        usage()
        sys.exit(1)

    possible_word(letters , length)

if __name__ == "__main__":
    main()

