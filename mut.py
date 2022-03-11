# ! /usr/bin/python3
# -*- coding = utf-8 -*-

import re
import os

clinvar = "variant_summary.txt"
file = open('mutation.txt', 'w+')
g = open('genes.txt', 'r')
gene = g.read()
genes = gene.split('\n')
genes = sorted(genes)

with open(clinvar, 'r') as f:
	for line in f:
		line = line.strip()
		array = line.split('\t')
		searchObj = re.findall(r'[\(](.*?)[\)]', array[2])
		if searchObj:
			if searchObj[0] in gene:
				file.write(array[2] + '\n')
				print(searchObj[0])
file.close()


