# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import urllib
import requests
from boto3 import Session
from settings import config as cfg


def _request_string(query, num, start):
    encoding = 'utf-8'
    params = {
        "q": query.encode(encoding),
        "cx": cfg['CUSTOM_SEARCH_ENGINE'],
        "key": cfg['API_KEY'],
        "num": num,
        "start": start,
        "safe": "high",
        "searchType": "image"
    }

    return cfg['SEARCH_URL'] + "?" + urllib.urlencode(params)


def get_image_url(keyword, total_num):
    img_list = []
    i = 0
    while i < total_num:
        num = 10 if (total_num - i) > 10 else (total_num - i)
        start = i + 1
        data = requests.get(_request_string(keyword, num, start)).json()
        for j in range(len(data["items"])):
            img_list.append(data["items"][j]["link"])
        i = i + 10
    return img_list


def put_img_list(bucket, img_list):
    s3 = Session().resource('s3')
    bucket = s3.Bucket(bucket)
    keyname = cfg['KEY']
    #  keyname = "{0:%Y-%m-%d}".format(datetime.today())
    obj = bucket.Object(keyname)
    img_list = ','.join(img_list)
    #  print(img_list)
    body = img_list
    response = obj.put(
            Body=body.encode('utf-8'),
            ContentEncoding='utf-8',
            ContentType='text/plane'
            )


def lambda_handler(event, context):
    img_list = get_image_url("和久田麻由子", 50)
    put_img_list(cfg['BUCKET'], img_list)


if __name__ == '__main__':
    img_list = get_image_url("和久田麻由子", 50)
    put_img_list(cfg['BUCKET'], img_list)
