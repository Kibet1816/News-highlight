import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News('bbc-news','Top News','All the latest news from around the world','https://www.bbc.co.uk/sport/football/48738649','sports')

    def test_init(self):
        """
        Test to check whether the source is instantiated correctly
        """
        self.assertEqual(self.new_source.id,'bbc-news')
        self.assertEqual(self.new_source.name,'Top News')
        self.assertEqual(self.new_source.description,'All the latest news from around the world')
        self.assertEqual(self.new_source.url,'https://www.bbc.co.uk/sport/football/48738649')
        self.assertEqual(self.new_source.category,'sports')
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News))


if __name__ == '__main__':
    unittest.main()
