"""
Get data from Twitter API
"""
import urllib.request
import json
import jmespath
import twurl


def execute(acct):
    """
    Get friends' screen name and location
    (only if it's present)
    :param acct:
    :return:
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'  # pylint: disable=invalid-name

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '10'})

    data = urllib.request.urlopen(url).read().decode()  # pylint: disable=consider-using-with

    js_friends = json.loads(data)

    friends_list = jmespath.search("users[?location != ''].{Name: screen_name, Location: location}",
                                   js_friends)
    return friends_list
