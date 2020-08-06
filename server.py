from flask import Flask,url_for,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:pagename>')
def html_page(pagename):	
	return render_template(pagename)


def write_to_file(data):
	with open ("database.txt", mode = 'a') as db:
		name = data["name"]
		email = data["email"]
		subject = data["Subject"]
		message = data["Message"]
		file = db.write(f'\n {name}, {email}, {subject}, {message}')

def write_to_csv(data):
	with open ("database2.csv", newline = '', mode = 'a') as db2:
		name = data["name"]
		email = data["email"]
		subject = data["Subject"]
		message = data["Message"]
		csv_writer = csv.writer(db2, delimiter=' ',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
		# csv_writer.writeheader([Name,Email,Subject,Message])
		csv_writer.writerow([name,email,subject,message])
		

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		# name = data['name']
		write_to_csv(data)
		return render_template('/thankyou.html',name = data['name'].split(' ')[0])
	else:
		return 'Something went wrong! Try Again'



	