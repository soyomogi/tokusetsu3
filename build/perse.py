# -*- coding: utf-8 -*- 
import re
#IN
f_in = open('index.html', 'r')
s = ""
for row in f_in:
	s += row
f_in.close()
######regex######
#この下に「blockstart」をペースト

#この下に「blockend」をペースト

#この下に「text」をペースト

#################
#OUT
f_out = open('index_fix.html', 'w')
f_out.write(s)
f_out.close