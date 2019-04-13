import requests
from requests.auth import AuthBase
import time, datetime, os, sys

sys.path.append(os.pardir)

from private.api_token_esa import API_TOKEN_ESA, TEAM_NAME_ESA

class AuthEsa(AuthBase):

    def __call__(self, r):
        self.TOKEN = API_TOKEN_ESA
        r.headers['Authorization'] = 'Bearer {}'.format(self.TOKEN)
        return r

class Esa():

    def __init__(self):
        self.session = requests.session()
        self.session.auth = AuthEsa()
        self.session.headers['Content-Type'] = 'application/json'

        self.api_endpoint = 'https://api.esa.io'

        self.TEAM_NAME = TEAM_NAME_ESA

    def checkEsa(self):
        resp = self.session.get('{}/v1/teams/{}/posts'.format(self.api_endpoint, self.TEAM_NAME))

        get_esa = resp.json()

        updated_article = []
        now = datetime.datetime.now()
        for article in get_esa['posts']:
            time_updated = datetime.datetime.strptime(article['updated_at'], '%Y-%m-%dT%H:%M:%S+09:00')
            check_time_updated = now - datetime.timedelta(days=7)
            
            if (time_updated > check_time_updated):
                updated_article.append(article)

        return updated_article