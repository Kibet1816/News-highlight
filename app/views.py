from flask import render_template
from app import app
from .requests import get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_source = get_source('id')
    print(news_source)
    title = 'Home - Read all news here'
    return render_template('index.html', title = title,news = news_source)

@app.route('/news/<news_id>')
def news(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)