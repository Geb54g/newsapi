from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def home():
    
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
# Your API key is: 8fef44d4c9bd4e70b5c1360222846157