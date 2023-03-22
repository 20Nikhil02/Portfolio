from flask import Flask,render_template,request
import pymysql as db

app = Flask(__name__)
#print(__name__)
'''
@app.route('/<username>')
def hello_world(username=None):
	return render_template('index.html',name=username)

'''
@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/index')
def indexhtml():
	return render_template('index.html')


def write_file(data):
		db = open ("database.txt","a") 
		name = data["name"]
		email = data["email"]
		sub = data["subject"]
		message = data["message"]
		db.write(f"{name},{email},{sub},{message}\n")
		db.close()

@app.route('/Submit_form',methods=['POST','GET'])
def submit_responce():
	if request.method=='POST':
		data = request.form.to_dict()
		write_file(data)
		return "Form Submitted"
	else:
		return "Error"

@app.route('/blog')
def blog():
	return "Hello Nikhil You have Routed for Blog Window as New Tab "

@app.route('/blog/nikhil')
def blognik():
	return "Hello Nikhil You have Routed for Blog Window as New Tab Nikhil"

