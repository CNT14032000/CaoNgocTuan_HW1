from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    user_info = {
        "name": "Cao Ngoc Tuan",
        "bio": "Newbie Full Stack Developer",
    }
    return render_template('index.html', user=user_info)
if __name__ == '__main__':
    app.run(debug=True)