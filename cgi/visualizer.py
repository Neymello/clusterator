#!/usr/bin/python
"""

CGI

"""
import cgitb,cgi
import json,sys,os

cgitb.enable()

fs = cgi.FieldStorage()

#print("Content-Type: application/json\n\n")
print("Content-Type: text/html\n\n")
print

scriptPath = "/var/www/clusterator/core/"
sys.path.append(scriptPath)

import util
import tokenator
docWordsStruct = util.getFileContent("../examples/TEST.DAT")

matrix = tokenator.createTermFrequencyMatrix(docWordsStruct);

html = "<table border='1'><thead><tr><th>DOC ID</th><th>TERMS</th></tr></thead><tbody>"

for doc in matrix:
    html = html + "<tr><td>"+doc+"</td>"

    for word in matrix[doc]:
        html = html + "<td>" + word + ":" + str(matrix[doc][word])  +"</td>"

    html = html + "</tr>"

html = html + "</tbody></table>"
#print(json.dumps(message,indent=1))
print(html)
