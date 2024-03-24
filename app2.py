from flask import Flask, render_template, request, redirect, url_for
app=Flask(__name__)
userdata={}
@app.route('/')
def HOME():
    return render_template('LOGIN.html')
@app.route('/LOGIN',methods=['POST'])
def LOGIN():
    username=request.form['username']
    password=request.form['password']
    if username in userdata:
        if userdata[username]==password:
             return render_template('blog.html',message='Logged in successfully')
        else:
            return render_template('LOGIN.html', error='Invalid username or password')
    else:
        return 'Invalid Username'
@app.route('/')
def SIGNUP():
    return render_template('SIGNUP.html')
@app.route('/SIGNUP',methods=['POST'])
def SIGNUP():
    username=request.form['FULLNAME']
    password=request.form['EMAILID']
    username=request.form['USERNAME']
    password=request.form['password']
    if username in userdata:
        return 'Username already exists'
    else:
        userdata[username]=password
        return render_template('blog.html',message='Account created successfully')
