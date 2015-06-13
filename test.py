import sys
import re
import operator
import time

if __name__ == "__main__":

    start = time.time()

    with open(sys.argv[1], "r") as fd:

        weblist = []
        for line_msg in fd:

            #web_url = re.search(r'"WARC-Target-URI":"(.+)","WARC-IP-Address"', line_msg)
            url = re.search('"WARC-Target-URI":"([^"]*)"', line_msg)

            try:
                links = re.search(r'"Links":\[{.+}\]}?,"\w+"', line_msg)
                list_links = links.group()

                #find_out = re.findall(r'"path":"\w+@/\w+"', list_links)
                #num_of_outlink = len(find_out)

                find_url = re.findall(r'"url":', list_links)
                num_of_url = len(find_url)

                find_href = re.findall(r'"href":', list_links)
                num_of_href = len(find_href)

                num_of_outlink = num_of_href + num_of_url

            except AttributeError:
                # This means there are no outlinks
                num_of_outlink = 0

            weblist.append([url.group(1), num_of_outlink])

    weblist.sort(key=operator.itemgetter(1), reverse=True)

    for data in weblist:
        print data[0],":", data[1]

    finish = time.time()
    print "Elapsed time: ", finish - start
