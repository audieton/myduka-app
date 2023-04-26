from flask import Flask, render_template
app = Flask(__name__)

#This is the first route
@app.route('/')
def home():
#Loading the html file
    return render_template('index.html')
#This is the second route
@app.route('/inventories')
def products():
#Loading the html file
    return render_template ('products.html')

