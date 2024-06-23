import os
import unittest
from pexel_downloader import PexelDownloader

class TestPexelDownloader(unittest.TestCase):
    def setUp(self):
        self.downloader = PexelDownloader()

    def test_search_images(self):
        result = self.downloader.search_images('nature')
        self.assertIn('photos', result)

if __name__ == '__main__':
    unittest.main()