from flask import Flask,render_template,request

app = Flask(__name__)

@app.route(rule='/')
def home() -> str:
    return render_template(template_name_or_list='index.html')
@app.route(rule='/login',methods=['POST','GET'])
def login() -> str:
    if request.method == 'POST':
        Username: str | None = request.form.get(key='Username')
        password: str | None = request.form.get(key='password')
    return render_template(template_name_or_list='login.html')
@app.route(rule='/signup', methods=['POST','Get'])
def signup() -> str:
    if request.method == 'POST':
        Username: str | None = request.form.get(key='Username')
        Email:str | None = request.form.get(key='Email')
        password: str | None = request.form.get(key='password')
        re_password: str | None = request.form.get(key='re-password')
    return render_template(template_name_or_list='signup.html')
if __name__ == '__main__':
    app.run(debug=True,port=8080,host='localhost')