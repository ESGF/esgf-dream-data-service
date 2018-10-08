from json import load, dumps

from parse_fasta import parse_fasta

from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()


def proc_json(f, args):

	if (type(f) is file):

		fname = f.name

		obj = cache.get(fname)

		if res is None:
			obj = load(f)
			cache.set(fname, obj)

	else:
		raise BaseException("Process-Request-Called-Without-Open-File")

	qlens = args.get('querylen')

	if (not qlens is None) and  len(qlens) > 0:

		qleni = int(qlens)

		for i in range(1, qleni+1):

			qq = args.get('query' + str(i))

			objnew = None
			if type(obj) is dict:
				if qq in obj:
					objnew = obj[qq]
				else:
					raise BaseException("NotFound")
			elif type(obj) is list:
				idx = int(qq)
				if idx < len(obj):
					objnew = obj[idx]
				else:
					raise BaseException("OutOfBounds")
			else:
				raise BaseException("TypeError")
			if objnew is None:
				raise BaseException("FailToAssign")
			obj = objnew

	if args.get('action') == "type":

		if type(obj) is dict:
			return "dict"
		elif type(obj) is list:
			return "list"
		else:
			return "scalar"
	elif args.get('action') == "query":
		return dumps(obj)
	elif args.get('action') == "len":
		return str(len(obj))
	elif args.get('action') == "keys":
		return dumps(obj.keys()) # assume exception gets caught for now
	

	return None


def proc_fasta(f, args):

	fdict = {}
	headers = []
	seq = []


	if (type(f) is file):

			fname = f.name

			obj = cache.get(fname)

			if res is None:
				if args.get('do_index') == 'true':

					res = parse_fasta(f, True)
					fdict=res
				else:
					res = parse_fasta(f, False)
					headers, seq = res		

				cache.set(fname, res)
			else:
				if args.get('do_index') == 'true':
					fdict = res
				else:
					headers, seq = res		

		else:	
			raise BaseException("Process-Request-Called-Without-Open-File")

	if args.get('action') == "len":
		return str(len(headers))
	if args.get('action') == "get_headers":
		return dumps(headers)
	if args.get('action') == "get_seqat":
		idxs = args.get('index')

		if (not idxs is None) and  len(idxs) > 0:
			idxi = int(idxs)
		else:
			return None			
		return dumps({ "header": headers[idxi], "sequence": seq[idxi]})


	return None
