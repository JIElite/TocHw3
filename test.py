import re
import sys

if __name__ == "__main__":
    links_regex = re.compile(r'"Links":\[{.+}\](,"Head"|},"Entity-Digest")')
    islinks_regex = re.compile(r'"Links":\[')

    with open(sys.argv[1], "r") as fd:
        number = 0
        for line in fd:
            number += 1
            if links_regex.search(line) == None and islinks_regex.search(line) != None:
                print number, "wrong!!!"

