import json
import random

import requests as req

import utils.configs as cfg


def get_vid_url():
    return random.choice(cfg.porns)


"""
Tiktok downloader without watermark
- https://hamod.ga/api/tiktokWithoutWaterMark.php?u=https://vt.tiktok.com/ZSJ75tXXa/
source = f'https://godownloader.com/api/tiktok-no-watermark-free?url={link}&key=godownloader.com'
https://tdl.heran.xyz/api/download
"""


def get_tiktok(link):
    payload = {'url': link}
    source = 'https://tdl.heran.xyz/api/download'
    resp = req.post(source, data=payload)
    return json.loads(resp.text)['video']['urls'][0]


# Get link Douyin without watermark
def get_douyin(link):
    source = 'https://dy.nisekoo.com/api/?url=' + link
    resp = req.get(source).json()
    return resp['mp4']


"""
Utils functions for videos
"""


# Check text has douyin video link or not
def have_douyin(text):
    try:
        link = next(el for el in text.split(' ') if el.startswith('https://v.douyin.com/'))
        return link
    except (Exception,):
        return ""
