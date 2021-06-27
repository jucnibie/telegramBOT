import json
import random
import os
import requests

# local import
#from .configs import IMGUR_TOKEN, NSFW_TOKEN, NSFW_CATEGORIES, IMAGE_CATEGORIES
from . import configs as cfg

def get_image(arg):
    try:
        img = cfg.IMAGE_CATEGORIES[arg]
        url = f'https://api.imgur.com/3/album/{img}/images'
        _headers = {'Authorization': cfg.IMGUR_TOKEN}
        response = requests.get(url, headers=_headers)
        json_data = json.loads(response.text)['data']
        random_number = random.randint(0, len(json_data))
        return json_data[random_number]['link']
    except:
        return "Có lỗi xảy ra. Thử lại đi tml"


def get_image_nsfw(arg):
    try:
        nsfw = cfg.NSFW_CATEGORIES[arg]
        url = f'https://api.imgur.com/3/album/{nsfw}/images'
        _headers = {'Authorization': cfg.NSFW_TOKEN}
        response = requests.get(url, headers=_headers)
        json_data = json.loads(response.text)['data']
        random_number = random.randint(0, len(json_data))
        return json_data[random_number]['link']
    except:
        return "Lỗi cmnr. Thử lại đi tml"


def get_some_image_nsfw(arg):
    try:
        nsfw = cfg.NSFW_CATEGORIES[arg]
        url = f'https://api.imgur.com/3/album/{nsfw}/images'
        _headers = {'Authorization': cfg.NSFW_TOKEN}
        response = requests.get(url, headers=_headers)
        json_data = json.loads(response.text)['data']
        links = [ val['link'] for val in json_data ]
        random_urls = random.sample(links, 5)
        return random_urls
    except:
        print("Lỗi cmnr. Thử lại đi tml")
