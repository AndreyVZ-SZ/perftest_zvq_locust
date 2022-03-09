import logging
import random
import time

from locust import TaskSet, task
# from locust_plugins.csvreader import CSVReader

from graphql import GQL
from methods import *
from vuser import *


def ios_login(self):
    res = self.client.get("/api/v2/tiny/profile/")
    headers_ios_set_token_id(self, res.json()['result']['profile']['token'], str(res.json()['result']['profile']['id']))
    time.sleep(1)
    self.client.get("/api/ads/next/v2")
    time.sleep(1)
    GQL.profiles(self, ["746246625"])
    time.sleep(1)
    self.client.get("/sapi/fetch/",
                    params={
                        'include': '(track release)',
                        'url': '/api/tiny/listen-next/?ids=&limit=10'},
                    name='/sapi/fetch/ (include)')
    time.sleep(1)
    res = self.client.post("/api/tiny/login/email",
                           params={'register': '1'},
                           data=f'email=perf_zvquser{self.vuser_id:05}%40zvqmail.com&password=stresstest&active=true',
                           headers={'content-type': 'application/x-www-form-urlencoded'})
    headers_ios_set_token(self, res.json()['result']['token'])
    res = self.client.get("/api/v2/tiny/profile/")
    self.user_id = str(res.json()['result']['profile']['id'])


class IosUser01(TaskSet):

    def __init__(self, parent):
        super(IosUser01, self).__init__(parent)
        self.vuser_id = ''
        self.token = ''
        self.user_id = ''

    def setup(self):
        """1 раз при старте"""
        pass

    def on_start(self):
        """при старте нового юзера"""
        self.vuser_id = increase_vuser_id()
        logging.info(f'ios01 user{self.vuser_id}')
        self.client.headers.update(
            {'user-agent': 'SberZvuk/4.11.0 (iPhone; iOS 15.2; Scale/3.00)/-Openplay Google-Apps-Script',
             # 'x-device-id': '85743537-98BF-4BBF-AD39-EFD5F239962D',
             'x-app-version': '4.11.0 (3000)'
             })
        ios_login(self)

    @task(1)
    def ads_next_v2(self):
        self.client.get("/api/ads/next/v2")

    @task(9)
    def graphql_req(self):
        switcher = random.randint(1, 9)
        if switcher == 1:
            choice_item = random.choice((["746246625"], ["717993527"], ["438619873"],
                                         ["506527198", "514072620", "386097314", "438615003", "331771699", "388922123",
                                          "371954642", "729177830", "420633244", "669505078", "471759800", "438616750"],
                                         ["331771699", "438615003", "506527198", "438616750", "438618754", "438619873",
                                          "371954642", "420633244", "669505078", "514072620", "388922123", "438612853"]
                                         ))
            GQL.profiles(self, choice_item)
        elif switcher == 2:
            GQL.get_collection_data(self)
        elif switcher == 3:
            GQL.get_disliked_collection(self)
        elif switcher == 4:
            choice_item = random.choice((["3", "4", "2"],
                                         ["1062105", "3363491", "5620367", "3245011", "4", "5460882", "3280849",
                                          "6836620", "6654032", "2", "6574321", "3", "5800657", "6647714"],
                                         ["4389296", "5620367", "5460882", "3", "4", "6836620", "3245011", "5800657",
                                          "2", "6519326", "6836834", "5453365", "5471917", "1062105"]))
            GQL.get_meta(self, choice_item)
        elif switcher == 5:
            GQL.get_available_waves(self)
        elif switcher == 6:
            GQL.get_wave_hidden_content_types(self)
        elif switcher == 7:
            GQL.get_wave_onboarding_buttons(self)
        elif switcher == 8:
            GQL.update_hidden_content_types(self)
        elif switcher == 9:
            GQL.get_wave_content(self)

    @task(5)
    def tiny_grid(self):
        switcher = random.randint(1, 5)
        if switcher == 1:
            self.client.get("/api/tiny/grid", params={"name": "zvuk-home", "market": "ru"})
        elif switcher == 2:
            self.client.get("/api/tiny/grid", params={"name": "grid_search", "market": "ru"})
        elif switcher == 3:
            self.client.get("/api/tiny/grid", params={"name": "new_2021_grid", "market": "ru"})
        elif switcher == 4:
            self.client.get("/api/tiny/grid", params={"name": "grid-podcasts", "market": "ru"})
        elif switcher == 5:
            self.client.get("/api/tiny/grid", params={"name": "zvuk-editorial_waves", "market": "ru"})

    @task(1)
    def tiny_grid_recommendations(self):
        self.client.get("/api/tiny/grid/recommendations", params={"market": "ru"})

    @task(1)
    def tiny_set_agreement(self):
        self.client.post("/api/tiny/set_agreement", data='agreement=1',
                         headers={'content-type': 'application/x-www-form-urlencoded'})

    @task(6)
    def sapi_meta(self):
        switcher = random.randint(1, 6)
        if switcher == 1:
            self.client.get("/sapi/meta",
                            params={
                                'include': '(track artist (release label))',
                                'tracks': '90652526,115025877'},
                            name='/sapi/meta (ios)')
        elif switcher == 2:
            self.client.get("/sapi/meta",
                            params={
                                'include': '(non_music_list (podcast publisher) (abook publisher) episode)',
                                'non_music_lists': '11'},
                            name='/sapi/meta (ios)')
        elif switcher == 3:
            self.client.get("/sapi/meta",
                            params={
                                'artists': '873552',
                                'include': '(artist(popular-track release :first 3)(release :first 2)(related-artists :first 10))'},
                            name='/sapi/meta (ios)')
        elif switcher == 4:
            choice_item = random.choice(('114739629,114189747,112858098', '78191011', '78191011,78191055,78190960',
                                         '115645279,82678166,78510394', '115645279',
                                         '115903770,115452616,114929301,114555943,114189372,113886493,112729397,112694907,112484827,112083484,111881687,111523446,110789040,110274128,109994683,109389157,108785941,108455870,108189238,107704175,107439369,107439485,107439579,107439606,107439640,107439671,107439706,107439708,107439737,107439778,107439852,107439910,107439979,107440013,107440053,107440112,107440140,107440159,107440179,107440207,107440291,107440315,107440365,107440367,107440369,107440436,107440446,107440483,107440533,107440551,107440578,107440670,107440695,107440699,107440749,107440758,107440773,107440839,107440918,107440932,107440977,107440997,107441020,107441048,107441065,107441071,107441109,107441115,107441171,107441205,107441215,107441267,107441310,107441352,107441407,107441417,107441419,107441427,107441439,107441442,107441497,107441499,107441501,107441508,107441519,107441523,107441525,107441568,107441570,107441572,107336864,107039507,106532056,91757453,91391701,90774760,90762986,90505529,90207967,89644613'
                                         ))
            self.client.get("/sapi/meta",
                            params={
                                'episodes': choice_item,
                                'include': '(episode (podcast publisher) listened_state)'},
                            name='/sapi/meta (ios)')
        elif switcher == 5:
            self.client.get("/sapi/meta",
                            params={
                                'include': '(release (related-releases :first 10) label track artist)',
                                'releases': '5997946'},
                            name='/sapi/meta (ios)')
        elif switcher == 6:
            self.client.get("/sapi/meta",
                            params={
                                'include': '(podcast publisher)',
                                'podcasts': '12889455'},
                            name='/sapi/meta (ios)')

    @task(1)
    def tiny_artists(self):
        choice_item = random.choice((
            "40397,130059,135149",
            "86115,105197,136866",
            "167841708,1458171,210148173,29915193,191237956,328670,238181,235894,209444697,193865705,292404,1148324,3409749,60914843,806438,205892039,209825554,2201433,3231844,873552,209589731,60021,658564,1574474,30207595,20619396,209996635,841863,1570980,209895325",
            "59907476,33178074,755169,3363462,99462936,29915193,328670,238181,209837488,1724799,59920939,1129206,3372662,292404,211639462,211289874,873552,217547,210756246,60021,727552,1574474,30207595,210494423,104460,157965703,3159506,1148324,361872,806438"
        ))
        self.client.get("/api/tiny/artists",
                        params={"ids": choice_item},
                        name='/api/tiny/artists')

    @task(1)
    def tiny_releases(self):
        choice_item = random.choice((
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
    def tiny_tracks(self):
        switcher = random.randint(1, 2)
        if switcher == 1:
            choice_item = random.choice((
                "115392270,115693122,113982688,115392189,115640661,115894257,115454448,115660899,114710717,114878522,115449148,115392183,115466950,115626216,115701857,115453771,115386976,114713277,115383915,115687935",
                "114801873,114574250,115856570,114770535,115181103,115509766,115687953,115721729,114690019,115626469,109573052,114878107,115700541,115699559,115116252,115453776,115827914,115675134,115499636,113942535"
            ))
            self.client.get("/api/tiny/tracks",
                            params={"ids": choice_item},
                            name='/api/tiny/tracks')
        elif switcher == 2:
            choice_item = random.choice(("68439511,68439511",
                                         "68216761,68216765,68438945",
                                         "114622397", "115383915,115383915,114690019,114690019",
                                         "115712814,115712814,115712814,115712814,115712814,115712814,115712814,115712814,115712814",
                                         "114331640,114478000,114151709,115706177,114477713,112642277,114476569,114973283,115723678,113036334,114973284,115662210,115712814,114581936,115705470,115417281,115386967,114582243,114475642,114729346",
                                         "113151575,93010217,112174331,86435153,68438945,109589345,68216761,113475691,68216765,113151577,90138630,109007117,108329396,113475676,113475686,46068664,113475687,68438935,46068657,91936085"
                                         ))
            self.client.get("/api/tiny/tracks",
                            params={"ids": choice_item, "include": "release"},
                            name='/api/tiny/tracks')

    @task(1)
    def tiny_track_stream(self):
        choice_item = random.choice(('114690019', '114622397', '114690019', '113151575', '68439511', '46068557',
                                     '115712814', '114151709', '115386967'))
        self.client.get("/api/tiny/track/stream",
                        params={"id": choice_item, "quality": "high"},
                        name='/api/tiny/track/stream')

    @task(1)
    def tiny_musixmatch_lyrics(self):
        choice_item = random.choice(('114690019', '115383915', '114622397', '113151575', '68439511', '46068557',
                                     '114151709', '115712814', '115386967'))
        self.client.get("/api/tiny/musixmatch/lyrics/",
                        params={"track_id": choice_item, "translation": "1"},
                        name='/api/tiny/musixmatch/lyrics/')

    @task(1)
    def tiny_artist_id_releases(self):
        self.client.get("/api/tiny/artist/873552/releases",
                        params={"limit": "20", "offset": "0"},
                        name='/api/tiny/artist/[id]/releases')

    @task(1)
    def tiny_popular_tracks(self):
        choice_item = random.choice(('873552'))
        self.client.get("/api/tiny/popular-tracks",
                        params={"artist": choice_item, "limit": "980", "offset": "20"},
                        name='/api/tiny/popular-tracks')
        # /api/tiny/popular-tracks?artist=873552&limit=980&offset=20

    @task(1)
    def tiny_suggest(self):
        choice_item = random.choice(('week', 'sun', 'moon', 'girl'))
        self.client.get("/api/tiny/suggest",
                        params={"limit": "3", "offset": "0", "query": choice_item,
                                "type": "episode,playlist,artist,track,release"},
                        name='/api/tiny/suggest')

    @task(1)
    def sapi_search(self):
        choice_item = random.choice(('week', 'sun', 'moon', 'girl'))
        self.client.get("/sapi/search",
                        params={"include": "track", "limit": "25", "offset": "0", "query": choice_item,
                                "user_id": self.user_id},
                        name='/sapi/search')

    @task(1)
    def sapi_fetch(self):
        self.client.get("/sapi/fetch/",
                        params={"include": "(track release)", "url": "/api/tiny/listen-next/?ids=&limit=10"},
                        name='/sapi/fetch/')
