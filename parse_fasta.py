
def parse_fasta(f, index=False):

	headarr = []
	seqarr = []
	tmp_val = []

	fdict = {}

	assert (type(f) == file)
	for line in f:

		if line[0] == '>':
			header = line.rstrip()
			headarr.append(header)
			if len(tmp_val) > 0:
				seqarr.append('\n'.join(tmp_val))
				
				if index:
					fdict[header] = tmp_val
				tmp_val = []
		else:
			tmp_val.append(line.rstrip())

	seqarr.append('\n'.join(tmp_val))
	if index:
		fdict[header] = tmp_val

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


