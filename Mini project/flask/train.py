import mechanize
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
rolls = raw_input("Enter you roll number")
result=pd.read_csv("result.csv")
lis=[]
for i in range(len(result.name)):
	if("Regular" in result.name[i] and "(R-2015)" in result.name[i]):
		print(result.urls[i])
		lis.append(result.urls[i])
urllen = len(lis)
s=[]
for i in range(urllen):
	br = mechanize.Browser()
	br.open(lis[i])
	br.select_form(nr=0)
	br.form['u_input']=rolls
	br.submit()
	soup = BeautifulSoup(br.response().read(),"html5lib")
	if (soup.findAll('table') and soup("td",{'colspan':'4'})[2].text) :
        	#print(soup("td",{'colspan':'4'})[2].text)
		s.append(soup.find('font'))
		s.append(soup.find('table'))
    	else:
        	i+=1
	br.close()
with open("result.html", "w") as f:
    for i in s:
        f.write(str(i)+'\n')
