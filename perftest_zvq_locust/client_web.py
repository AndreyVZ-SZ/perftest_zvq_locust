import logging
import random
import time

from locust import TaskSet, task
# from locust_plugins.csvreader import CSVReader

from graphql import GQL
from methods import *
from vuser import *


class FlowException(Exception):
    pass


def web_login(self):
    self.client.get("/")
    time.sleep(1)
    res = self.client.get("/api/tiny/profile")
    headers_set_token_id(self, res.json()['result']['token'], str(res.json()['result']['id']))
    time.sleep(1)
    self.client.get("/api/ads/next/v2")
    time.sleep(1)
    self.client.get("/sapi/grid", params={"name": "zvuk_grid_top100"})
    time.sleep(1)
    self.client.post("/api/tiny/clickstream-web")
    time.sleep(1)
    GQL.get_profile(self, ids=[438615003, 438612853, 438616750, 371954642, 669505078, 386097314, 388922123, 446775763,
                               297277082, 438619873, 471759800, 331771699], country_code="ru")
    time.sleep(1)
    GQL.get_playlists(self, ids=[1062105], shortTrackList=False, limNumber=3, country_code="ru")

    res = self.client.get("/sapi/meta",
                          params={
                              'tracks': "108506417,115025877,113850252,108151297,109329303,112411200,113523986,112186985,114146877,90885182,105312812,114640322,114283019,87971523,110060634,108494292,87962394,110064071,111055639,113056172,82376435,82933129,88836233,80948653,87773124,113130457,91780188,106200598,88836238,114986983,106628608,90166466,115392189,83250618,53638558,111735924,106023566,82726211,105174276,77830364,68995148,114717620,115117121,113982688,109488051,69498564,67529723,85124486,64406426,114717699,73226141,79828594,70558248,84546619,68824646,89042315,112776265,90823496,114985435,109937583,114580754,115693122,107059662,61540474,115166877,90965391,67529725,92791333,110527642,114713952,110373642,113976323,71366405,114335633,87772952,92791334,82023290,89621330,107458059,114007202,106686716,77677633,108324227,69802670,110473479,113384795,115020184,47787072,58377272,109488106,91397931,110856030,82293829,106545077,106202820,90533342,104851454,114177675,115012292,115224071",
                              'include': "(track (release label) artist)"},
                          name='/sapi/meta (tracks)')
    # log_info(res)
    # logging.info(self.client.headers)
    time.sleep(1)
    self.client.get("/api/tiny/login/sber/get_params/")
    time.sleep(1)
    res = self.client.post("/api/login_or_register",
                           data=f'email=perf_zvquser{self.vuser_id:05}%40zvqmail.com&password=stresstest&active=true',
                           headers={'content-type': 'application/x-www-form-urlencoded'})
    headers_set_token(self, res.json()['result']['sauth']['value'])
    time.sleep(1)
    res = self.client.get("/api/tiny/profile")
    # logging.info(str(res.json()))
    headers_set_id(self, str(res.json()['result']['id']))
    # logging.info(self.client.headers)
    time.sleep(1)
    self.client.get("/api/tiny/subscription", params={"app": "zvooq"})
    time.sleep(1)
    self.client.get("/sapi/grid", params={"name": "zvuk_grid_main"}, name='/sapi/grid')
    time.sleep(1)
    self.client.get("/sapi/grid", params={"name": "zvuk_grid_main_custom_ad"}, name='/sapi/grid')
    time.sleep(1)


class WebUser01(TaskSet):

    def __init__(self, parent):
        super(WebUser01, self).__init__(parent)
        self.vuser_id = ''
        self.token = ''
        self.user_id = ''
        # self.gql_switcher = 0
        # self.grid_switcher = 0

    def setup(self):
        """1 раз при старте"""
        pass

    def on_start(self):
        """при старте нового юзера"""
        self.vuser_id = increase_vuser_id()
        logging.info(f'web01 user{self.vuser_id}')
        self.client.headers.update(
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0 Google-Apps-Script'})
        web_login(self)

    def on_stop(self):
        self.client.post("/api/tiny/logout")

    @task(7)
    def graphql_request(self):
        switcher = random.randint(1, 8)
        if switcher == 1:
            GQL.playlists(self, country_code="ru")
        elif switcher == 2:
            GQL.user_collection(self, country_code="ru")
        elif switcher == 3:
            GQL.get_all_hidden_collection(self, country_code="ru")
        elif switcher == 4:
            choice_item = random.choice(([1062105], [1124972]))
            GQL.get_playlists(self, ids=choice_item, shortTrackList=False, limNumber=3, country_code="ru")
        elif switcher == 5:
            GQL.profile(self, ids=[438616750, 371954642, 420633244, 514072620, 386097314, 388922123, 297277082,
                                       438619873, 471759800, 438618754, 331771699, 506527198], country_code="ru")
        elif switcher == 6:
            choice_item = random.choice((115020184, 115025877))
            GQL.collection(self, id=choice_item, country_code="ru")
        elif switcher == 7:
            GQL.hidden_collection(self, id=115020184, country_code="ru")
        else:
            GQL.get_tracks(self, ids=[113523986], country_code="ru")

    @task(5)
    def grid_request(self):
        switcher = random.randint(1, 5)
        if switcher == 1:
            self.client.get("/sapi/grid", params={"name": "zvuk_grid_main"}, name='/sapi/grid')
        elif switcher == 2:
            self.client.get("/sapi/grid", params={"name": "zvuk_grid_main_custom_ad"}, name='/sapi/grid')
        elif switcher == 3:
            self.client.get("/sapi/grid", params={'name': 'zvuk_grid_top100'}, name='/sapi/grid')
        elif switcher == 4:
            self.client.get("/sapi/grid", params={'name': 'zvuk_grid_errors'}, name='/sapi/grid')
        else:
            self.client.get("/sapi/grid", params={'name': 'grid_web_new_playlists'}, name='/sapi/grid')

    @task(3)
    def sapi_meta_request(self):
        switcher = random.randint(1, 3)
        if switcher == 1:
            choice_item = random.choice(('93010217',
                                         '108506417,115025877,113850252,108151297,109329303,112411200,113523986,112186985,114146877,90885182,105312812,114640322,114283019,87971523,110060634,108494292,87962394,110064071,111055639,113056172,82376435,82933129,88836233,80948653,87773124,113130457,91780188,106200598,88836238,114986983,106628608,90166466,115392189,83250618,53638558,111735924,106023566,82726211,105174276,77830364,68995148,114717620,115117121,113982688,109488051,69498564,67529723,85124486,64406426,114717699,73226141,79828594,70558248,84546619,68824646,89042315,112776265,90823496,114985435,109937583,114580754,115693122,107059662,61540474,115166877,90965391,67529725,92791333,110527642,114713952,110373642,113976323,71366405,114335633,87772952,92791334,82023290,89621330,107458059,114007202,106686716,77677633,108324227,69802670,110473479,113384795,115020184,47787072,58377272,109488106,91397931,110856030,82293829,106545077,106202820,90533342,104851454,114177675,115012292,115224071',
                                         '79828594'))
            # "(track (release label) artist)"
            self.client.get("/sapi/meta",
                            params={
                                'tracks': choice_item,
                                'include': "(track  )"},
                            name='/sapi/meta (tracks)')
        elif switcher == 2:
            choice_item = random.choice(('5586659', '211625099'))
            self.client.get("/sapi/meta",
                            params={
                                'artists': choice_item,
                                'include': "(artist (release false :first 1000))"},
                            name='/sapi/meta (artists)')

    @task(1)
    def tiny_subscription(self):
        self.client.get("/api/tiny/subscription", params={"app": "zvooq"})

    @task(1)
    def tiny_get_agreement(self):
        self.client.get("/api/v2/tiny/get_agreement")

    @task(1)
    def tiny_set_agreement(self):
        self.client.post("/api/tiny/set_agreement", data='adversting=true&agreement=true',
                         headers={'content-type': 'application/x-www-form-urlencoded'})

    @task(1)
    def tiny_track_stream(self):
        choice_item = random.choice(('93010217', '79828594'))
        self.client.get("/api/tiny/track/stream",
                        params={"id": choice_item, "quality": "high"},
                        name='/api/tiny/track/stream')

    @task(1)
    def tiny_artists(self):
        self.client.get("/api/tiny/artists",
                        params={"ids": "5586659"},
                        name='/api/tiny/artists')

    @task(1)
    def tiny_artist_related(self):
        self.client.get("/api/tiny/artist/related", params={"id": "5586659", "limit": "20"},
                        name="/api/tiny/artist/related")

    @task(1)
    def tiny_popular_tracks(self):
        choice_item = random.choice(('5586659', '211625099'))
        self.client.get("/api/tiny/popular-tracks",
                        params={"artist": choice_item, "limit": "200"},
                        name='/api/tiny/popular-tracks')
        #                 params={"artist": "211625099", "limit": "10"},

    @task(1)
    def tiny_suggest(self):
        self.client.get("/api/tiny/suggest",
                        params={"query": "rain", "limit": "2", "type": "artist,release,playlist,track,episode"},
                        name='/api/tiny/suggest')

    @task(1)
    def ads_next_v2(self):
        self.client.get("/api/ads/next/v2")

    @task(1)
    def user_library(self):
        self.client.get("/api/user/library", params={"return_shared_playlists": "true", "username": "zvooqplay"},
                            name='/api/user/library')

    @task(1)
    def sapi_search(self):
        self.client.get("/sapi/search",
                        params={"query": "rain", "include": "artist track release playlist episode", "limit": "6",
                                "offset": "0", "user_id": self.user_id},
                        name='/sapi/search')

    @task(1)
    def tiny_grid_sberbox_homepage(self):
        self.client.get("/api/tiny/grid/sberbox-homepage", headers={'Content-Type': 'application/json'})

    @task(1)
    def sberbank_subscription_status(self):
        self.client.get("/api/sberbank/subscription_status", headers={'X-AUTH-KEY': 'a5f02f3675c746889878f9777ac715a6da690c8f', 'Content-Type': 'application/json'})


class WebUser02(TaskSet):

    def __init__(self, parent):
        super(WebUser02, self).__init__(parent)
        self.vuser_id = ''
        self.token = ''

    def setup(self):
        """1 раз при старте"""
        pass

    def on_start(self):
        """при старте нового юзера"""
        self.vuser_id = increase_vuser_id()
        logging.info(f'web02 user{self.vuser_id}')
        self.client.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0'})
        # self.client.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0 Google-Apps-Script'})
        web_login(self)

    @task(1)
    def user_cycle(self):
        pass
