# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 23:46:54 2023

@author: User
"""
import pandas as pd
import polars as pl
import numpy as np
import re

def clean_number(arr):
    cleaned_arr = []
    for x in arr:
        x = x.replace("(", "").replace(") ", "").replace("-", "").replace("(", "")
        cleaned_arr.append(x)
        cleaned_arr = [int(x) if x.isdigit() else x for x in cleaned_arr]
        return cleaned_arr
    

with open(r"C:\Users\User\Downloads\KSBL python\file.txt", "r") as f:
    contents = f.read()
    lines = contents.split("\n")

clean_list = [s for s in lines if s.strip() != '']
clean_list = [s for s in lines if s.strip() != '']
clean_list=[re.sub("-", "", s)for s in clean_list]
clean_number(clean_list)
name=[]
accredation=[]
address=[]
email=[]
contact=[]
website=[]
distance=[]
remaining=[]
cl=[]
for x in clean_list:
    if x.find("@") != -1:
        email.append(x)
    elif x.find(".com") != -1 or x.find(".org") != -1 or x.find(".edu") != -1 or x.find("www.") != -1:
        website.append(x)
    elif x.find("miles") != -1:
        distance.append(x)
    elif x.find("Accredited") != -1 or x.find("Certified") != -1:
        accredation.append(x)
    elif x.isdigit() or x.startswith("("):
        contact.append(x)
    elif x.find("Clinic Logo")!=-1:
        pass
    else:
        remaining.append(x)
        # name.append(remaining[1])
        # remaining.clear()
# print(clean_list)
print("name",name)
print("accredation",accredation)
print("address",address)
print("email",email)
print("contact",contact)
print("website",website)
print("distance",distance)
print("remaining",remaining)
# mega_list = list(zip(name, accredation, address, email, contact, website, distance))
# df = pd.DataFrame(mega_list, columns=['Name', 'Accredation', 'Address', 'Email', 'Contact', 'Website', 'Distance'])
# print(df)
# df.to_csv(r"C:\Users\User\Downloads\KSBL python\df.csv")