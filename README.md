# cs5293sp23-project1
### Name - Suma Sri Chowdary Atheti

### Project Description - In this project we take multiple text files and redact sensitive information such as names, phone numbers, gender, dates and addresses from it and save the redacted data into a new file with .redacted extension. The process of redaction is often expensive and can be used widely for police reports, emails and many more. In this project we have taken sample files of emails and redacted sensitive information from it.



https://user-images.githubusercontent.com/124108020/229971135-3a71afc6-b2a7-47a3-86d7-41785f1cd59e.mov


### Requirements
Python version - 3.10

#### required libraries
```
pipenv install spacy
pipenv install re
pipenv install glob
pipenv install commonregex
```

### How to run

#### Command to run the project - 
#### pipenv run python redactor.py --input '*.txt' --names --dates --phones --genders --address --output 'files/' --stats stderr
Here, the argument after --input is the location of the input text files that are to be redacted.
--names, --dates , --phones, --genders, --address are to be redacted. --output is the location of the files that are to be stored after redaction. --stats shows the statistics of how many words are redacted from which file.

#### Command to run test cases - pipenv run python -m pytest

## Functions -
The logic of the code is written in redactor.py file
We use a for loop to traverse each file from a folder and call the desired functions to extract the sensitive information from the text file.

### phone_number()
This function returns the phone numbers of the pattern XXX-XXX-XXX and (XXX)XXX-XXX.
```
def phone_number(text):
    regex1 = r"(?:[0-9]{3}[-.]|\([0-9]{3}\))?[0-9]{3}[-.][0-9]{4}\b"
    phone_numbers = re.findall(regex1, text)
    return phone_numbers
```
Phone_number function takes the contents of the text file as input and returns phone numbers matching the regular expression from the context. 

### gender()
This function returns the words that describe the gender of a person such as he, she, her, him, etc.
```
def gender(text):
    c = ['he','him','she','her','mother','father','sister','brother','lady','boy','girl','man','woman']
    d=[]
    for cc in c:
        if cc in text:
            d.append(cc)
    return d 
```
The gender function takes the content of the text file as input and return if the words specified in the list are present.

### date()
This function returns the dates present in the text file.
```
def date(text):
    parsed_text = CommonRegex(text)
    dates_list = parsed_text.dates
    return dates_list
```
The date function takes the contents of the text as input and returns all formats of dates present in CommonRegex library if present in the text file.

### address()
This function returns the street addresses present in the text file.
```
def address(text):
    parsed_text = CommonRegex(text)
    st_address = parsed_text.street_addresses
    return st_address
```
The address function takes the contents of the text as input and returns street addresses present in the text file.

### name()
This function retunrs names present in the email.
```
def names(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    namess = []
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            namess.append(ent.text)
    return namess
```
The name function takes the contents of the file as input and returns names present in the text file. It uses spacy library to identify the names present in the text file.

### redact()
Redact function takes all the returned values from the above functions, replaces them with a block and returns the redacted file content.This redacted file content is put into a new file with .redacted extension appended to it.
```
def redact(text,total):
    for word in total:
        redacted_word = block * len(word)
        text = text.replace(word, redacted_word)
    return text
```

### stats
After the process of redaction, all the words redated from each file are printed to stderr in the below format.
```
<_io.TextIOWrapper name='6.txt' mode='r' encoding='utf-8'>
This file doesn't have phone numbers to be redacted 
Total number of genders redacted are 5
Total number of dates redacted are 1
Total number of names redacted are 6
Total number of addresses redacted are 1
total number of redaction in this file are 13
```
First line is the name of the file followed by the summary of the redaction process and last line is the total number of words redacted in a file.

### test cases
In pytest.py file we check if each function from redactor.py returns a value.

### Assumptions
1. Phone number following XXX-XXX-XXX and (XXX)XXX-XXX pattern are only extracted.
2. For specifying the gender the words present in the list are only considered.
3. Addresses the follow the pattern of street_addresses from common regex library are only identified and redacted from the text file.

### Bugs
1. while downloading en_core_web_sm using the command 'pipenv install en_core_web_sm' i faced few path issues. Therefore, if facing the same issues, please uncomment line number 38 in redactor.py that will download en_core_web_sm in the desired path and will run the code. 
