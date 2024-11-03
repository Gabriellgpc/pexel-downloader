from pexel_downloader import PexelDownloader
import os
YOUR_API_KEY = os.environ.get("PEXEL_API_KEY")
downloader = PexelDownloader(api_key=YOUR_API_KEY)
downloader.download_images(query='beaches', num_images=100, save_directory='./images')