from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'cricket123'

# In-memory user database
users = {}

@app.route('/')
def home():
    if 'user' in session:
        return render_template('home.html', user=session['user'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            return redirect(url_for('home'))
        return "Invalid username or password!"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return "Username already exists!"
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/players')
def players():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('players.html')

@app.route('/schedules')
def schedules():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('schedules.html')

@app.route('/news')
def news():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
