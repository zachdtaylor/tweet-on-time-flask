import json
import requests
import urllib

from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from requests_oauthlib import OAuth1
from .settings import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from .models import Tweet

auth = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

tweet_scheduler = BackgroundScheduler()


def get_profile_info():
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    res = requests.get(url, auth=auth)
    data = json.loads(res.text)
    data['profile_image_url_https'] = data['profile_image_url_https'].replace(
        'normal', '400x400')
    return data


def post_tweet(tweet):
    encoded = urllib.parse.quote(tweet.body)
    url = f'https://api.twitter.com/1.1/statuses/update.json?status={encoded}'
    res = requests.post(url, auth=auth)
    tweet.delete()
    return json.loads(res.text)


def schedule_tweet(status, datetime_str):
    tweet = Tweet(body=status, tweet_on=datetime_str)
    tweet.save()
    tweet_scheduler.add_job(
        lambda: post_tweet(tweet),
        'date',
        run_date=datetime.fromisoformat(datetime_str)
    )


if __name__ == '__main__':
    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))
