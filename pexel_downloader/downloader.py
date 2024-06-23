# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Last Modified by:   Luis Condados
import requests
import os
from joblib import Parallel, delayed
from tqdm import tqdm

IMAGES_SIZES_LIST=["original", "large2x" ,"large" ,"medium" ,"small" ,"portrait" ,"landscape", "tiny"]

class PexelDownloader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.pexels.com/v1/'

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

        Parallel(n_jobs=-1)(delayed(self._download_image)(
            img['src'][size], os.path.join(save_directory, f"{img['id']}.jpg")
        ) for img in tqdm(images, desc="downloading ..."))