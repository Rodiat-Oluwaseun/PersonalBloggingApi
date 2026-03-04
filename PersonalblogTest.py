import unittest


# Import for APi
from blog_service import BlogRepository


class TestBlogRepository(unittest.TestCase):
    def setUp(self):
        """Set up a repository instance before each test."""
        self.repo = BlogRepository()

    def test_fetch_all_posts_type(self):
        """Test that fetching posts returns a list."""
        posts = self.repo.fetch_all_posts()
        self.assertIsInstance(posts, list)

    def test_invalid_post_creation(self):
        """Test how the code handles missing data (Exception Handling)."""
        with self.assertRaises(Exception):
            # Attempting to add a post without required fields
            self.repo.add_post(None, None)


if __name__ == '__main__':
    unittest.main()
