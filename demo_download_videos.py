from pexel_downloader import PexelDownloader
import os
YOUR_API_KEY = os.environ.get("PEXEL_API_KEY")
downloader = PexelDownloader(api_key=YOUR_API_KEY)
downloader.download_videos(query="nature", num_videos=5, save_directory="videos", size="medium")