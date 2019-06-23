class News:
    '''
    News class to define News sources
    '''

    def __init__(self,id,name,title,description,poster,time_published,content):
        self.id = id
        self.name =name
        self.title = title
        self.description = description
        self.poster = 'https://m.files.bbci.co.uk/modules/bbc-morph-sport-opengraph/1.1.1/images/bbc-sport-logo.png'
        self.time_published = time_published
        self.content = content