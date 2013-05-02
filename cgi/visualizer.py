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

scriptPath = "/var/www/clusterator/core/"
sys.path.append(scriptPath)

from util import Util
from tokenator import Tokenator
docWordsStruct = Util().getFileContent("/var/www/clusterator/examples/TEST.DAT")

matrix = Tokenator().createTermFrequencyMatrix(docWordsStruct);

html = "<table border='1'><tbody>"

for doc in matrix:
    html = html + "<tr><td>"+doc+"</td>"

    for word in matrix[doc]:
        html = html + "<td>" + word + ":" + str(matrix[doc][word])  +"</td>"

    html = html + "</tr>"

html = html + "</tbody></table>"
#print(json.dumps(message,indent=1))
print(html)