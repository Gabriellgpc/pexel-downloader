#!/bin/bash
rm -rf build/ dist/ pexel_downloader.egg-info/
python setup.py sdist bdist_wheel
twine upload dist/*