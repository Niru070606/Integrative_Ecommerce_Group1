from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/secondPage')
def secondPage():
    return render_template('secondPage.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/deals')
def deals():
    return render_template('deals.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/product/<filename>')
def product_detail(filename):
    return render_template('product_templates/' + filename + '.html')
"""
yung product/filename route web url
 ay kukunin nya lahat ng name ng file para ma rener yung exact file gamit yung string concatenation sa baba



Use The funcntion as first href parameter and filename as second href parameter
"""

if __name__ == '__main__':
    app.run(debug=True)

