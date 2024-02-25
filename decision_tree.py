# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:26:49 2020

@author: fatemeh parsa
decision tree module
"""
import gain as g
import mainprogram as mp
import numpy as np
import entropy as en


def best_root(data):
    f_list = data.columns
    f_gains = list()
    for i in range(0, len(f_list)-1):
        f_gains.append(g.gain(f_list[i],data))
    f_i = np.argmax(f_gains)
    return f_list[f_i]

class tree_node:
    def __init__(self, name, childs ,parent):
        self.feature_name = name
        self.childs = childs
        self.parent = parent
        tree_nodes_array.append([name, parent])

def decision_tree_f(data,root):
    A=data[root]
    V = list(dict.fromkeys(A))
    for j in range (0,len(V)):
        temp_data= data[data[root]==V[j]].copy()
        temp_data=temp_data.reset_index(drop=True)
        if en.entropy(root,V[j],data)==0:
            y=temp_data.columns[-1]
            answer=temp_data[y][0]
            tree_node( V[j],answer,root)
            tree_node( answer,0,V[j])
            
           
        else:

            new_data=data.copy()
            A=new_data[root]
            V = list(dict.fromkeys(A))   
            dl=len(data[root])
            for i in range (0,dl):            
                if new_data[root].loc[i]!=V[j]:
                    new_data.drop([i],inplace=True)
            new_data=new_data.reset_index(drop=True)
            del new_data[root]     
            new_root=best_root(new_data)
            new_child=list(dict.fromkeys(new_root))
            tree_node( V[j],new_root,root)
            tree_node( new_root,new_child,V[j])            
            decision_tree_f(new_data,new_root)
    return
      
firstroot=best_root(mp.data)
tree_nodes_array=["start"]
A=mp.data[firstroot]
V = list(dict.fromkeys(A))
tree_node( firstroot, V,"start")
decision_tree_f(mp.data,firstroot)
print (tree_nodes_array)





