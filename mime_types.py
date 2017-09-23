MIME_TYPES = { "kmerdb": "application/octet-stream", "pdf": "application/pdf",
	       "jpeg": "image/jpeg",  "gz": "application/x-gzip", 
	       "txt": "text/plain", "README": "text/plain",
	       "nc": "application/x-netcdf", "ncl": "text/ncl", 
	       "f90": "text/x-fortran", "json": "text/json" }

def get_mime(path):


	parts = path.split('.')
	
	key = parts[-1]

	if key in MIME_TYPES:
		return MIME_TYPES[key]
	else:
		return ""
