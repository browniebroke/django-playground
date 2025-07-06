from django.test import TestCase

from playground.apps.blog.models import Post


class BrowsableApiPaginationTests(TestCase):
    def test_next_link(self):
        Post.objects.bulk_create(
            [
                Post(title="Post 1", text="heelo"),
                Post(title="Post 2", text="world"),
                Post(title="Post 3", text="there"),
                Post(title="Post 4", text="there"),
            ]
        )

        response = self.client.get("/api/posts/?timestamp=3", headers={"Accept": "text/html"})

        self.assertEqual(200, response.status_code)

        self.assertContains(response, "Post 1")
        self.assertContains(response, "Post 2")
        self.assertNotContains(response, "Post 3")
        self.assertContains(
            response,
            """<a href="http://testserver/api/posts/?page=2%C3%97tamp%3D3" rel="nofollow">http://testserver/api/posts/?page=2&amp;timestamp=3</a>""",
            html=True
        )