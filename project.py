from flask import Flask, request, render_template
from rand import randd

web_app = Flask(__name__)

#First page
@web_app.route('/')
def entry() -> 'html':
    return render_template('entry.html', titles='Welcome to the randnumber 2.0')



def logg(reqq, results) -> xz:
    """log"""
    with open('logi.log', 'a') as log:
        print(reqq, results, file=log)
  
@web_app.route('/res', methods=['POST'])
def res() -> 'html':
    """Results"""
    numberss = request.form['numbers']
    logg(request, resultss)
    return render_template('results.html',
    numbb = numberss,
    resultss = randd(numberss))


if __name__ == "__main__":
    web_app.run(debug=True)
