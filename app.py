from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def examus():
    return render_template('examus.html')

@app.route('/bruh')
def choco():
    return render_template('choco.html')

if __name__ == '__main__':
    app.run()
