import sys
import re
import operator
import time
import json

if __name__ == "__main__":

    start = time.time()

    with open(sys.argv[1], "r") as fd:

        weblist = []
        index = 0
        for line_msg in fd:
            index = index + 1
            #web_url = re.search(r'"WARC-Target-URI":"(.+)","WARC-IP-Address"', line_msg)
            url = re.search('"WARC-Target-URI":"([^"]*)"', line_msg)

            web_encode = json.loads(line_msg)
            links = web_encode['Envelope']['Payload-Metadata']['HTTP-Response-Metadata']['HTML-Metadata']['Links']
            print json.dumps(links, indent=4)


    finish = time.time()
    print "Elapsed time: ", finish - start
