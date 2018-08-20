import sys, time

from parse_fasta import *

index = False

for arg in sys.argv[1:]:

    with open(arg) as f:
	print "processing ", arg, " indexing ", index
	if index:
		sttime = time.time()
		d = parse_fasta(f , index)
		endtime = time.time()
		print endtime - sttime
		
	else:
		sttime = time.time()
		h, s = parse_fasta(f , index)
		endtime = time.time()
		print endtime - sttime
		print "index phase"
		sttime = time.time()
		d = index_data(h, s)
		endtime = time.time()
		print endtime - sttime

        index = not index
        sys.stdout.flush()
