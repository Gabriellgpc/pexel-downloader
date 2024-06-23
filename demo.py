from pexel_downloader import PexelDownloader
downloader = PexelDownloader(api_key="YOUR_KEY_API")
downloader.download_images(query='sunset', num_images=200, save_directory='./images')