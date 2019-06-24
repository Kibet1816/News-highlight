import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    def setUp(self,author,title,description,url,urlToImage,publishedAt):
        """
        SetUp to run before each test case
        """
        self.new_article = Articles('null','Women\'s world cup','That was not football','https://www.bbc.co.uk/sport/football/48738649','https://ichef.bbci.co.uk/onesport/cps/624/cpsprodpb/13590/production/_97584297_breaking_news.png','2019-06-23T18:02:58Z')


    def test_init(self):
        """
        Test to verify correct instantiation
        """
        self.assertEqual(self.new_article.author,'null')
        self.assertEqual(self.new_article.title,'Women\'s world cup')
        self.assertEqual(self.new_article.description,'That was not football')
        self.assertEqual(self.new_article.url,'https://www.bbc.co.uk/sport/football/48738649')
        self.assertEqual(self.new_article.urlToImage,'https://ichef.bbci.co.uk/onesport/cps/624/cpsprodpb/13590/production/_97584297_breaking_news.png')
        self.assertEqual(self.new_article.publishedAt,'2019-06-23T18:02:58Z')         



