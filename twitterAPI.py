import urllib.request
import urllib.parse
import urllib.error
import twurl
import ssl
import json

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# while True:
#     print('')
#     acct = input('Enter Twitter Account:')


def get_user_json(acct):
    TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '1'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    return js


def get_user_friends_json(acct):
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '47'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    return js


def json_name(js):
    return js[0]['user']['name']


def json_location(js):
    return js[0]['user']['location']


def json_friends_count(js):
    return js[0]['user']['friends_count']


def json_followers_count(js):
    return js[0]['user']['followers_count']


def json_profile_image(js):
    return js[0]['user']['profile_image_url_https']

def json_lang(js):
    return js[0]['user']['lang']

def json_created_at(js):
    return js[0]['user']['created_at']
js=get_user_friends_json('elonmusk')
for i in range(47):
    print(js['users'][i]['location'])