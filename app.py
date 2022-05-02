from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')

def home():
    newsapi = NewsApiClient(api_key="8fef44d4c9bd4e70b5c1360222846157")
    
    top_headlines = newsapi.get_top_headlines(sources='cnn')
    
    t_article = top_headlines['articles']
    
    news =[]
    desc =[]
    img =[]
    p_date =[]
    url =[]
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
# Your API key is: 8fef44d4c9bd4e70b5c1360222846157