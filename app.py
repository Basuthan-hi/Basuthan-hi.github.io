from flask import Flask,render_template

app = Flask(__name__)

@app.route(rule='/')
def home() -> str:
    return render_template('index.html')
@app.route(rule='/login')
def login() -> str:
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True,port=8080,host='localhost')