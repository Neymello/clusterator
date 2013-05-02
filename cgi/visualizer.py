#!/usr/bin/python
"""

CGI

"""
import cgi
import json,sys,os

fs = cgi.FieldStorage()

#print("Content-Type: application/json\n\n")
print("Content-Type: text/html\n\n")
print()


# A nested FieldStorage instance holds the file
fileitem = fs['file']

# Test if the file was uploaded
if fileitem.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(fileitem.filename)

   open('/var/www/clusterator/files/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'


#print(json.dumps(message,indent=1))
print(message)