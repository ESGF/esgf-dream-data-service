from flask import Flask, request, abort, make_response
from time import sleep


#from json import loads
import os


from mime_types import get_mime
from convert_path import convert_path
from proc import *

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def feedback_srv(path):

    if path == "":
        response = make_response("<h1>ESGF DREAM DATA SERVICE</h1>") 
        #URL: " + urlpath + "<p>PATH:" + phys_path )     #
        return (response)                                                #

    urlpath = path

    # Use ESGF configured roots mappings - same as THREDDS
    phys_path = convert_path(urlpath) 

    if phys_path == "":
        abort(404)
         
    resp_file = None


    if not os.path.exists(phys_path):
        abort(404)

    if os.path.isdir(phys_path):
        abort(400)

    try:
        
       resp_file =open(phys_path)
    except Exception as e:

        response = make_response("Error opening file on server: " + str(e), 500)
        return (response)

    mime = get_mime(phys_path)

    arrggs = request.args


    # TODO - better error handling passed back

    # if not json
    action= arrggs.get('action')
    if ( not (action is None ) ) and len(action) > 0:


        if "json" in mime:
            
            try:
                    
                jobj = proc_json(resp_file, arrggs)

            except BaseException as e:
                return(make_response("Bad Request querying JSON: " + str(e), 400))

            if jobj is None:
                return(make_response("Bad Request querying JSON", 400))

            return(make_response(jobj))
        elif "fasta" in mime:

            resp = proc_fasta(resp_file, arrggs)

            if resp is None:
                return(make_response("Bad Request querying FASTA: '" + action +"'" , 400))
            return (make_response(resp))

    response = make_response(resp_file.read())

    if len(mime) > 0:
        response.headers['Content-Type'] = mime

    return (response)


if __name__ == '__main__':
    app.run()

