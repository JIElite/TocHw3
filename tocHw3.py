# ----------------------------------------------------------------------------
#
# Name: Jie Han Chen(JIElite)
# Student ID: F74016077
#
# This code is including 5 function:
#   1. get_outlink_list(fd, reversable)
#   2. get_link_number(website)
#   3. print_data(weblist, top)
#   4. get_input()
#   5. get_topk()
#
# The first function is used to get a sorted list of input data, the element
# is consist of  [webURI, outlink number]. You can choose the data list is
# ascending or descending.
#
# The second function: get_link_number(website) is using for get the number of
# outlink for each URI. I use regex to parse the json data.
#
# The third function: There are two parameters in print_data(weblist, top)
#
# get_input() is used to check whether the second argument sys.argv[1] is
# a file.
#
# get_topk() is used to check whether sys.argv[2] exists and it
# is a positive integer.
#
# ----------------------------------------------------------------------------

import sys
import operator
import os.path
import re
import time


web_regex = re.compile(r'"WARC-Target-URI":"([^"]*)"')
links_regex = re.compile(r'"Links":\[{.+}\](,"Head"|},"Entity-Digest")')
url_regex = re.compile(r'"url":')
href_regex = re.compile(r'"href":')


def print_data(weblist, top):
    """
    print_data(weblist, top) is used to print out the data which is requested
    by user. If the user request 10 data, it should check fallthrough whether
    the outlink number of 11th data is as same as 10th.
    """

    num_of_data = len(weblist)

    for i in xrange(top):
        try:
            print "{0}:{1}".format(weblist[i][0], weblist[i][1])
        except IndexError:
            print "Your request is more than total number of data"
            print "There are total: {0} data".format(num_of_data)
            return

    # Process the remaining webpage with same outlink number
    if top < num_of_data:
        try:
            while weblist[top-1][1] == weblist[top][1]:
                print "{0}:{1}".format(weblist[top][0], weblist[top][1])
                top = top + 1
        except IndexError:
            return
    return


def get_link_number(line_msg):
    """
    This function  can get outlink number of each website.
    It decides the number of outlink by using regex to search  r'"url":'
    and r'"href":' pattern. Finally, add the result for each pattern to get
    the number of outlink.
    """

    try:
        # Try to searh outlinks, if return match object, means there
        # exist some outlinks of this uri.
        links = links_regex.search(line_msg)
        list_links = links.group()

        find_url = url_regex.findall(list_links)
        num_of_url = len(find_url)

        find_href = href_regex.findall(list_links)
        num_of_href = len(find_href)

        num_of_outlink = num_of_href + num_of_url
    except AttributeError:
        # This means there are no "Links" tag
        num_of_outlink = 0

    return num_of_outlink


def get_outlink_list(fd, reversable):
    """
    This function returns a sorted list, the key depends on number of outlink.
    The second parameter is for choosing the outlink is ascending(reversable = True)
    or descending(reversable = False). Finally it returns a list including
    [website uri, outlink number ] as each element in the list.
    """

    weblist = []

    for line_msg in fd:
        url = web_regex.search(line_msg)
        num_of_outlink = get_link_number(line_msg)
        weblist.append([url.group(1), num_of_outlink])

    weblist.sort(key=operator.itemgetter(1), reverse=reversable)
    return weblist


def get_input():
    """
    We Assume the second argument of CLI is input file
    In this funtion, we need to check whether this argument(sys.argv[1]) is
    a file. If it's not, we will print error message and exit.
    """

    try:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print "There is no such file: {0}".format(filename)
            sys.exit(0)

    except IndexError:
        print "There is no input file"
        sys.exit(0)

    return filename


def get_topk():
    try:
        top_k = int(sys.argv[2])
        if top_k < 0:
            raise ValueError
    except IndexError as index_err:
        print "There is no input top_k"
        sys.exit(0)
    except ValueError:
        print "The top_k must be positive integer"
        sys.exit(0)

    return top_k

if __name__ == "__main__":
    start_time = time.time()

    filename = get_input()
    top_k = get_topk()
    with open(filename, "r") as fd:
        weblist = get_outlink_list(fd, True)
        print_data(weblist, top_k)

    finish_time = time.time()
    print "Elapsed Time: ", finish_time - start_time
