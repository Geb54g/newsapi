from flask import Flask, render_template


from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def home():
    
    newsapi = NewsApiClient(api_key ="8fef44d4c9bd4e70b5c1360222846157")
    
    top_headlines = newsapi.get_top_headlines(sources='bbc-news')
    
    all_articles = newsapi.get_everything(sources='bbc-news')
    
    t_articles = top_headlines['articles']
    
    a_articles = all_articles['articles']
    
    news = []
    desc =[]
    img = []
    p_date =[]
    url =[]
    
    
    for i in range(len(t_articles)):
        main_article = t_articles[i]
        
        
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])
        
    news_all =[]    
    desc_all =[]
    img_all = []
    p_date_all =[]
    url_all =[]
    
    for j in range(len(a_articles)):
        a_article = a_articles[j]
        
        
        news_all.append(a_article['title'])
        desc_all.append(a_article['description'])
        img_all.append(a_article['urlToImage'])
        p_date_all.append(a_article['publishedAt'])
        url_all.append(a_article['url'])
        
        
        
        contents = zip(news,desc,img,p_date,url)
        all = zip(news_all,desc_all,img_all,p_date_all,url_all)
    
    return render_template('home.html',contents=contents,all=all)


if __name__=='__main__':
    app.run(debug=True)