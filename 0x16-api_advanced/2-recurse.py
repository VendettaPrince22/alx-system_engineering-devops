#!/usr/bin/python3
"""
Recursive function that queries the Reddit API returning a list containing the titles of all hot articles of a given subreddit.
"""
import requests
import requests.auth

def recurse(subreddit, hot_list=[], after="", count=0):

    token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzE1MTc1NTM1LjMxMTk0NywiaWF0IjoxNzE1MDg5MTM1LjMxMTk0NywianRpIjoiT0pGMGNSSnh4N2t6MGtXaHFlRzJFNkNodmJYSTJRIiwiY2lkIjoiYnNoeFpKdE1CNldBdXYyLWJCdTVKUSIsImxpZCI6InQyX3Yxa3M0c2FpeSIsImFpZCI6InQyX3Yxa3M0c2FpeSIsImxjYSI6MTcwOTAwMzIyMTcyNCwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.Cp4SPUNUbRPBptvZ2_O-28HU9a5B6_saEjwJqHDmd7kCMT6ACDOwiz0UxN3TGmRoS1HEMUta2EOqIx0p_u4kNBOQIhTo0r-ugz6uMuPFvkoyjaxIpwdzFOyGmJ86jOM5G5lzSaEmBVAEbD40XIAlHKo9JwBMh6dT1QiUINTSqv_hB3RW_JLkul9h13ciJMA3yOGSqx9BLQkXf_N_d98hUN1h3-0dji9ZZMKlBOMpS5BdMBAJWCqODAU1wNEc43NqNvAQH66eE3vZQY0VIIkDlaV5ZKVL9XG0TC2wuRpVD-YuJy8F6mS1L9PaJaJEPZJy1BcrHdRUQdb47Xcd1zD2rA'

    url = 'https://oauth.reddit.com/r/{}/hot'.format(subreddit)
    headers = {"Authorization": "bearer {}".format(token), "User-Agent": "MyApp/0.1 by MissionAfternoon245"}
    payload = {'after': after, 'count': count, 'limit': 2000, 'show': 'all'}

    response = requests.get(url, params=payload, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return None

    result = response.json()
    results = result['data']
    after = results.get('after')
    count += results.get('dist')

    for data in result.get('children'):
        hot_list.append(data['data'].get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list

if __name__ == '__main__':
    result = 'programming'
    print(len(result))
