from django.test import SimpleTestCase, TestCase
from .models import Article
from django.urls import reverse

# Create your tests here.
class BlogAppTest(SimpleTestCase):


    def test_django(self):
        self.assertTrue(True)


class BlogTest(TestCase):
    def test_django(self):
        self.assertEqual(len(Article.objects.all()), 0)
        Article.objects.create(title='Title 1')
        Article.objects.create(title='Title 2')
        self.assertEqual(len(Article.objects.all()), 2)

        a= Article.objects.get(pk=2)
        self.assertEqual(a.title, 'Title 2')

        a.title = 'New Title'
        a.save()
        self.assertEqual(a.title, 'New Title')

        a.delete()
        self.assertEqual(len(Article.objects.all()), 1)

class ArticleViewsTest(TestCase):
    def test_article_list_view(self):
        self.assertEqual(reverse("article_list"), "/article/")

    def test_artice_add_view(self):
        a = dict(title='T 1', body='NONE')
        b = dict(title='T 2', body='NONE')

        response = self.client.post(reverse('article_add'),a)
        response = self.client.post(reverse('article_add'),b)
        self.assertEqual(len(Article.objects.all()), 2)
                             
