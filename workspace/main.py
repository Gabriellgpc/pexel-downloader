# -*- coding: utf-8 -*-
# @Author: Luis Condados
# @Date:   2023-09-09 15:49:49
# @Last Modified by:   Luis Condados
# @Last Modified time: 2023-09-09 16:51:56

import logging
import os

import click

logging.basicConfig(level=logging.INFO,
                    format='[%(name)s] - [%(levelname)s] - %(message)s',
                    handlers=[logging.StreamHandler()])

import pexel_downloader

@click.command()
@click.option('-q', '--query', help='Query text')
@click.option('-m', '--max_images', default=100, help='Max number of images')
@click.option('-o', '--output_dir', help='Output directory')
@click.option('-s', '--image_size', help='''
    Valid image size types:
                    original,
                    large,
                    large2x,
                    medium,
                    small,
                    portrait,
                    landscape,
                    tiny''', default='medium')
def main(query, max_images, output_dir, image_size):

    logging.info('Making {} dir ...'.format(output_dir))
    os.makedirs(output_dir, exist_ok=True)

    logging.info('Searching for "{}" images. and saving to {} dir'.format(query, output_dir))
    pexel_downloader.download_from_pexel(query,
                                         max_images,
                                         output_dir,
                                         image_size)

if __name__ == "__main__":
    main()