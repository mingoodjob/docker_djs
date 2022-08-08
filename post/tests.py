from django.test import TestCase

# Create your tests here.

class PostTest(TestCase):
    def test_post_list(self):
        response = self.client.get('/post/')
        self.assertEqual(response.status_code, 200)
    
    # def test_post_detail(self):
    #     response = self.client.get('/post/1/')
    #     self.assertEqual(response.status_code, 200)

    def test_post_create(self):
        response = self.client.post('/post/', {
            'author': 1,
            'title': 'test',
            'content': 'test',
            'exposure': True,
            # 'image': 'test',
        })
        self.assertEqual(response.status_code, 200)