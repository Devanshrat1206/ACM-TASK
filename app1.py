from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def HOME():
    return render_template('blog.html')
@app.route('/LOGIN')
def LOGIN():
    return render_template('LOGIN.html')
@app.route('/SIGNUP')
def SIGNUP():
    return render_template('SIGNUP.html')
@app.route('/CREATEBLOG')
def CREATEBLOG():
    return render_template('CREATEBLOG.html')
@app.route('/BLOGS')
def BLOGS():
    return render_template('BLOGS.html')
@app.route('/ABOUT')
def ABOUT():
    return render_template('ABOUT.html')
@app.route('/CONTACT')
def CONTACT():
    return render_template('CONTACT.html')
if __name__ == '__main__':
    app.run(debug=True)