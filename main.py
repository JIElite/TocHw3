import sys
import json
import operator

def print_outlink(weblist, top):
    for i in xrange(top):
        print "{0}:{1}".format(weblist[i][0], weblist[i][1])

    # Processing the remaining webpage with same outlink number
    while weblist[top-1][1] == weblist[top][1]:
        print "{0}:{1}".format(weblist[top][0], weblist[top][1])
        top = top + 1
    return


def get_list_outlink(fd):
    weblist = []

    for line in fd.readlines():
        web_encode = json.loads(line)
        #print json.dumps(web_encode, sort_keys=True, indent=4)
        try:
            weburl = web_encode['Envelope']['WARC-Header-Metadata']['WARC-Target-URI']
            links = web_encode['Envelope']['Payload-Metadata']['HTTP-Response-Metadata']['HTML-Metadata']['Links']
        except KeyError:
            # If it arise KeyError means there is not ['Link'] element
            # Because of using len(links) to get the number of outlink
            # we set links to empty string to get 0
            links = ""
        pair = (weburl, len(links))
        weblist.append(pair)

    weblist = sorted(weblist, key = operator.itemgetter(1), reverse = True)
    return weblist



if __name__ == "__main__":
    try:
        fd = open(sys.argv[1], "r")
        top = int(sys.argv[2])
    except IndexError:
        print "Please check your input arguments"

    weblist = get_list_outlink(fd)
    print_outlink(weblist, top)

    fd.close()
