# ! /usr/bin/python3
# -*- coding = utf-8 -*-

import re
import os
from collections import Counter
import pandas as pd
import numpy as np

df = pd.read_excel('mutation2.xlsx')
df = df[['Gene', 'Transcript']]
g = open('genes.txt', 'r')
gene = g.read()
genes = gene.split('\n')
genes = sorted(genes)

dic = {}
for i in genes:
    nm = []
    for j in df.index:
        if i == df.loc[j, 'Gene']:
            nm.append(df.loc[j, 'Transcript'])
    dic[i] = nm
    print(i)

dic2 = {}
for k,v in dic.items():
    a = Counter(v)
    dic2[k] = a
    print(k)

file = open('count2.txt', 'w+')
for k,v in dic2.items():
    file.write(str(k)+'\t'+str(v)+'\n')
file.close()