#!/usr/bin/python

import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument("file", help="The file to parse")
args = parser.parse_args()

items = []
labels = {}
labels[-1] = "UNKNOWN"


def convert_to_date(unix_ts):
    return datetime.datetime.fromtimestamp(unix_ts).strftime("%Y-%m-%d")


class Item(object):
    def __init__(self, fields):
        self.itemid = fields[1]
        self.name = fields[2]
        self.amount = fields[3]
        self.timestamp = convert_to_date(int(fields[6]) / 1000)
        self.labelId = int(fields[10])

# read in all the lines, delimited by ;
fh = open(args.file, 'r')
for line in fh:
    fields = line.split(';')
    if fields[0] == '01':
        i = 0
        for f in fields:
            # print "  %d: %s" % (i, f)
            i = i+1

        items.append(Item(fields))
    elif fields[0] == '02':
        labels[int(fields[1])] = fields[2]


for item in items:
    print "%s,%s,%s,%s" % (item.timestamp, labels[item.labelId], item.name, item.amount)

