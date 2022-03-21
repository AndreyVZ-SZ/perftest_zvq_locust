import logging
import random
import time
import json

from locust import TaskSet, task
# from locust_plugins.csvreader import CSVReader

from graphql import GQL
from methods import *
from vuser import *
from weight import weight


class FlowException(Exception):
    pass


def web_login(self):
    self.client.get("/")
    time.sleep(1)
    res = self.client.get("/api/tiny/profile")
    headers_set_token_id(self, res.json()['result']['token'], str(res.json()['result']['id']))
    time.sleep(1)
    # log_info(res)
    # logging.info(self.client.headers)
    self.client.get("/api/tiny/login/sber/get_params/")
    time.sleep(1)
    res = self.client.post("/api/login_or_register",
                           # data=f'email=perf_zvquser{self.vuser_id:05}%40zvqmail.com&password=stresstest&active=true',
                           data=f'email={get_email(self.vuser_id)}&password=stresstest&active=true',
                           headers={'content-type': 'application/x-www-form-urlencoded'})
    check_response(res)
    headers_set_token(self, res.json()['result']['sauth']['value'])
    time.sleep(1)
    res = self.client.get("/api/tiny/profile")
    headers_set_id(self, str(res.json()['result']['id']))
    # logging.info(str(res.json()))
    # logging.info(self.client.headers)
    time.sleep(1)



class WebUser01(TaskSet):

    def __init__(self, parent):
        super(WebUser01, self).__init__(parent)
        self.vuser_id = ''
        self.token = ''
        self.user_id = ''

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

    # @task
    # def pass_task(self):
    #     pass

    @task(weight["/api/ads/next/v2"])
    def ads_next_v2(self):
        self.client.get("/api/ads/next/v2")

    @task(weight["/"])
    def ads_next_v2(self):
        self.client.get("/")

    @task(weight["/api/tiny/profile"])
    def api_tiny_profile(self):
        self.client.get("/api/tiny/profile")

    @task(weight["/api/tiny/graphql"])
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

    @task(weight["/sapi/grid"])
    def sapi_grid(self):
        grid_params = [
            {"name": "zvuk_grid_main"},
            {"name": "zvuk_grid_main_custom_ad"},
            {"name": "zvuk_grid_errors"},
            {"name": "zvuk_grid_top100"},
            {"name": "grid_web_new_playlists"}
        ]
        switcher = random.randint(0, len(grid_params)-1)
        self.client.get("/sapi/grid", params=grid_params[switcher], name="/sapi/grid")

    @task(weight["/sapi/meta"])
    def sapi_meta(self):
        switcher = random.randint(1, 2)
        if switcher == 1:
            choice_item = random.choice(('93010217',
                                         '108506417,115025877,113850252,108151297,109329303,112411200,113523986,112186985,114146877,90885182,105312812,114640322,114283019,87971523,110060634,108494292,87962394,110064071,111055639,113056172,82376435,82933129,88836233,80948653,87773124,113130457,91780188,106200598,88836238,114986983,106628608,90166466,115392189,83250618,53638558,111735924,106023566,82726211,105174276,77830364,68995148,114717620,115117121,113982688,109488051,69498564,67529723,85124486,64406426,114717699,73226141,79828594,70558248,84546619,68824646,89042315,112776265,90823496,114985435,109937583,114580754,115693122,107059662,61540474,115166877,90965391,67529725,92791333,110527642,114713952,110373642,113976323,71366405,114335633,87772952,92791334,82023290,89621330,107458059,114007202,106686716,77677633,108324227,69802670,110473479,113384795,115020184,47787072,58377272,109488106,91397931,110856030,82293829,106545077,106202820,90533342,104851454,114177675,115012292,115224071',
                                         '79828594'))
            # "(track (release label) artist)"
            self.client.get("/sapi/meta",
                            params={
                                'tracks': choice_item,
                                'include': "(track  )"},
                            name="/sapi/meta")
        elif switcher == 2:
            choice_item = random.choice(('5586659', '211625099'))
            self.client.get("/sapi/meta",
                            params={
                                'artists': choice_item,
                                'include': "(artist (release false :first 1000))"},
                            name="/sapi/meta")

    @task(1)
    def tiny_subscription(self):
        self.client.get("/api/tiny/subscription", params={"app": "zvooq"})

    @task(weight["/api/v2/tiny/get_agreement"])
    def tiny_get_agreement(self):
        self.client.get("/api/v2/tiny/get_agreement")

    @task(weight["/api/tiny/set_agreement"])
    def tiny_set_agreement(self):
        self.client.post("/api/tiny/set_agreement", data='adversting=true&agreement=true',
                         headers={'content-type': 'application/x-www-form-urlencoded'})

    @task(weight["/api/tiny/track/stream"])
    def tiny_track_stream(self):
        choice_item = random.choice(('93010217', '79828594'))
        self.client.get("/api/tiny/track/stream",
                        params={"id": choice_item, "quality": "high"},
                        name="/api/tiny/track/stream")

    @task(weight["/api/tiny/artists"])
    def tiny_artists(self):
        self.client.get("/api/tiny/artists",
                        params={"ids": "5586659"},
                        name="/api/tiny/artists")

    @task(weight["/api/tiny/artist/related"])
    def tiny_artist_related(self):
        self.client.get("/api/tiny/artist/related", params={"id": "5586659", "limit": "20"},
                        name="/api/tiny/artist/related")

    @task(weight["/popular_tracks"])
    def tiny_popular_tracks(self):
        choice_item = random.choice(('5586659', '211625099'))
        self.client.get("/api/tiny/popular-tracks",
                        params={"artist": choice_item, "limit": "200"},
                        name='/api/tiny/popular-tracks')
        #                 params={"artist": "211625099", "limit": "10"},

    @task(weight["/api/tiny/suggest"])
    def tiny_suggest(self):
        self.client.get("/api/tiny/suggest",
                        params={"query": "rain", "limit": "2", "type": "artist,release,playlist,track,episode"},
                        name="/api/tiny/suggest")

    @task(weight["/api/v2/user/library"])
    def user_library(self):
        self.client.get("/api/user/library", params={"return_shared_playlists": "true", "username": "zvooqplay"},
                            name='/api/user/library')

    @task(weight["/sapi/search"])
    def sapi_search(self):
        self.client.get("/sapi/search",
                        params={"query": "rain", "include": "artist track release playlist episode", "limit": "6",
                                "offset": "0", "user_id": self.user_id},
                        name="/sapi/search")

    @task(weight["/api/tiny/grid/sberbox-homepage"])
    def tiny_grid_sberbox_homepage(self):
        self.client.get("/api/tiny/grid/sberbox-homepage", headers={'Content-Type': 'application/json'})

    @task(weight["/api/sberbank/subscription_status/"])
    def sberbank_subscription_status(self):
        self.client.get("/api/sberbank/subscription_status/", headers={'X-AUTH-KEY': 'a5f02f3675c746889878f9777ac715a6da690c8f', 'Content-Type': 'application/json'})

    @task(weight["/api/tiny/radio"])
    def tiny_radio(self):
        choice_item = random.choice(("703580", "888840"))
        self.client.get("/api/tiny/radio", params={"ids": choice_item, "type": "artist", "limit": "30"}, name="/api/tiny/radio")

    @task(weight["/api/v2/data-flow/"])
    def data_flow(self):
        self.client.post("/api/v2/data-flow", headers={'X-Device-Id': '683e6d9122708645fd169aac271852e2'})

    @task(weight["/api/tiny/musixmatch/lyrics"])
    def tiny_musixmatch_lyrics(self):
        choice_item = random.choice(('114690019', '115383915', '114622397', '113151575', '68439511', '46068557',
                                     '114151709', '115712814', '115386967'))
        self.client.get("/api/tiny/musixmatch/lyrics",
                        params={"track_id": choice_item},
                        name="/api/tiny/musixmatch/lyrics")

