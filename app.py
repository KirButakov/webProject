from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
