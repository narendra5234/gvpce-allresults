from flask import Flask, render_template, request
import mechanize
from BeautifulSoup import BeautifulSoup
import numpy as np
import pandas as pd
import urllib2
import re
import matplotlib.pyplot as plt

app = Flask(__name__)
@app.route('/')
def student():
	return render_template('student.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		rolls = request.form.get("Name")
		start="http://gvpce.ac.in"
		l1=[]
		html_page = urllib2.urlopen("http://gvpce.ac.in/result.html")
		soup = BeautifulSoup(html_page)
		for link in soup.findAll('a'):
			l1.append(start+str(link.get('href'))[2:])
		links=[]
		for i in range(len(l1)):
			l=" "
			for j in l1[i]:
				if(j==' '):
					l=l+'%20'
				else:
					l=l+j
				links.append(l)
		text=[]
		for i in soup.findAll('a'):
   		 #links.append(str(link.find('font'))[22:])
    			text.append(str(i.text))
		urls=np.asarray(links[8:])
		name=np.asarray(text[8:])
		df1=pd.DataFrame(name,columns=['name'])
		df2=pd.DataFrame(urls,columns=['urls'])
		result = pd.concat([df2,df1],axis=1)
		print(result)
		# urllen = len(result)
		# s=[]
		# for i in range(urllen):
		# 	br = mechanize.Browser()
		# 	br.open(result["urls"][i])
		# 	br.select_form(nr=0)
		# 	br.form['u_input']=rolls
		# 	br.submit()
		# 	soup1 = BeautifulSoup(br.response().read(),"html5lib")
		# 	if (soup1.findAll('table') and soup("td",{'colspan':'4'})[2].text) :
		# 		s.append(soup1.find('font'))
		# 		s.append(soup1.find('table'))
		# 	else:
		# 		i+=1
		# 	br.close()
		# with open("templates/result.html", "w") as f:
		# 	for i in s:
		# 		f.write(str(i)+'\n')
		return render_template("result.html")

if __name__ == '__main__':
   app.run(debug = True)
