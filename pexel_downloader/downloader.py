# downloader.py
import os
import click
from .pexel_downloader import PexelDownloader

IMAGES_SIZES_LIST= ["original", "large2x" ,"large" ,"medium" ,"small" ,"portrait" ,"landscape", "tiny"]
VIDEO_SIZES_LIST = ["large", "medium", "small"]

@click.command()
@click.argument("query", type=str)
@click.argument("num", type=int)
@click.argument("content-type", type=click.Choice(["image", "video"], case_sensitive=False))
@click.option("--size", default="medium", help="Size of the image or video.")
@click.option("--save-directory", "-o", default="downloads", help="Directory to save downloaded files.")
def main(query, num, content_type, size, save_directory):
    """
    CLI tool to download images or videos from Pexels.

    \b
    QUERY - The search term for the content.
    NUM - The number of images or videos to download.
    CONTENT_TYPE - The type of content to download (image or video).

    example of usage, downloading 5 videos of nature from Pexels:
    \b
    \tpexel-downloader nature 5 videos
    """
    # Check for API key in environment variable if not provided as an option
    api_key = os.getenv("PEXEL_API_KEY")
    if not api_key:
        api_key = click.prompt("Please enter your Pexels API key", hide_input=True)

    # Initialize the downloader with the API key
    downloader = PexelDownloader(api_key=api_key)

    # Download images or videos based on the content type
    if content_type.lower() == "image":
        downloader.download_images(query=query, num_images=num, save_directory=save_directory, size=size)
    else:
        downloader.download_videos(query=query, num_videos=num, save_directory=save_directory, size=size)

    click.echo(f"[INFO] Downloaded {num} {content_type}s to {save_directory}")