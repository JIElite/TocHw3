import sys
import operator
import os.path
import re
import time

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

    for line_msg in fd:

        #web_url = re.search(r'"WARC-Target-URI":"(.+)","WARC-IP-Address"', line_msg)
        url = re.search('"WARC-Target-URI":"([^"]*)"', line_msg)


        links = re.findall(r'"Links":\[{.+}\],"Head"', line_msg)

        try:
            find_url = re.findall(r'"url":', links[0])
            num_of_url = len(find_url)
        except IndexError:
            num_of_url = 0

        try:
            find_href = re.findall(r'"href":', links[0])
            num_of_href = len(find_href)
        except IndexError:
            num_of_href = 0

        num_of_outlink = num_of_href + num_of_url
        weblist.append([url.group(1), num_of_outlink])
        #weblist.append([num_of_outlink, web_url.group(1)])

    weblist.sort(key=operator.itemgetter(1), reverse=True)
    return weblist


if __name__ == "__main__":

    start_time = time.time()

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

    finish_time = time.time()
    print "Elapsed Time: ", finish_time - start_time
