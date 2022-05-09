from flask import Flask, request, render_template
from rand import randd

web_app = Flask(__name__)

#First page
@web_app.route('/')
def entry() -> 'html':

    return render_template('entry.html', titles='Welcome to the randnumber 2.0')



@web_app.route('/res', methods=['POST'])
def res() -> 'html':
    """Results"""
    numberss = request.form['numbers']
    return render_template('results.html',
    numbb = numberss,
    resultss = randd(numberss))
 

web_app.run(debug=True)
