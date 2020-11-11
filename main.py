#!python3 

import docx # python_docx module
import PyPDF2 # PyPDF2 module
import os
import pprint
import math

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

# remove non romanian letters and space
# remove double space "  "
# ana are mere -> "an na a.  .a re e."  -> grup de 2 exemplu
# make 2 modes: one with spaces one without

    d = dict()

    total = 0

    for i in data:
        if i.isalpha():
            d.setdefault(i.lower(),0)  
            d[i.lower()] += 1

    delVals = []
    for (k, val) in d.items():
        if(val < 5):
            #remove letters that are not from the romanian alfabet
            delVals.append(k)
        else:
            total += val

    for i in delVals:
        del d[i]

    print(total)
    pprint.pprint(d)

    #calculate entropy

    entropy = 0.0

    for (k, val) in d.items():
        probab = val / total
        entropy += probab * math.log2(1/probab)

    return entropy

e = calculateEntropyLetters(getText('Ioan Slavici.docx'))

print('\n', e)