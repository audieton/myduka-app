from flask import Flask, render_template
app = Flask(__name__)

#This is the first route
@app.route('/')
def home():
#Loading the html file
    return render_template('index.html')
#This is the second route
@app.route('/products')
def products():
#Loading the html file
#This is where we get data from products table
#run pip install psycopg2
   products[
     (1,"omo",40,50,100)
     (2,"bread",50,60,200)
     (3,"milk",60,65,150)
 ]
 #This is where we load an html file
   return render_template ('products.html',products=products)

app.run()

import psycopg2
