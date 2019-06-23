import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('bbc-news','BBC News','Watch: Fifa Women\'s World Cup - England v Cameroon in last 16 under way','England face Cameroon in the round of 16 at the Fifa Women\'s World Cup 2019 ','https://m.files.bbci.co.uk/modules/bbc-morph-sport-opengraph/1.1.1/images/bbc-sport-logo.png',67,'GulaGula')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()