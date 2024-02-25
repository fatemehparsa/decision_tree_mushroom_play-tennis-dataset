# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:25:30 2020

@author: fatemeh parsa

gain module
"""
import entropy as en


def gain(a,data):
    A=data[a]
    V = list(dict.fromkeys(A))
    ES=en.entropy (a,'s',data)
    S=A.size
    sigma = 0
    for i in range(0, len(V)):
        EV=en.entropy(a, V[i],data)
        SV=en.sum_yes_no
        sigma += (SV/S)*EV    
    gain_a=ES-sigma
    print ("gain ",a,"is:",gain_a)
    return gain_a

