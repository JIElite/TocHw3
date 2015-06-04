import sys
import json
import operator


if __name__ == "__main__":
    try:
        f = open(sys.argv[1], "r")
        request = int(sys.argv[2])
    except:
        print "Error"

    weblist = []
    for line in f.readlines():
        web_encode = json.loads(line)
        #print json.dumps(web_encode, sort_keys=True, indent=4)

        try:
            weburl = web_encode['Envelope']['WARC-Header-Metadata']['WARC-Target-URI']
            links = web_encode['Envelope']['Payload-Metadata']['HTTP-Response-Metadata']['HTML-Metadata']['Links']
            pair = (weburl, len(links))
            weblist.append(pair)
        except KeyError:
            # if there is no 'Links' key in the webpage, we just pass it
            pass

    weblist = sorted(weblist, key = operator.itemgetter(1))
    weblist.reverse()

    for i in xrange(request):
        print weblist[i]

    f.close()
