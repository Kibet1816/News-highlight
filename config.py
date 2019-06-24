class Config:
    '''
    General configuration parent class
    '''
    # NEWS_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_BASE_URL = 'https://newsapi.org/v1/sources?language=en&category={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True