import json
import os
import random

import requests

# local import
from utils.configs import NSFW_CATEGORIES, IMAGE_CATEGORIES

# TOKEN
IMGUR_TOKEN = "Bearer " + os.getenv('IMGUR_TOKEN')
NSFW_TOKEN = "Bearer " + os.getenv('NSFW_TOKEN')


def get_image(category, nsfw=False):
    token = NSFW_TOKEN if nsfw else IMGUR_TOKEN
    categories = NSFW_CATEGORIES if nsfw else IMAGE_CATEGORIES
    try:
        album_id = categories[category]
        url = f'https://api.imgur.com/3/album/{album_id}/images'
        _headers = {'Authorization': token}
        response = requests.get(url, headers=_headers)
        json_data = json.loads(response.text)['data']
        random_number = random.randint(0, len(json_data))
        return json_data[random_number]['link']
    except (Exception,):
        return "Có lỗi xảy ra. Thử lại đi tml"


def get_some_image_nsfw(arg):
    try:
        nsfw = NSFW_CATEGORIES[arg]
        url = f'https://api.imgur.com/3/album/{nsfw}/images'
        _headers = {'Client-ID': NSFW_TOKEN}
        response = requests.get(url, headers=_headers)
        json_data = json.loads(response.text)['data']
        links = [val['link'] for val in json_data]
        random_urls = random.sample(links, 5)
        return random_urls
    except (Exception,):
        return "Có lỗi xảy ra. Thử lại đi tml"
