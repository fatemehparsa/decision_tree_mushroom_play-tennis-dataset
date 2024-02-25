# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:50:46 2020

@author: fatemeh parsa
main program
"""
import pandas as pd


data_path="data\PlayTennis.csv"
data=pd.read_csv(data_path,sep=',')

print(data)
