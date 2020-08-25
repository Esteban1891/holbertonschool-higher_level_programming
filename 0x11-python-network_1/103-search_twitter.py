#!/usr/bin/python3
"""
takes in 3 strings and sends a search request to the Twitter API
"""


if __name__ == '__main__':
    import requests
    from base64 import b64encode
    from sys import argv
    key_secret = argv[1] + ':' + argv[2]
    base64_encode = b64encode(key_secret.encode()).decode('utf-8')
    payload = {'grant_type': 'client_credentials'}
    header = {'Authorization': 'Basic {}'.format(base64_encode),
              'Content-Type':
              'application/x-www-form-urlencoded;charset=UTF-8'}
    r = requests.post('https://api.twitter.com/oauth2/token', headers=header,
                      data=payload)
    token = r.json()
    b = token.get('access_token')
    header = {'Authorization': 'Bearer {}'.format(b)}
    payload = {'q': argv[3], 'count': 5}
    r = requests.get('https://api.twitter.com/1.1/search/tweets.json',
                     headers=header, params=payload)
    response = r.json()
    tweets = response.get('statuses')
    for tweet in tweets:
        print('[{}] {} by {}'.format(tweet.get('id'), tweet.get('text'),
                                     tweet.get('user').get('name')))
