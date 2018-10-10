# esgf-dream-data-service
A file data server for the DREAM project and ESGF

## Prequistites

ESGF datanode installation or Python 2.7 with required modules (see requirememts.txt)

## Installation


git clone this repo to your server.  Fix permissions to ensure the user is running.


    cd esgf-dream-data-server
    chmod a+r *.py


For testing you can run the data service as a standalone application.  You'll need to run (ensure you have flask installed in your test python):

     $ python dream_data.py

This will run a server on port 5000, and you can test without published datasets

For integration testing you will need to setup the dream-data server endpoint in your esgf-httpd.conf.




