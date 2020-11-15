#!python3 

import docx # python_docx module
import PyPDF2 # PyPDF2 module
import os
import pprint
import math
import re

debug = True

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


# (Sebi) function that helps at text splitting

def listToString(data):
    stringGol = ""
    for cuvant in data:
        stringGol += cuvant
        stringGol += ' '
    
    return stringGol



def calculateEntropy(data):

    # (Sebi) split the text in words and add them to the dictionary
    # after that apply the formula

    dictionar = dict()

    total = 0

    separatori = "—,./?!-_)(*&^%$#@\"\'"
    for separator in separatori:
        data = data.split(separator)
        data = listToString(data)

    data = data.lower()
    data = data.split()

    for cuvant in data:
        if cuvant in dictionar:
            dictionar[cuvant] += 1
        else:
            dictionar[cuvant] = 1


    total = 0
    for (k, val) in dictionar.items():
        total += val

    if debug:
        print("Total:", total)
        pprint.pprint(dictionar)

    #calculate entropy
    entropy = 0.0

    for (k, val) in dictionar.items():
        probab = (val / total) / 2
        entropy += probab * math.log2(1 / probab)
    return entropy

e = calculateEntropy(getText('Ioan Slavici.docx')) # 92844


print('Entropie:', e)

