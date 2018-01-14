# -*- coding: utf-8 -*-
import re
import json
import pandas as pd
import pdb
# construct search str

to_whom=r'\b(?:לי|לך|לו|לה|לנו|לכם|לכן|להם|להן|לכולם|לכולן|לכולכם|לכולכן|לכולנו\w+?\b)'
regex_a = r'(?:\w+\W+){,5}הי[י]?תה\s*?' + to_whom + r'\s+?\bאת\b\W+ה(\w+)(?:\W+\w+){,2}' 
regex_b = r'(?:\w+\W+){,5}הי[י]?תה\s*?' + to_whom + r'\s+?\bה(\w+)\b(?:\W+\w+){,3}' 
regex_c = r'(?:\w+\W+){,5}הי[י]?ה\s*?' + to_whom + r'\s+?\bאת\b\W+ה(\w+)(?:\W+\w+){,2}' 
regex_d = r'(?:\w+\W+){,5}הי[י]?ה\s*?' + to_whom + r'\s+?\bה(\w+)\b(?:\W+\w+){,3}' 
regex_lst = [regex_a, regex_b, regex_c, regex_d]


# init
df_columns = ['id', 'match', 'structure' ,'post_content', 'nickname', 'blogger_age', 'blogger_gender', 'post_title', 'post_date', 'post_hour', 'post_url' ]
nounlist_a,nounlist_b,nounlist_c,nounlist_d = [],[],[],[]
nounlist=[nounlist_a,nounlist_b,nounlist_c,nounlist_d]

# read input file (*.xlsx) and store in pandas.DataFrame:
 
item={}

filename = input("enter file to process:")
ofilename = input("enter *.txt file for output:")
if not filename.strip():
	filename = '..\\work\\israblog_matches_with_identified_structure.xlsx'
if not ofilename.strip():
	ofilename = '..\\work\\israblog_matches_statistics.xlsx'


with pd.ExcelFile(filename) as xls:
	group_a = pd.read_excel(xls, 'group_a')
	group_b = pd.read_excel(xls, 'group_b')
	group_c = pd.read_excel(xls, 'group_c')
	group_d = pd.read_excel(xls, 'group_d')

for i ,group in enumerate([group_a, group_b, group_c, group_d]):
	for match in group.match:
		nounlist[i].append(re.findall(regex_lst[i], match)[0])

writer = pd.ExcelWriter(ofilename,engine='xlsxwriter',options={'strings_to_urls': False})
for i ,group in enumerate(['group_a', 'group_b', 'group_c', 'group_d']):
	pd.Series(nounlist[i]).value_counts().to_excel(writer,group)
writer.save()



print('\ndone!\n')



