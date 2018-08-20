import sys, numpy

fn = ""

files_idx = []
files_spt = []
parse_times = []
index_times = []
tot_times = []

indexing = False
pres = 0
i_phase = False

for line in open(sys.argv[1]):

    parts = line.split()

    if parts[0] == "processing":

        fn = parts[1] 
        indexing = parts[3].rstrip() == "True"

        i_phase = False
    else:

        if indexing == True:

            res = float(line.rstrip())
            if fn in files_idx:
                idx = files_idx.index(fn)
                tot_times[idx].append(res)
            else:
                files_idx.append(fn)
                tot_times.append([res])
        else:
            if i_phase:

                res = float(line.rstrip())
                if fn in files_spt:
                    idx = files_spt.index(fn)
                    index_times[idx].append(res)
                    parse_times[idx].append(pres)
                else:
                    files_spt.append(fn)
                    index_times.append([res])
                    parse_times.append([pres])
            else:
                if line.rstrip() == "index phase":
                    i_phase = True
                else:
                    pres = float(line.rstrip())

for fn, ta in zip(files_idx, tot_times):

    print fn, numpy.sum(ta), 0, 0

for fn, pa, ia in zip(files_spt, parse_times, index_times):

    npa = numpy.array(pa)
    nia = numpy.array(ia)
    print fn, numpy.mean(npa + nia ), numpy.mean(pa), numpy.mean(ia)
