# For now use a hardcoded test dictionary
# TODO: convert to use esg.ini setting

ESGF_ROOTS = { "esgf_data": "/esg/data"}



def convert_path(in_path):


	parts = in_path.split('/')
	if len(parts) < 1:
		return ""
	logical_root = parts[0]

	if not logical_root in ESGF_ROOTS:
		return ""
	phys_root = ESGF_ROOTS[logical_root]

	return '/'.join([phys_root] + parts[1:] )
	
