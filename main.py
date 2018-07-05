from __future__ import print_function

from Tokens import *
from Yacc import *


def main():
    aparser = yacc
    s1 = "ArrayList < String > a ;"
    print(s1)
    print(aparser.parse(s1))
    print()

    bparser = yacc
    s2 = "ArrayList<String> a ;"
    print(s2)
    print(bparser.parse(s2))
    print()


if __name__ == "__main__":
    main()
