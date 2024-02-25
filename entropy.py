# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:57:18 2020

@author: fatemeh parsa

intropy module
"""
import math as m

def entropy(a,v,data):
    global AY,A,Y,count ,V,num_no_v,num_yes_v,sum_yes_no
    num_yes_v=0
    num_no_v=0
    sum_yes_no=0
    if v=='s':             
        Y=data[list(data.columns)[-1]]
        count=Y.value_counts()
        j=0
        for i in count:
            if count.index[j]==('Yes'):               
                num_yes_v= count['Yes']
                
            elif count.index[j]==('No'):
                num_no_v= count['No']                
            j=j+1        

    else: 
        A=data[a]
        Y=data[list(data.columns)[-1]]
        AY=A.copy()
        V=v
        for i in range (0,len(Y)):
            
            AY[i]=(A[i],Y[i])
            count=AY.value_counts()

        j=0
        for i in count:
            if count.index[j]==(V, 'Yes'):               
                num_yes_v= count[V, 'Yes']
                
            elif count.index[j]==(V, 'No'):
                num_no_v= count[V, 'No']
                
            j=j+1

    sum_yes_no= num_no_v + num_yes_v

    if num_no_v==0 :
        entropy_a=-(num_yes_v/sum_yes_no)*m.log2(num_yes_v/sum_yes_no)
    elif num_yes_v==0 :
        entropy_a=-(num_no_v/sum_yes_no)*m.log2(num_no_v/sum_yes_no)       
    else :
        entropy_a=-(num_yes_v/sum_yes_no)*m.log2(num_yes_v/sum_yes_no)-(num_no_v/sum_yes_no)*m.log2(num_no_v/sum_yes_no)
    print ("entropy ",v,entropy_a)
    return entropy_a




