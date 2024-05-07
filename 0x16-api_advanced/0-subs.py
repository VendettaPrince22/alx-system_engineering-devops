#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscribers for a given subreddit.
If an invalid subreddit is given, the function returns 0

Args:
    subreddit(string) -- subreddit to check
"""

import requests
import requests.auth

def number_of_subscribers(subreddit):
    access_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzE1MTc1NTM1LjMxMTk0NywiaWF0IjoxNzE1MDg5MTM1LjMxMTk0NywianRpIjoiT0pGMGNSSnh4N2t6MGtXaHFlRzJFNkNodmJYSTJRIiwiY2lkIjoiYnNoeFpKdE1CNldBdXYyLWJCdTVKUSIsImxpZCI6InQyX3Yxa3M0c2FpeSIsImFpZCI6InQyX3Yxa3M0c2FpeSIsImxjYSI6MTcwOTAwMzIyMTcyNCwic2NwIjoiZUp5S1Z0SlNpZ1VFQUFEX193TnpBU2MiLCJmbG8iOjl9.Cp4SPUNUbRPBptvZ2_O-28HU9a5B6_saEjwJqHDmd7kCMT6ACDOwiz0UxN3TGmRoS1HEMUta2EOqIx0p_u4kNBOQIhTo0r-ugz6uMuPFvkoyjaxIpwdzFOyGmJ86jOM5G5lzSaEmBVAEbD40XIAlHKo9JwBMh6dT1QiUINTSqv_hB3RW_JLkul9h13ciJMA3yOGSqx9BLQkXf_N_d98hUN1h3-0dji9ZZMKlBOMpS5BdMBAJWCqODAU1wNEc43NqNvAQH66eE3vZQY0VIIkDlaV5ZKVL9XG0TC2wuRpVD-YuJy8F6mS1L9PaJaJEPZJy1BcrHdRUQdb47Xcd1zD2rA'

    headers = {"Authorization": "bearer {}".format(access_token), "User-Agent": "Root/0.1 by MissionAfternoon245"}
    url = "https://oauth.reddit.com/r/{}/about".format(subreddit)

    subs = requests.get(url, headers=headers, allow_redirects=False)
    if subs.status_code == 404:
        return 0

    result = subs.json()
    final = result['data'].get('subscribers')

    return final

if __name__ == '__main__':
    subs = number_of_subscribers('programming')

    print(subs)
