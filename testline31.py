import sys
import re


if __name__ == "__main__":
    with open(sys.argv[1], "r") as fd:
        nurl = 0
        nref = 0
        for line in fd:
            if re.search(r'"url":', line) != None:
                nurl = nurl + 1
            if re.search(r'"href":', line) != None:
                nref = nref + 1

        print nurl, nref
