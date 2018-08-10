import sys, time

from proc_fasta import *

index = False

for arg in sys.args[1:]:

	print "processing ", arg, " indexing ", index
	if index:
		sttime = time.time()
		d, h, s = parse_fasta(arg , index)
		endtime = time.time()
		print endtime
		
	else:
		sttime = time.time()
		h, s = parse_fasta(arg , index)
		endtime = time.time()
		print endtime
		print "index phase"
		sttime = time.time()
		index_data(h, s)
		endtime = time.time()
		print endtime

	index = not index

