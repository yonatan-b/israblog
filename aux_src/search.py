# -*- coding: utf-8 -*-
import re
import json
import pandas as pd
import pdb
# construct search str

to_whom=r'\b(?:לי|לך|לו|לה|לנו|לכם|לכן|להם|להן|ל\w+?\b)'
regex_a = r'(?:\w+\W+){,5}הי[י]?תה\s*?' + to_whom + r'\s+?\bאת\b\W+ה\w+(?:\W+\w+){,2}' 
regex_b = r'(?:\w+\W+){,5}הי[י]?תה\s*?' + to_whom + r'\s+?\bה\w+\b(?:\W+\w+){,3}' 
regex_c = r'(?:\w+\W+){,5}הי[י]?ה\s*?' + to_whom + r'\s+?\bאת\b\W+ה\w+(?:\W+\w+){,2}' 
regex_d = r'(?:\w+\W+){,5}הי[י]?ה\s*?' + to_whom + r'\s+?\bה\w+\b(?:\W+\w+){,3}' 


# init
df_columns = ['match', 'post_content', 'nickname', 'blogger_age', 'blogger_gender', 'post_title', 'post_date', 'post_hour', 'post_url' ]
dictlist_a,dictlist_b,dictlist_c,dictlist_d = [],[],[],[]

# read input file (israblog posts)  aline at a time:

item={}

filename = input("enter file to process:")
ofilename = input("enter *.xlsx file for output:")
if not filename.strip():
	filename = '..\\data\\israblog.jl'
if not ofilename.strip():
	ofilename = '..\\data\\israblog_matches.xlsx'

list_a, list_b, list_c, list_d = [],[],[],[]
n_match=0
with open(filename, mode='r', encoding="utf8") as f:
	for index,line in enumerate(f):
		item = json.loads(line)
		post_content = item['post_content']
		b_match = False
		if post_content :
			list_a = re.findall(regex_a, post_content)
			list_b = re.findall(regex_b, post_content)
			list_c = re.findall(regex_c, post_content)
			list_d = re.findall(regex_d, post_content)
		if list_a:
			b_match = True
			for match in list_a:
				item['match'] = match
				#pdb.set_trace()
				dictlist_a.append(item)
		if list_b:
			b_match = True
			for match in list_b:
				item['match'] = match
				dictlist_b.append(item)
		if list_c:
			b_match = True
			for match in list_c:
				item['match'] = match
				#pdb.set_trace()
				dictlist_c.append(item)
		if list_d:
			b_match = True
			for match in list_d:
				item['match'] = match
				#pdb.set_trace()
				dictlist_d.append(item)
		if b_match:
			n_match+=1
			print (' '*150,end='\r')
			print ('{} item(s) matched. Last match ln.: {}. Match: {}'.format(n_match, index,match.replace('\n',' ')),end='\r')

group_a = pd.DataFrame(dictlist_a,columns=df_columns)
group_b = pd.DataFrame(dictlist_b,columns=df_columns)
group_c = pd.DataFrame(dictlist_c,columns=df_columns)
group_d = pd.DataFrame(dictlist_d,columns=df_columns)

writer = pd.ExcelWriter(ofilename,engine='xlsxwriter',options={'strings_to_urls': False})
group_a.to_excel(writer,'group_a', index = False)
group_b.to_excel(writer,'group_b', index = False)
group_c.to_excel(writer,'group_c', index = False)
group_d.to_excel(writer,'group_d', index = False)
writer.save()

print('\ndone!\n')



