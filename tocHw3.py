import sys
import json
import operator
import os.path

def print_outlink(weblist, top):
    total_data = len(weblist)

    for i in xrange(top):
        try:
            print "{0}:{1}".format(weblist[i][0], weblist[i][1])
        except IndexError:
            print "Your request is more than total number of data"
            print "There are total: {0} data".format(total_data)
            return

    # Processing the remaining webpage with same outlink number
    if top < total_data:
        try:
            while weblist[top-1][1] == weblist[top][1]:
                print "{0}:{1}".format(weblist[top][0], weblist[top][1])
                top = top + 1
        except IndexError:
            return
    return


def get_list_outlink(fd):
    weblist = []

    for line in fd.readlines():
        web_encode = json.loads(line)
        # print json.dumps(web_encode, sort_keys=True, indent=4)
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

    weblist.sort(key=operator.itemgetter(1), reverse=True)
    return weblist


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        if os.path.exists(filename):
            pass
        else:
            raise IOError
    except IndexError:
        print "There is no input file"
        sys.exit(0)
    except IOError:
        print "There is no such file: {0}".format(filename)
        sys.exit(0)


    with open(filename, "r") as fd:
        try:
            top_k = int(sys.argv[2])
        except IndexError as index_err:
            print "There is no input top_k"
            sys.exit(0)
        except ValueError:
            print "The top_k must be integer"
            sys.exit(0)
        weblist = get_list_outlink(fd)
        print_outlink(weblist, top_k)
