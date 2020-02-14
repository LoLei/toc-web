from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return render_template('result.html', result=processed_text)


if __name__ == '__main__':
    app.run(debug=True)
