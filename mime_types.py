MIME_TYPES = { "kmerdb": "application/octet-stream", "pdf": "", "jpeg": "",  "gz": "", "txt": "text/plain", "README": "text/plain" }

def get_mime(key):

	return MIME_TYPES[key]
