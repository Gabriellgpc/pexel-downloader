# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Last Modified by:   Luis Condados
import os
import csv
import requests
from tqdm import tqdm
from joblib import Parallel, delayed

IMAGES_SIZES_LIST= ["original", "large2x" ,"large" ,"medium" ,"small" ,"portrait" ,"landscape", "tiny"]
VIDEO_SIZES_LIST = ["large", "medium", "small"]

class PexelDownloader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.pexels.com/v1/'

    def _log_to_csv(self, content_id, author_name, profile_url, file_path, content_type, csv_file="downloaded_content.csv"):
        # Check if CSV exists; if not, create it with headers
        if not os.path.exists(csv_file):
            with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Content ID", "Author", "Profile URL", "File Path", "Content Type"])

        # Append new content information to CSV
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([content_id, author_name, profile_url, file_path, content_type])

    def search_images(self, query, per_page=80, page=1):
        url = f"{self.base_url}search"
        headers = {"Authorization": self.api_key}
        params = {"query": query, "per_page": per_page, "page": page}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def _download_image(self, img_url, img_name):
        img_data = requests.get(img_url).content
        with open(img_name, 'wb') as handler:
            handler.write(img_data)

    def download_images(self, query, num_images, save_directory, size='original'):
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        assert size in IMAGES_SIZES_LIST, "size must be one of {}".format(IMAGES_SIZES_LIST)

        images = []
        page = 1
        while len(images) < num_images:
            result = self.search_images(query=query, per_page=80, page=page)
            images.extend(result['photos'])
            page += 1
            if not result['photos']:
                break

        images = images[:num_images]

        def process_image(img):
            img_url = img['src'][size]
            author  = img['photographer']
            profile_url = img['photographer_url']
            img_name_sufix = author.lower().replace(' ', '_').split('/')[0].split("\\")[0]
            img_name = os.path.join(save_directory, f"{img['id']}_{img_name_sufix}.jpg")
            self._download_image(img_url, img_name)

            # Log details to CSV
            self._log_to_csv(content_id=img['id'], author_name=author, profile_url=profile_url, file_path=img_name, content_type="image")


        Parallel(n_jobs=-1)(delayed(process_image)(img) for img in tqdm(images, desc="Downloading ..."))

    def search_videos(self, query, per_page=80, page=1):
        url = f"{self.base_url}videos/search"
        headers = {"Authorization": self.api_key}
        params = {"query": query, "per_page": per_page, "page": page}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def _download_video(self, video_url, video_name):
        video_data = requests.get(video_url, stream=True)
        with open(video_name, 'wb') as handler:
            for chunk in video_data.iter_content(chunk_size=1024):
                if chunk:
                    handler.write(chunk)

    def download_videos(self, query, num_videos, save_directory, size='medium'):
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        assert size in VIDEO_SIZES_LIST, f"size must be one of {VIDEO_SIZES_LIST}"

        videos = []
        page = 1
        while len(videos) < num_videos:
            result = self.search_videos(query=query, per_page=80, page=page)
            videos.extend(result['videos'])
            page += 1
            if not result['videos']:
                break

        videos = videos[:num_videos]

        def process_video(video):
            video_files = video['video_files']
            video_url = next((file['link'] for file in video_files if file['quality'] == size), video_files[0]['link'])
            author = video['user']['name']
            profile_url = video['user']['url']
            video_name_sufix = author.lower().replace(' ', '_').split('/')[0].split("\\")[0]
            video_name = os.path.join(save_directory, f"{video['id']}_{video_name_sufix}.mp4")
            self._download_video(video_url, video_name)

            # Log details to CSV
            self._log_to_csv(content_id=video['id'], author_name=author, profile_url=profile_url, file_path=video_name, content_type="video")

        Parallel(n_jobs=-1)(delayed(process_video)(video) for video in tqdm(videos, desc="Downloading videos..."))