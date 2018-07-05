#from __future__ import print_function

from Tokens import *
from Yacc import *


def main():
    aparser = parser
    s1 = "ArrayList < String > a ;"
    print(parser.parse(s1))
    pass
    #print(s1)
    #print(aparser.parse(s1))
    #print()

    #bparser = parser
    #s2 = "ArrayList<String> a ;"
    #print(s2)
    #print(bparser.parse(s2))
    #print()

if __name__ == "__main__":
    main()
