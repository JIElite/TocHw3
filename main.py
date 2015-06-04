import sys
import json


if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    for line in f.readlines():
        web_encode = json.loads(line)
        #print json.dumps(web_encode, sort_keys=True, indent=4)
        try:
            links = web_encode['Envelope']['Payload-Metadata']['HTTP-Response-Metadata']['HTML-Metadata']['Links']
            print "Outlink : ", len(links)
        except:
            pass
    f.close()
