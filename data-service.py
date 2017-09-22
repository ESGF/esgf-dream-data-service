from flask import Flask, request, abort, make_response
from time import sleep
#from json import loads
import os


from mime_types import get_mime
from data_roots import convert_path


app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    response = make_response("<h1>ESGF DREAM DATA SERVICE</h1>")    
    return (response)

@app.route('/', methods=['GET'])
def feedback_srv():
    
    urlpath = request.path
    # Use ESGF configured roots mappings - same as THREDDS
    phys_path = convert_path(urlpath) 

    if phys_path == "":
        abort(404)
         
    resp_file = None

    try:
        resp_file =open(phys_path)
    except Exception as e:

        response = make_response("Error opening file on server: " + str(e), status="500")
        return (response)

    response = make_response(resp_file.read())
    response.headers['Content-Type'] = get_mime(phys_path)

    return (response)


if __name__ == '__main__':
    app.run()

