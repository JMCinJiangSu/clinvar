# ! /usr/bin/python3
# -*- coding = utf-8 -*-

import re
import os

clinvar = "variant_summary.txt"
file = open('mutation2.txt', 'w+')
g = open('genes.txt', 'r')
gene = g.read()
genes = gene.split('\n')
genes = sorted(genes)

with open(clinvar, 'r') as f:
	for line in f:
		line = line.strip()
		array = line.split('\t')
		for i in genes:
			if i in array:
				file.write(i+'\t'+array[2]+'\n')
				print(i)
			
file.close()


