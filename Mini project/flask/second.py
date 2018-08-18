from flask import Flask, render_template, request
import mechanize
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np
app = Flask(__name__)
@app.route('/')
def student():
	return render_template('student.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		rolls = request.form.get("Name")
		a=request.form.get("course")
		b=request.form.get("other")
		a=str(a)
		b=str(b)
		if(b=="Supple+Regular"):
			b="Regular"
			c="Supplementary"
		else:
			c="-1"
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
			text.append(str(i.text).lstrip('\n'))
	    #links.append(str(link.find('font'))[22:])
		urls=np.asarray(links[8:])
		name=np.asarray(text[8:])
		df1=pd.DataFrame(name,columns=['name'])
		df2=pd.DataFrame(urls,columns=['urls'])
		result = pd.concat([df1,df2],axis=1)
		s=["""<center><div class="header" style="width: 1003px; height: 130px">
			<h1>
			<img src="static/banner.jpg" width="1000" height="100" border="0"></h1>
			<div class="subheader_left" style="width: 1000px; height: 24px">
				&nbsp;</div>
				</div><center>"""]

		for i in range(500):
			if((a in result.name[i]) and (b in result.name[i] or c in result.name[i]) and ("(R-2015)" in result.name[i])):
				br = mechanize.Browser()
				br.open(result.urls[i])
				br.select_form(nr=0)
				br.form['u_input']=rolls
				br.submit()
				soup = BeautifulSoup(br.response().read(),"html5lib")
				if (soup.findAll('table')) :
        	#print(soup("td",{'colspan':'4'})[2].text)
					s.append("<center>")
					s.append(soup.find('font'))
					s.append(soup.find('table'))
					s.append("</center>")
					s.append("<br><br><br>")
				else:
					i+=1
				br.close()
		with open("templates/result.html", "w") as f:
			for i in s:
				f.write(str(i)+'\n')
		return render_template("result.html")
if __name__ == '__main__':
   app.run(debug = True)
