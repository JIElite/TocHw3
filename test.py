import sys
import re
import operator
import time

if __name__ == "__main__":

    start = time.time()

    with open(sys.argv[1], "r") as fd:

        weblist = []
        index = 0
        for line_msg in fd:
            index = index + 1
            #web_url = re.search(r'"WARC-Target-URI":"(.+)","WARC-IP-Address"', line_msg)
            url = re.search('"WARC-Target-URI":"([^"]*)"', line_msg)

            pattern = r'''
            "Links":
             \[
            (
            {
            ("\w+":"[^"]+",?)+
            },?
            )+
             \]
            '''
            links = re.findall(pattern , line_msg)
            print links

            #weblist.append([url.group(1), len(find)])

    weblist.sort(key=operator.itemgetter(1), reverse=True)

    finish = time.time()
    print "Elapsed time: ", finish - start
