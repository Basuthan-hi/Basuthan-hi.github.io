from flask import Flask,render_template,request,flash,get_flashed_messages
app = Flask(__name__)
app.config['SECRET_KEY'] = open('key.txt', 'r').read()

import sqlite3
con=sqlite3.connect('user.db',check_same_thread=False)

try:
    con.execute("""CREATE TABLE IF NOT EXISTS Users (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Username TEXT NOT NULL,
                        Email TEXT NOT NULL UNIQUE,
                        Password TEXT NOT NULL
                    )""")
    print("Table created successfully")
except Exception as e:
    print("e")

# 
# 

def insertData(name,email,password):
    qry="insert into Users (Username,Email,Password) values (?,?,?);"
    con.execute(qry,(name,email,password))
    con.commit()
    print("User Details Added")
    
def updateData(name,email,password,id):
    qry="update Users set Username=?,Email=?,Password=? where ID=?;"
    con.execute(qry,(name,email,password,id))
    con.commit()
    print("User Details Updated")
    
def deleteData(id):
    qry="delete from Users where id=?;"
    con.execute(qry,(id))
    con.commit()
    print("User Details Deleted")

def selectData():
    qry="select * from Users"
    result=con.execute(qry)
    for row in result:
        print(row)
    

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
        if password != re_password:
            flash('Passwords do not match' ,category='error')
        elif len(password) <7:
            flash('Passwords is less than 7 characters', category='error')
        elif len(Email)<4:
            flash('Email is less than 4 characters' ,category='error')
        elif len(Username)<4:
            flash('Username is less than 4 characters', category='error')
        else:
            insertData(Username,Email,password)
            flash('User Details Added', category='success')

    return render_template(template_name_or_list='signup.html')
if __name__ == '__main__':
    app.run(debug=True,port=8080,host='localhost')