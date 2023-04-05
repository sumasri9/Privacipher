import sys
import glob
import re
import spacy.cli
from commonregex import CommonRegex
import en_core_web_sm

a =[]
a = sys.argv
path = ''
redacted_path = ''
status = ''
for i in range(len(a)):
    if a[i] == '--input':
        path += a[i+1]
    if a[i] == '--output':
        redacted_path += a[i+1]
    if a[i] == '--stats':
        status += a[i+1]
b=glob.glob(path)
block = '\u2588'
def phone_number(text):
    regex1 = r"(?:[0-9]{3}[-.]|\([0-9]{3}\))?[0-9]{3}[-.][0-9]{4}\b"
    phone_numbers = re.findall(regex1, text)
    return phone_numbers
def gender(text):
    c = ['he','him','she','her','mother','father','sister','brother','lady','boy','girl','man','woman']
    d=[]
    for cc in c:
        if cc in text:
            d.append(cc)
    return d   
def date(text):
    text = CommonRegex(text)
    dates_list = text.dates
    return dates_list
def names(text):
    #spacy.cli.download('en_core_web_sm')
    nlp= en_core_web_sm.load()
    doc = nlp(text)
    namess = []
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            namess.append(ent.text)
    return namess
def address(text):
    text = CommonRegex(text)
    address = text.street_addresses
    return address
def redact(text,total):
    for word in total:
        redacted_word = block * len(word)
        text = text.replace(word, redacted_word)
    return text
for file in b:
    with open(file, 'r',encoding="utf-8") as file:
        text = file.read()
        stats = ''
        stats += str(file) + "\n"
        phones = phone_number(text)
        if(len(phones)==0):
            stats += "This file doesn't have phone numbers to be redacted \n"
        else:
            stats += "Total number of phone numbers redacted are "
            stats += str(len(phones)) + "\n"
        x = gender(text)
        if(len(x)==0):
            stats += "This file doesn't have genders to be redacted \n"
        else:
            stats += "Total number of genders redacted are "
            stats += str(len(x)) + "\n"
        dates = date(text)
        if(len(dates)==0):
            stats += "This file doesn't have dates to be redacted \n"
        else:
            stats += "Total number of dates redacted are "
            stats += str(len(dates)) + "\n"
        z = names(text)
        if(len(z)==0):
            stats += "This file doesn't have names to be redacted \n"
        else:
            stats += "Total number of names redacted are "
            stats += str(len(z)) + "\n"
        add = address(text)
        if(len(add)==0):
            stats += "This file doesn't have addresses to be redacted \n"
        else:
            stats += "Total number of addresses redacted are "
            stats += str(len(add)) + "\n"
        total = phones + x + dates + z + add
        stats += "total number of redaction in this file are "
        stats += str(len(total)) + "\n"
        suma = redact(text,total)
        new_file = file.name + ".redacted"
        paths = redacted_path + new_file
        with open(paths , 'w') as f:
            f.write(suma)
        if status == 'stderr':
            sys.stderr.write(stats)
        
