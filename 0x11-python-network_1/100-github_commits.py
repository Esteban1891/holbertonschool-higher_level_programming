#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'https://api.github.com/repos/{}/{}/commits'\
        .format(argv[1], argv[2])
    r = requests.get(url)
    results = ''
    count = 0
    for commit in r.json():
        count += 1
        if count > 10:
            break
        if isinstance(commit, dict):
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit').
                                  get('author').get('name')))
