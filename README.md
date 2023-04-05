# cs5293sp23-project1
Name - Suma Sri Chowdary Atheti

### Project Description - In this project we take multiple text files and redact sensitive information such as names, phone numbers, gender, dates and addresses from it and save the redacted data into a new file with .redacted extension. The process of redaction is often expensive and can be used widely for police reports, emails and many more. In this project we have taken sample files of emails and redacted sensitive information from it.
### How to install
Python version - 3.10
### required libraries
pipenv install spacy
pipenv install re
pipenv install glob
pipenv install commonregex
### How to run
we can run the project usingthe following command - 
pipenv run python redactor.py --input '*.txt' --names --dates --phones --genders --address --output 'files/' --stats stderr
