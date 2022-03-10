import logging
import random
import time

from locust import TaskSet, task
# from locust_plugins.csvreader import CSVReader

from graphql import GQL
from methods import *
from vuser import *


def android_login(self):
    res = self.client.get("/api/v2/tiny/profile/")
    headers_ios_set_token_id(self, res.json()['result']['profile']['token'], str(res.json()['result']['profile']['id']))
    time.sleep(1)
    self.client.get("/api/ads/next/v2")
    time.sleep(1)
    GQL.collection_ids(self)
    time.sleep(1)
    res = self.client.post("/api/tiny/login/email",
                           params={'register': 'true'},
                           data=f'email=perf_zvquser{self.vuser_id:05}%40zvqmail.com&password=stresstest&active=true',
                           headers={'content-type': 'application/x-www-form-urlencoded'})
    headers_ios_set_token(self, res.json()['result']['token'])
    res = self.client.get("/api/v2/tiny/profile/")
    self.user_id = str(res.json()['result']['profile']['id'])


class AndroidUser01(TaskSet):

    def __init__(self, parent):
        super(AndroidUser01, self).__init__(parent)
        self.vuser_id = ''
        self.token = ''
        self.user_id = ''

    def setup(self):
        """1 раз при старте"""
        pass

    def on_start(self):
        """при старте нового юзера"""
        self.vuser_id = increase_vuser_id()
        logging.info(f'Android01 user{self.vuser_id}')
        self.client.headers.update(
            {'user-agent': 'OpenPlay|4.10.2-DEV|Android|11|unknown Android SDK built for x86',
             # 'x-device-id': 'eade61479a2f2d87',
             'x-app-version': '4.10.2-DEV'
             # 'x-app-build:': '410020001'
             })
        android_login(self)

    @task(1)
    def ads_next_v2(self):
        self.client.get("/api/ads/next/v2")

    @task(1)
    def tiny_set_agreement(self):
        self.client.post("/api/tiny/set_agreement", data='adversting=true&agreement=true',
                         headers={'content-type': 'application/x-www-form-urlencoded'})

    @task(9)
    def grid_request(self):
        grid_params = [
            {"name": "zvuk_home", "market": "ru", "include": "(playlist) (release) (artist) "},
            {"name": "grid3-recommendations", "market": "ru", "include": "(playlist) (release) (artist) "},
            {"name": "grid-podcasts", "market": "ru"},
            {"name": "spring22_grid"},
            {"name": "zvuk-editorial_waves", "market": "ru"},
            {"name": "soundtracks_grid"},
            {"name": "pop_grid"},
            {"name": "games_grid"},
            {"name": "smartreading_grid"}
        ]
        switcher = random.randint(0, len(grid_params)-1)
        self.client.get("/sapi/grid", params=grid_params[switcher])

    @task(1)
    def tiny_releases(self):
        choice_item = random.choice((
            "22854925,21703849,22519893,21184181,22873751,22872679",
            "21745892,22203745",
            "3408091,7474990,10690736",
            "663472,1028135,8187246",
            "3454964,3714447,4109911",
            "22360538,22497153,22493275,22224186,22150229,22392831,20702202,21776256,22216774,22275722,22318589,22403880,22184717,22337466,22274396,22123159,21834233,21753620,22186195,22394281",
            "22360538,22592931,22666427,22516395,22666463,22150229,22585340,22549882,21776256,22275722,22318589,22493275,22661222,22520969,21184181,22337466,22580680,22647134,22571055,22661269"
        ))
        self.client.get("/api/tiny/releases",
                        params={"ids": choice_item},
                        name='/api/tiny/releases')

    @task(1)
    def tiny_playlists(self):
        choice_item = random.choice((
            "5608175,6286714,1124972",
            "2,5685771",
            "5460882,3245011,5800657,1062105"
        ))
        self.client.get("/api/tiny/playlists",
                        params={"ids": choice_item, "include": "playlist_track"},
                        name="/api/tiny/playlists")