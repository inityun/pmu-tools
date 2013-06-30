#!/usr/bin/python
# verify plog.* output by running event one by one
import sys, os

def run(x):
	print x
	os.system(x)

for l in sys.stdin:
	if l.find(",") < 0:
		continue
	n = l.strip().split(",")
	run("perf stat --output l -x, -e %s ./loop" % (n[1]))
	f = open("l", "r")
	for i in f:
		if i.find(",") < 0:
			continue
		j = i.strip().split(",")
		break
	f.close()
	if float(n[0]) > 0:
		delta = (float(j[0]) - float(n[0]))/float(n[0])
	else:
		delta = 0
	print n[1],j[0],n[0],"%.2f" % (delta * 100.0)
