# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:54:23 2021

@author: Nirodya Pussadeniya
Data Science Internship - Task @Kainovation Technologies

"""

#importing necessary libraries
from pdfminer.high_level import extract_text
import spacy
import re

#Defining the ssential variables to identify phone numbers and email addresses
PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

#Taking user input- file path
pdf_path= input("Enter your file path:")

#Defining fnction to extraxt the text from pdf
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

#Extracting text from the pdf
txt=extract_text_from_pdf(pdf_path)

#Opening a new text file to write data
text_file=open("resume_text.txt",mode="w",encoding="utf-8")
#Write all the data in cv in text filee 
text_file.write(txt)    
#Closing text file
text_file.close()

#Defining function to extarct phone numbers from text
def extract_phone_number(resume_text):
    phone = re.findall(PHONE_REG, resume_text)
    if phone:
        number = ''.join(phone[0])
        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None

#Defining function to extarct emails from text
def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)

#Defining function to extarct person names from text
person=[]
def extract_name(resume_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(txt)
    for token in doc:
        if token.pos_=='PROPN':
            person.append(token.text)
    return person

#Calling the functions 
if __name__ == '__main__':
    
    #Opening a new text file to write data
    text_file=open("data.txt",mode="w",encoding="utf-8")
    
    #Calling extract_name function to extract name
    names=extract_name(txt)
    if names:
        print("\n")
        print('Name: '+ names[0],names[1])
        
        #Write name on text file
        text_file.write("Name: "+ names[0])
        text_file.write(" "+names[1])
    
    #Calling extract_emails function to extract emails
    emails = extract_emails(txt)
    if emails:
        print('\nEmail: '+emails[0])
        
        #Write emails on text file
        text_file.write('\nEmail: '+emails[0])
    
    #Calling extract_phone_number function to extract phone number
    phone_number = extract_phone_number(txt)
    if phone_number:
        print('\nPhone number: '+phone_number)
        
        #Write phone number on text file
        text_file.write('\nPhone number: '+phone_number )
    
    #Closing text file
    text_file.close()