from json import load

def proc_json(f, args):

	obj = load(f)

	qlens = args.get('querylen')

	if len(qlens) > 0:

		qleni = int(qlens)

		for i in range(1, qleni+1):

			qq = args.get(query + str(i))

			objnew = None
			if type(obj) is dict:
				if qq in obj:
					objnew = obj[qq]
				else:
					raise BasicException("NotFound")
			elif type(obj) is list:
				idx = int(qq)
				if idx < len(obj):
					objnew = obj[idx]
				else:
					raise BasicException("OutOfBounds")
			else:
				raise BasicException("TypeError")
			if objnew is None:
				raise BasicException("FailToAssign")
			obj = objnew

	if args.get('action') == "type":

		if type(obj) is dict:
			return "dict"
		elif  type(obj) is list:
			return "list"
		else:
			return "scalar"
	elif args.get('action') == "query":
		return obj
	elif args.get('action') == "len":
		return len(obj)
	elif args.get('action') == "keys":
		return obj.keys() # assume exception gets caught for now
	

	return None





