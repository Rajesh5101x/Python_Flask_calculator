from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html',title="Home")

@app.route('/Calculator')
def calc():
    return render_template('calc.html',title="Calculator")

@app.route('/Result/<res>')
def result(res):
    return render_template('result.html',title="Result",res=res)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/features')
def features():
    return render_template('features.html')

if __name__ == '__main__':
    app.run(debug=True)