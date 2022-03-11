# ! /usr/bin/python3
# -*- coding = utf-8 -*-

import os
import pandas as pd
import numpy as np
import re
import openpyxl
import datetime

# 先对原始数据进行清洗，删除Name列不是NM开头的行
def clean(df):
	df2 = pd.DataFrame(columns = df.columns)
	m = 0
	for i in df.index:
		if 'NM_' in df.loc[i, 'Name']:
			df2.loc[m] = df.loc[i]
			m += 1
	return df2

def extract(df, germgenes):
	colnames = ['Gene', 'Transcript', 'DNA_change', 'Protein_change', 'Significance']
	GRCh37 = pd.DataFrame(columns = colnames)

	k = 0
	for i in df.index:
		for j in germgenes:
			if j == df.loc[i, 'GeneSymbol']:
				GRCh37.loc[k, 'Transcript'] = ''.join(re.findall(r'(.*?)[\(]', df.loc[i, 'Name'].split(':')[0]))
				GRCh37.loc[k, 'Gene'] = j
				GRCh37.loc[k, 'DNA_change'] = ''.join(re.findall(r'(.*?)[\(]', df.loc[i, 'Name'].split(':')[-1]))
				GRCh37.loc[k, 'Protein_change'] = ''.join(re.findall(r'[\(](.*?)[\)]', df.loc[i, 'Name'].split(':')[-1]))
				GRCh37.loc[k, 'Significance'] = df.loc[i, 'ClinicalSignificance']
		k += 1
	return GRCh37

def contents(name):
	cont = []
	with open(name) as f:
		for line in f:
			line = line.strip()
			cont.append(line)
	return cont


def main():
	germgenes = contents('germgene.txt')

	title = []
	with open('variant_summary.txt') as f:
		for i in range(1):
			title.append(f.readline())

	GRCh37 = []
	GRCh37.append(title[0])
	GRCh38 = []
	GRCh38.append(title[0])
	with open('variant_summary.txt') as f:
		for line in f:
			for j in germgenes:
				if ('GRCh37' in line) and (j in line):
					GRCh37.append(line)
					
	f = open('GRCh37.txt', 'w+')
	f.write(''.join(GRCh37))
	f.close()

	df = pd.read_table('GRCh37.txt', dtype = 'str')
	df2 = clean(df)
	GRCh37 = extract(df2, germgenes)

	writer = pd.ExcelWriter('GRCh37.xlsx', engine = 'openpyxl')
	GRCh37.to_excel(writer, index = False)
	writer.save()



if __name__ == '__main__':
	starttime = datetime.datetime.now()
	main()
	end = datetime.datetime.now()
	print(end-starttime)
