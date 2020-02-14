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


if __name__ == '__main__':
    app.run(debug=True)
