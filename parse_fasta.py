
def parse_fasta(f, index=False):

	headarr = []
	seqarr = []
	tmp_val = []

	fdict = {}

	for line in f:

		if line[0] == '>':
			headarr.append(line.rstrip())
			if len(tmp_val) > 0:
				seqarr.append('\n'.join(tmp_val))
				if index:
					fdict[headarr[-1]] = seqarr[-1]
		else:
			tmp_val.append(line.rstrip())

	seqarr.append('\n'.join(tmp_val))
	if index:
		fdict[headarr[-1]] = seqarr[-1]

	assert (len(seqarr) == len(headarr))

	if index:
		return fdict
	else:
		return headarr, seqarr


def index_data(ka, va):


	fdict = {}
	for k, v in zip(ka, va):
		fdict[k] = v
	return fdict


import sys
