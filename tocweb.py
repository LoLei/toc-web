import contextlib
import io
from tug_overlap_checker import tug_overlap_checker
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # Get the submitted course IDs
        text = request.form['text']
        lines = text.split('\n')
        lines = [l.rstrip() for l in lines]
        print(lines)

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            res = tug_overlap_checker.main(raw_args=lines)
        output = f.getvalue()
        print("captured: {}".format(output))

        return render_template('result.html', result=output)
    elif request.method == 'GET':
        text = "ERROR: Fill out form on main page"
        return render_template('result.html', result=text)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
