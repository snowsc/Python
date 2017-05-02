import requests

response = requests.get('https://api.github.com/users/Microsoft/repos')

for repo in response.json():
    print('[{}] {}'.format(repo['language'], repo['name']))