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

        return render_template('result.html', result=text)
    elif request.method == 'GET':
        text = "ERROR: Fill out form on main page"
        return render_template('result.html', result=text)


def main():
    # tug_overlap_checker.main(raw_args=['123 234'])
    app.run(debug=True)


if __name__ == '__main__':
    main()
