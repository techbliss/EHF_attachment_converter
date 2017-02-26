# -*- coding: utf-8 -*-
import base64
import re
import os
import sys
import xml
import sys
import base64
os.chdir(os.path.dirname(sys.argv[0]))


def mains():

    file = sys.argv[1]

    from xml.dom import minidom

    doc = minidom.parse(file)

    name = doc.getElementsByTagName("cbc:EmbeddedDocumentBinaryObject")[0]
    #get base64 pdfstring so we can convert to pdf
    name2 = doc.getElementsByTagName("cbc:Name")[0]
    #get invoice name
    name3 = doc.getElementsByTagName("cbc:IssueDate")[0]
    #get invoice date

    filename = (name2.firstChild.data)
    filedate = (name3.firstChild.data)
    a = (name.firstChild.data)

    b = base64.urlsafe_b64decode(a.encode('UTF-8'))

    try:
        with open(filename+"."+filedate+"1.pdf") as text_file:
            text_file.write(b)
            pass
    except IOError:
        with open(filename+"."+filedate+".pdf", "wb") as text_file:
            text_file.write(b)


if __name__ == '__main__':
  mains()

