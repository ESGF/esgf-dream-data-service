from json import load, dumps

def proc_json(f, args):

	if (type(f) is file):

		obj = load(f)

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

	if args('do_index') == 'true':

		parse_fasta(f)
	else:
		
	if args.get('action') == "len":
		return len()
