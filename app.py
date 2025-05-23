from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/reels')
def reels():
    return render_template('reels.html')

if __name__ == '__main__':
    app.run(debug=True)
