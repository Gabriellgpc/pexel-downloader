# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Date:   2023-09-09 16:50:19
# @Last Modified by:   Luis Condados
# @Last Modified time: 2023-09-09 16:51:38
import logging
import os

from tqdm import tqdm


import requests
# Import API class from pexels_api package
from pexels_api import API


def download_from_url(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

def download_from_pexel(query,
                        max_images=100,
                        dest_dir='photos',
                        image_size='medium',
                        ):

    """
        image_size: one of the following:
            "original";
            "large2x";
            "large";
            "medium";
            "small";
            "portrait";
            "landscape";
            "tiny".
    """

    valid_image_size_type = ['original',
                             'large',
                             'large2x',
                             'medium',
                             'small',
                             'portrait',
                             'landscape',
                             'tiny']

    assert image_size in valid_image_size_type, 'Invalid image_size. Please check image_size to match of the format expected.'

    # your Pexels API
    PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')

    # Create API object
    api = API(PEXELS_API_KEY)

    page = 0
    progress_bar = tqdm(total=max_images,
                        desc='Max number of images to be downloaded')
    while max_images > 0:
        page += 1
        # Search 'query' p
        api.search(query, results_per_page=80, page=page)
        # Get photo entries
        photos = api.get_entries()
        if photos == None:
            logging.info('No more photos to retrieve for the query "{}".'.format(query))
            break

        # Loop the five photos
        for photo in tqdm(photos, desc='Page {}'.format(page)):
            max_images -= 1
            progress_bar.update(1)
            # Print photographer
            logging.debug('Photographer: {}'.format(photo.photographer))
            # Print url
            logging.debug('Photo url: {}'.format(photo.url))
            # Print original size url
            logging.debug('Photo original size: {}'.format(photo.original))

            # filename = os.path.join( dest_dir,  )
            filename = '{}_{}.jpg'.format(photo.photographer.rsplit(' ')[-1],
                                    photo.url.rsplit('/')[-2])
            filename = os.path.join(dest_dir, filename)

            # to avoid download if already downloaded
            if os.path.exists(filename):
                continue

            url = None
            if image_size == 'medium':
                url = photo.medium
            elif image_size == 'large':
                url = photo.large
            elif image_size == 'tiny':
                url = photo.tiny
            elif image_size == 'small':
                url = photo.small
            elif image_size == 'landscape':
                url = photo.landscape
            else:
                url = photo.original
            download_from_url(url, filename)

    logging.info('Max downloaded images reached!')