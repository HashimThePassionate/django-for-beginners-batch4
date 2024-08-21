from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


class PostsTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(test='This is a test')

    def test_post_content(self):
        self.assertEqual(self.post.test, 'This is a test')

    def test_url_exists_at_correct_location(self):  # new
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):  # new
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "Message Board")

