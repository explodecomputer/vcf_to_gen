#!/usr/bin/python

import sys
import gzip

def get_probs(x):
	return " ".join(map(str, [round(pow(10, float(y)),3) for y in x.split(":")[2].split(",")]))


def get_probs_all(x):
	return " ".join([get_probs(y) for y in x])

print 'input file:', str(sys.argv[1])
print 'output file:', str(sys.argv[2])


f = gzip.open(sys.argv[1])
o = gzip.open(sys.argv[2], "wb")

for _ in xrange(4):
	a = next(f)

line = f.readline()
while line:
	content = line.strip().split('\t')
	first = " ".join([content[0], content[2], content[1], content[3], content[4]])
	del content[:9]
	probs = get_probs_all(content)
	o.write(first + " " + probs + "\n")
	line = f.readline()
f.close()
o.close()




