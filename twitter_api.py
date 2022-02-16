import urllib.request
import twurl
import json
import jmespath


def execute(acct):
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '10'})

    data = urllib.request.urlopen(url).read().decode()

    js = json.loads(data)

    friends_list = jmespath.search("users[?location != ''].{Name: screen_name, Location: location}", js)
    return friends_list
