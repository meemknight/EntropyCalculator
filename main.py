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

#todo (Vlod): count letters and apply the formula
def calculateEntropyLetters(data, n=1):

# remove non romanian letters and space
# remove double space "  "
# ana are mere -> "an na a.  .a re e."  -> grup de 2 exemplu
# make 2 modes: one with spaces one without

    d = dict()

    total = 0

    # Construim aici sirul de caractere ce ulterior va reprezenta cheia dictionarului
    # Practic folosim aceasta lista ca sa grupam caracterele textului cate n (parametrul functiei)
    charList = []

    i = 0

    while i < len(data):
        char = data[i]


        isValidCharacter = bool(re.search("[a-zţşăîâ ]", char, re.IGNORECASE))
        if isValidCharacter:
            charList.append(char)

        
        if len(charList) == n:
            s = "".join(charList)
            d.setdefault(s.lower(),0)  
            d[s.lower()] += 1
            charList = []
            i -= (n-1)
        
        i += 1

    total = 0
    for (k, val) in d.items():
        total += val

    if debug:
        print("Total:", total)
        pprint.pprint(d)

    #calculate entropy
    entropy = 0.0

    for (k, val) in d.items():
        probab = val / total
        entropy += probab * math.log2(1/probab)

    return entropy

# f1 = calculateEntropyLetters(getText('Ioan Slavici.docx'))

# print('f1:', f1)

e = calculateEntropyLetters("Ana are", 2)

# e = calculateEntropyLetters(getText('Ioan Slavici.docx'), 2)

print('Entropie:', e)