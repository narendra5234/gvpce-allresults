from flask import Flask, render_template, request
import mechanize
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
@app.route('/')
def student():
	return render_template('student.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		rolls = request.form.get("Name")
		# a=request.form.get("B.Tech")
		# b=request.form.get("Regular")
		# result=pd.read_csv("result.csv")
		# lis=[]
		# for i in range(len(result.name)):
		# 	if(("B.Tech" in result.name[i]) and ("Regular" in result.name[i]) and "(R-2015)" in result.name[i]):
		# 		print(result.urls[i])
		# urllen = len(lis)
		urls = ['http://gvpce.ac.in/results/B.Tech%20I%20Semester%20Regular%20(R-2015)_December%202015/btechsearch.asp',
'http://gvpce.ac.in/results/B.Tech%20II%20Semester%20(Regular)%20(R-2015)_May%202016%20(For%202015%20Admitted%20Batch)/btechsearch.asp',
'http://gvpce.ac.in/results/B.Tech%20III%20Semester%20(R-2015)%20Regular%20Results-October-2016/btechsearch.asp',
'http://gvpce.ac.in/results/B.Tech%20IV%20Sem%20Regular%20%20(R-2015)%20(For%202015%20%20Batch)%20Result_April,%202017/btechsearch.asp',
'http://gvpce.ac.in/results/B.Tech%20V%20Sem%20Regular%20(R-2015)%20(For%202015%20batch)%20Result_October-%202017/btechsearch.asp',
'http://www.gvpce.ac.in/results/B.Tech%20VI%20Sem%20Regular%20%20(R-2015)%20(For%202015%20batch)%20Result_April-2018/btechsearch.asp',
'http://gvpce.ac.in/results/Revalution%20Result%20of%20B.Tech%20III%20Sem%20Regular%20%20(R-2015)%20(For%202015%20Batch)-October-2016/btechsearch.asp']
		urllen=len(urls)
		s=[]
		for i in range(urllen):
			br = mechanize.Browser()
			br.open(urls[i])
			br.select_form(nr=0)
			br.form['u_input']=rolls
			br.submit()
			soup = BeautifulSoup(br.response().read(),"html5lib")
	#names.append(soup("td",{'colspan':'4'})[1].text)
	#gpa.append(soup("td",{'colspan':'4'})[2].text)
			if (soup.findAll('table') and soup("td",{'colspan':'4'})[2].text) :
				s.append(soup.find('font'))
				s.append(soup.find('table'))
    		else:
        		i+=1
			br.close()
		with open("templates/result.html", "w") as f:
			for i in s:
				f.write(str(i)+'\n')
		return render_template("result.html")

if __name__ == '__main__':
   app.run(debug = True)
