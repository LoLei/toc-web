import sys
from tug_overlap_checker import tug_overlap_checker
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        text = request.form['text']
    elif request.method == 'GET':
        text = "ERROR: Fill out form on main page"
    return render_template('result.html', result=text)


def main():
    sys.argv += ['123 234']
    tug_overlap_checker.main()
    app.run(debug=True)


if __name__ == '__main__':
    main()
