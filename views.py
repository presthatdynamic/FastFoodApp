from flask import Flask, render_template,request, session, redirect, url_for
from flask_app import app
#Here I have used strgen to geneate random IDs for my customers

#set secret key for the app in order to use sessions 
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#routing the app to the login page.(In this case this is my starting page)
@app.route('/', methods=['GET', 'POST'])
def login():	
	return render_template('login.html')

#routing to createuser page
@app.route('/createuser',methods=['GET', 'POST'])
def createuser():
	if request.method=='POST':
		fn=request.form['field1']
		ln=request.form['field2']
		lid=request.form['field3']
		cno=request.form['field4']
		pwd=request.form['field5']
		if(fn!='' and ln!='' and cno!='' and pwd!=''):
			return render_template('success.html')
		else:
			return 'Failure:credentials are not filled in properly'
	
	return render_template('createuser.html')


@app.route('/index',methods=['GET', 'POST'])
def index():
	if request.method=='POST':
		f=request.form.getlist('food')
		i=request.form.getlist('American')
		session['food']=f
		session['American']=i
		session["t_list"]=f+i
		session['cnt']=len(session["t_list"])
		t=f+i
		l=[]
		d=[]
		for j in t:	
			session["t_names"]=l	
		return render_template('cart.html')
	return render_template('index.html')		

@app.route('/cart',methods=['GET', 'POST'])
def cart():
	if request.method=='POST':
		return render_template('checkout.html')
	return render_template('cart.html')	

@app.route('/checkout',methods=['GET', 'POST'])
def checkout():
	if request.method=='POST':
		cardno=request.form['cardno']
		addr=request.form['addr']	
		return render_template('end.html')

	error="payment failed.Try again!"			
	return render_template('checkout.html',error=error)	

#Delete the session variable on logout
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))
	
@app.route('/adminupdateitem', methods=['GET'])	
def	adminUpdateItem():
	return render_template('adminUpdateItem.html')
	
@app.route('/additem', methods=['GET'])	
def	addItem():
	return render_template('addItem.html')
	
@app.route('/orderitemlist', methods=['GET'])	
def	orderItemList():
	return render_template('orderItemList.html')
	
@app.route('/userorderhistory', methods=['GET'])	
def	userOrderHistory():
	return render_template('userOrderHistory.html')
	
	
	 
	
	
