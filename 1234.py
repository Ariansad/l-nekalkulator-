# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 12:40:58 2022

@author: s_ari
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
from joblib import dump, load
import pickle
from PIL import Image



st.write('''
         Boliglånsøknad
         
         ''')
train_data=pd.read_csv('BOLIGDATA/train.csv')
test_data=pd.read_csv('BOLIGDATA/test.csv')
 

model = pickle.load(open('./BOLIGDATA/model.pkl', 'rb'))

def bruker_input():
    
    st.image('https://upload.wikimedia.org/wikipedia/commons/9/99/DNB_ASA.png')
    ## Full Name
    fn = st.text_input('Full Name')
    
## BrukerID
    lånid = st.text_input('Loan_ID')
    
## Kjønn
    kjønnvalg = ('Female','Male')
    valg_av_kjønn = list(range(len(kjønnvalg)))
    kjønn = st.selectbox("Gender",valg_av_kjønn, format_func=lambda x: kjønnvalg[x])

## ekteskap
    giftvalg = ('No','Yes')
    valg_om_gift = list(range(len(giftvalg)))
    ekteskap = st.selectbox("Married", valg_om_gift, format_func=lambda x: giftvalg[x])

#Antall lånere
    antlånerevalg = ('0','1','2','3+')
    valg_av_antlånere = list(range(len(antlånerevalg)))
    lånere = st.selectbox("Dependents",  valg_av_antlånere, format_func=lambda x: antlånerevalg[x])

##Utdanning
    utdanningvalg = ('Not Graduate','Graduate')
    valg_av_utdanning = list(range(len(utdanningvalg)))
    utdanning = st.selectbox("Education",valg_av_utdanning, format_func=lambda x: utdanningvalg[x])

## selvansatt
    selvansattvalg = ('Yes','No')
    valg_av_selvansatt= list(range(len(selvansattvalg)))
    selvans = st.selectbox("Self Employed ",valg_av_selvansatt, format_func=lambda x: selvansattvalg[x])

## Lønn
    lønn = st.number_input("Applicant's Monthly Income($)",min_value=0, value=0)
  
## Kausjonist
    kausjonist = st.number_input("Co-Applicant's Monthly Income($)",min_value=0, value=0)
  
## Mengde lån som vil tas
    lån = st.number_input("Loan Amount",min_value=0, value=0)

## Nedbetalingstid 
    nedbetalingsvalg = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    valg_av_nedbetaling = range(len(nedbetalingsvalg))
    lengde = st.selectbox("Loan duration in days",valg_av_nedbetaling, format_func=lambda x: nedbetalingsvalg[x])

##Kredittscore
    kredittscore = st.number_input("Credit Score",min_value=0.00, max_value=1.00, value=0.00, step=0.01)
##Eiendomsområde
    eiendomvalg = ('Rural','Semi-Urban','Urban')
    valg_av_eiendom = list(range(len(eiendomvalg)))
    eiendom = st.selectbox("Property Area",valg_av_eiendom, format_func=lambda x: eiendomvalg[x])   

    if st.button("Submit"):
        duration = 0
        if lengde == 0:
            duration = 60
        if lengde == 1:
            duration = 180
        if lengde == 2:
            duration = 240
        if lengde == 3:
            duration = 360
        if lengde == 4:
            duration = 480
        features = [[kjønn, ekteskap, lånere, utdanning, selvans, lønn, kausjonist, lån, lengde, kredittscore, eiendom]]
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error(
         "Hello: " + fn +" || "
         "Account number: "+lånid +' || '
         'According to our Calculations, you will not get the loan from Bank'
     )
        else:
            st.success(
         "Hello: " + fn +" || "
         "Account number: "+lånid +' || '
         'Congratulations!! you will get the loan from Bank'
     )

bruker_input()