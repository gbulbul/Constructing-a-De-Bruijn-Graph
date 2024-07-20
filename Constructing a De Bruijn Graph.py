# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:14:21 2024

@author: gbulb
"""

class Constructing_a_De_Bruijn_Graph:
    def find_triples(list_of_strings):
        list_1=[]
        list_2=[]
        tup=[]
        for i,idx in enumerate(list_of_strings):
            for j,idy in enumerate(list_of_strings):
                if idx!=idy:
                   if (idy[1:4],idx[0:3]) not in tup and (idx[0:3],idy[1:4]) not in tup and idx[0:3]!=idy[1:4] and idx[0:2]!=idy[1:3] and idx[1:3]!=idy[2:4] and idx[0]!=idy[1] :
                       list_1.append(idx[0:3])
                       list_2.append(idy[1:4])
                       tup = list(zip(list_1, list_2))
        return tup
    def find_pair_of_triples(tup):
        for i,idx in enumerate(tup):  
            print(f'({idx[0]},{idx[1]})')
if __name__=="__main__":    
    import pandas as pd
    string1,string2,string3,string4,string5,string6='TGAT','CATG','TCAT','ATGC','CATC','CATC'
    list_of_strings=[string1,string2,string3,string4,string5,string6]
    tup=Constructing_a_De_Bruijn_Graph.find_triples(list_of_strings)
    Constructing_a_De_Bruijn_Graph.find_pair_of_triples(tup)
    
    
 