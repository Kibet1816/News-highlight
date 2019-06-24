from app import app
import urllib.request,json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']

base_url = app.config['NEWS_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)
            return source_results


def process_results(source_list):
    """
    Function  that processes the movie result and transform them to a list of Objects
    """
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        poster = source_item.get('urlToImage')
    
        if poster:
            source_object = News(id,name,poster)
            source_results.append(source_object)

    return source_results