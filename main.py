#!python3 

import docx # python_docx module
import PyPDF2 # PyPDF2 module
import os
import pprint

def readDOCX(path):
    d = docx.Document(path)

    text = ""
    l = []
    for p in d.paragraphs:
        l.append(p.text)

    text = '\n'.join(l)
    return text

def readPDF(path):
    f = open(path, 'rb')

    l = []
    pdf = PyPDF2.PdfFileReader(f)
    print(path, pdf.numPages)

    for i in range(pdf.numPages):
        l.append(pdf.getPage(i).extractText())

    f.close()

    return '\n'.join(l)



def getText(path):
    if(not os.path.isfile(path)):
        return ''

    if path.lower().endswith('.docx'):
        return readDOCX(path)
    if path.lower().endswith('.pdf'):
        return readPDF(path)

#todo (Vlod): count letters and apply the formula
def calculateEntropyLetters(data):

    d = dict()

    for i in data:
        d.setdefault(i,0)  
        d[i] += 1

    pprint.pprint(d)

    return None

calculateEntropyLetters(getText('Document1.docx'))