# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:49:20 2023

@author: samad_chalchal
"""

import pandas as pd
import polars as pl
import numpy as np
import re

with open(r"C:\Users\User\Downloads\KSBL python\file.txt", "r") as f:
    contents = f.read()
    lines = contents.split("\n")

clean_list = [s for s in lines if s.strip() != '']
clean_list=[re.sub("-", "", s)for s in clean_list]

def extractDigits(lst):
    res = []
    for el in lst:
        sub = el.split(', ')
        res.append(sub)
     
    return(res)
cleaned_list_list=(extractDigits(clean_list))

clinic_logo_index = [i for i,sublist in enumerate(clean_list) if 'Clinic Logo' in sublist]
mile_index = [i for i,sublist in enumerate(clean_list) if ' mile' in sublist]

text_list=[]
for x in range(len(clinic_logo_index)):
    text_list.append(clean_list[clinic_logo_index[x]:mile_index[x]+1])
    print(text_list)
name=[]
accredation=[]
address=[]
email=[]
contact=[]
website=[]

for line in text_list:
    if len(line) >= 5:
        _, username, _, _, email_address = line[:5]
        name.append(username)
        email.append(email_address)

    
print("name",name)
print("email",email)
mega_list = list(zip(name,email))
df = pd.DataFrame(mega_list, columns=['Name','Email'])
print(df)
df.to_csv(r"C:\Users\User\Downloads\KSBL python\df.csv")

    
    

