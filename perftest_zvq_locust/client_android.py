import logging
import random
import time

from locust import TaskSet, task
# from locust_plugins.csvreader import CSVReader

from graphql import GQL
from methods import *
from vuser import *
from weight import weight


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
                           headers={'content-type': 'application/x-www-form-urlencoded'},
                           name="/api/tiny/login/email")
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

    @task(weight["/api/ads/next/v2"])
    def ads_next_v2(self):
        self.client.get("/api/ads/next/v2")

    @task(weight["/api/tiny/set_agreement"])
    def tiny_set_agreement(self):
        self.client.post("/api/tiny/set_agreement", data='adversting=true&agreement=true',
                         headers={'content-type': 'application/x-www-form-urlencoded'})

    @task(weight["/api/v2/tiny/profile/"])
    def api_v2_tiny_profile(self):
        self.client.get("/api/v2/tiny/profile/")

    @task(weight["/api/tiny/graphql"])
    def graphql(self):
        switcher = random.randint(1, 6)
        if switcher == 1:
            #"ids": ["717993527"]
            GQL.get_profiles(self, ids=["729177830", "386097314", "669505078", "331771699", "388922123", "471759800", "514072620", "371954642", "438616750", "506527198", "420633244", "438615003"])
        elif switcher == 2:
            GQL.collection_ids(self)
        elif switcher == 3:
            GQL.hidden_content_types(self)
        elif switcher == 4:
            GQL.available_waves(self)
        elif switcher == 4:
            GQL.wave_content(self)
        elif switcher == 5:
            choice_item = random.choice((["3245011"], ["6626390"], ["5800657"], ["7072660"], ["2", "4"]))
            GQL.get_playlists_android(self, ids=choice_item)
        elif switcher == 6:
            choice_item = random.choice((["6923325", "6868356", "6923300", "6868363", "6923275"],
                                         ["7036625", "6709336", "6745682", "6745855", "6768737", "6769741", "6770837"]))
            GQL.get_public_profile_playlists_with_fixed_covers(self, ids=choice_item)



    @task(weight["/sapi/grid"])
    def sapi_grid(self):
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
        self.client.get("/sapi/grid", params=grid_params[switcher], name="/sapi/grid")

    @task(weight["/api/tiny/releases"])
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

    @task(weight["/api/tiny/playlists"])
    def tiny_playlists(self):
        choice_item = random.choice((
            "5608175,6286714,1124972",
            "2,5685771",
            "5460882,3245011,5800657,1062105"
        ))
        self.client.get("/api/tiny/playlists",
                        params={"ids": choice_item, "include": "playlist_track"},
                        name="/api/tiny/playlists")

    @task(weight["/api/tiny/tracks"])
    def tiny_tracks(self):
        choice_item = random.choice((
            "10308201,35249919,45423527,14641503,5826388,17760217,28526660,83430866,10381371,24945786,77905355,115059634,70144757,34848339",
            "116347671,116347674,116347664,116347669,116347663,116347667,116347665,116347670,116347668,116347673,116347666,116347672",
            "110064071,112682608,108151297,108506417,114282153,104911494,110060634,105018063,110373642,104642998,110527642,109329303,108324227,108324226,73676816,90670901,90885182,76419009,92791333,90823496,86308872,106268385,69372333,89621330,82376435,87962394,35078253,53638558,88349777,84876992,88836238,83673980,87773124,78288495,87971523,82695521,82023290,23552161,86180320,63854017",
            "116347671,116347674,116347664,116347669,116347663,116347667,116347665,116347670,116347668,116347673,116347666,116347672",
            "112465289,68312836,62528918,57566871,57791893,57758071,76934897,91825378,46037397,86896053,62130211,45882394,46838637,37798841,91825315,57563923,68450686,67688493,57946954,105930811,65594022",
            "116257431,116257421,116257430,116257428,116257432,116257420,116257427,116257433,116257424,116257422,116257429,116257426,116257423,116257425"
        ))
        self.client.get("/api/tiny/tracks",
                        params={"ids": choice_item},
                        name="/api/tiny/tracks")

    @task(weight["/api/tiny/track/stream"])
    def tiny_track_stream(self):
        choice_item = random.choice(("35249919", "115059634", "10381371", "34848339", "68193075", "10519220", "61713423"))
        self.client.get("/api/tiny/track/stream",
                        params={"id": choice_item, "quality": "mid"},
                        name='/api/tiny/track/stream')

    @task(50)
    def sapi_meta(self):
        choice_params = [
            {"episodes": "116249546,115977200,115645272,115174081,114640173,114263748,113951037,113675062,112775663,112613812,112556252,112297109,112142435,111872381,111659564,111146501,110958711,110684197,110381862,110079390,110039063,109847229,109491802,108852899,108611750,108512749,108342204,108269664,108269667,108005221,107938147,107616883,107424391,107109383,107109391,106925463,106606233,106479199,106226240,106090174,106036371,105923415,105819449,105795512,105518378,105432322,105379962,105012260,104652538,104575326,104215423,92830586,92663754,92663783,92164972,91812731,91613849,91613882,91078714,90887593,90763026,90636269,90245166,90207999,90062508,89737485,89548718,89548722,89040197,89040202,89040212,89040227,88790903,88790910,88667392,88432974,88375462,88323416,88323418,88207490,88207494,88207503,88005721,87980708,87959708,87906301,87878034,87878036,87784750,87675407,87638028,87186192,87186200,86875205,86875210,86875213,86875220,86875221,86875226,86875227,86875237,86875238,86875245,86068896,86068902,86068906,86068910,86068921,86068927,86068944,86068971,85214601,85214609,84904583,84904588,84904594,84546974,84546994,84547014,84328747,84242069,84115234,83858751,83806503,83793243,83777796,83629445,83629447"},
            {"episodes": "83257942,83257946,83150286,83114974,83094963,83094964,83094968,83094971,82944366,82835940,82835941,82835943,82835948,82678217,82678220,82579593,82579599,82395565,82390102,82390104,82307513,82288102,82284573,82284574,82206821,82181078,82181083,82168006,82168012,82168016,82074474,82074481,82015503,82015527,82015532,81866285,81838118,81838164,81838214,81557946,81516027,81516042,81516070,81405523,81405539,81405579,81405617,81405623,81195544,81195576,80985709,80985712,80985717,80985715,80763218,80985719,80763223,80705064,80126596,80126473,79812574,79800507,79800510,79604099,79583984,79584002,79513167,79486772,79486840,79285619,79285661,79208722,79165922,79165924,79028729,78984343,78920763,78908333,78830888,78805233,78535665,78601398,78487771,78487870,78377286,78367588,78367622,78367619,78367626,78367629,78129940,78103985,78103986,77857181,77857182,77826426,77826427,77826428,77826429,77826430,77311502,77311503,77217070,77217071,77217072,77217073,77217074,77217075,77217076,77217077,77217079,77217078,77217080,77217081,76689278,76689279,76689280,76689281,76689282,76689283,76689284,76689285,76689286,76689287,76689288,76689289,76689290,76689291"},
            {"episodes": "76689292,76689293,76689294,76689295,76689296,76689297,76689298,76689299,76689300,76689301,76689302,76689303,76689304,76689305,76689306,76689307,76689308,76689309,76689310,76689311,76689312,76689313,76689314,76689315,76689316,76689317,76689318,76689319,76689320,76689321,76689322,76689323,76689324,76689325,76689326,76689327,76689328,76689329,76689330,76689331,76689332,76689333,76689334,76689335,76689336,76689337,76689338,76689339,76689340,76689341,76689342,76689343,76689344,76689345,76689346,76689347,76689348,76689349,76689350,76689351,76689352,76689353,76689354,76689355,76689356,76689357,76689358,76689359,76689360,76689361,76689362,76689363,76689364,76689365,76689366,76689367,76689368,76689369,76689370,76689371,76689372,76689373,76689374,76689375,76689376,76689377,76689378,76689379,76689380,76689381,76689382,76689383,76689384,76689385,76689386,76689387,76689388,76689389,76689390,76689391,76689392"},
            {"episodes": "116036609,114491287,112779475,112257120,110200369,110200384,108455809,106532176,105305492,104351366,104351464,90162776,88666928,88433910,84904148,82943889,81865832,80762724,80763221,80763352,80763483,80763554,80763589,80763698,80763775,80763811,80763821,75889758,75889759,75889760,75889761,75889762,75889763,75889764,75889765,75889766,75889767,75889769,75889770,75889771,75889772,75889773,75889774"},
            {"episodes": "107424184"},
            {"podcasts": "12942247,12874305,12882611,12882607"},
            {"artists": "210756246", "include": "(artist (related-artists :first 20))"},
            {"releases": "22728561", "include": "(release (related-releases :first 20))"},
            {"releases": "22666427", "include": "(release (related-releases :first 20))"}
        ]
        switcher = random.randint(0, len(choice_params) - 1)
        self.client.get("/sapi/meta", params=choice_params[switcher], name="/sapi/meta")

    @task(weight["/api/tiny/artists"])
    def tiny_artists(self):
        choice_item = random.choice(("5586659", "339816"))
        self.client.get("/api/tiny/artists", params={"ids": choice_item}, name='/api/tiny/artists')

    @task(weight["/sapi/search"])
    def sapi_search(self):
        self.client.get("/sapi/search",
                        params={"query": "rain", "include": "artist track release playlist episode", "limit": "6",
                                "offset": "0", "user_id": self.user_id},
                        name='/sapi/search')

    @task(weight["/api/tiny/musixmatch/lyrics"])
    def tiny_musixmatch_lyrics(self):
        choice_item = random.choice(('114690019', '115383915', '114622397', '113151575', '68439511', '46068557',
                                     '114151709', '115712814', '115386967'))
        self.client.get("/api/tiny/musixmatch/lyrics",
                        params={"track_id": choice_item, "translation": "true"},
                        name="/api/tiny/musixmatch/lyrics")

