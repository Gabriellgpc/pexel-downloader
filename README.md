# pexel-downloader
"Pexel Downloader: Python-based web scraper for effortlessly downloading high-quality photos and videos from Pexels.com, open-source with MIT License."

![pexel-downloader](pexel_downloader-logo.jpg)

📷 **Pexel Downloader - Your Gateway to Stunning Visuals!** 🎥

Welcome to the Pexel Downloader, a Python-based web scraper designed to help you effortlessly gather high-quality photos and videos from the Pexels.com website. Whether you're a content creator, developer, or just a visual enthusiast, this open-source tool is here to simplify your media acquisition process.

🚀 **Key Features:**
- Download photos and videos from Pexels with ease.
- MIT License: Contribute and enhance the project freely.
- Seamless integration with your Python projects.
- Stay up-to-date with Pexels' latest content.

Pexel Downloader offers a user-friendly interface, robust performance, and the flexibility to fit seamlessly into your projects. Join our community of developers and creators, and together, let's make this tool even better.

🔧 **Installation:**
To get started, simply clone this repository and follow the setup instructions in our documentation.

Or, simply run the following command on your python environment
```bash
pip install pexel-downloader
```

🏃**How to use it**

First things first, you need to create an account on [pexels.com](https://www.pexels.com/)! Once you have login you can access the api page to get your unique API Key, you will find it in this link https://www.pexels.com/api/new/.

the first thing you need to do inder to run the `main.py`, is to get yout API Key from pexels.com,
create your pexels account, go to `Images & Video API` and then `Your API Key`.
Copy the API Key and export in your terminal export such as:

Example of how to query for 200 images of nice sunsets 🌞. by default it will download the images on the original size, but you can select one of the other sizes.

-   original
-   large2x
-   large
-   medium
-   small
-   portrait
-   landscape
-   tiny


```python
from pexel_downloader import PexelDownloader

downloader = PexelDownloader(api_key="YOUR_KEY_API")
downloader.download_images(query='sunset', num_images=200, save_directory='./images', size='original')
```

🙌 **Contributions Welcome:**
We invite you to contribute to the development of Pexel Downloader. Feel free to submit bug reports, feature requests, or even make direct contributions. Let's build something amazing together!

📜 **License:**
Pexel Downloader is released under the MIT License, granting you the freedom to use and modify it for your projects.

<!-- 🔗 **Links:**
- [Demo Video](Link to Demo Video)
- [Report Issues](Link to Issue Tracker)
- [Contribute Guidelines](Link to Contribution Guidelines) -->

Get started with Pexel Downloader today, and elevate your visual content game. Happy scraping!