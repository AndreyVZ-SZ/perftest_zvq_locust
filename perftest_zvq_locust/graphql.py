import locustfile


class GQL:

    def choose_operation(self):
        pass

    #------Android-------


    def collection_ids(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "collectionIds",
                                        "variables": {},
                                        "query": "query collectionIds { collection { __typename tracks { __typename ...CollectionItemGqlFragment } artists { __typename ...CollectionItemGqlFragment } releases { __typename ...CollectionItemGqlFragment } playlists { __typename ...CollectionItemGqlFragment } books { __typename ...CollectionItemGqlFragment } chapters { __typename ...CollectionItemGqlFragment } episodes { __typename ...CollectionItemGqlFragment } profiles { __typename ...CollectionItemGqlFragment } } getPlayState { __typename episodes chapters } hidden_collection { __typename tracks { __typename ...HiddenItemGqlFragment } artists { __typename ...HiddenItemGqlFragment } } } fragment CollectionItemGqlFragment on CollectionItem { __typename id collectionLastModified } fragment HiddenItemGqlFragment on CollectionItem { __typename id collectionLastModified }"
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (droid collectionIds)'
                                    )
        return response


    #-------IOS----------

    def get_wave_content(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "GetWaveContent",
                                        "query": "query GetWaveContent($waveId: ID!, $limit: Int, $waveItem: WaveItemInput, $ban: Boolean, $localTime: DateTime!) {\n  wave {\n    __typename\n    waveContent(\n      contentInput: {waveId: $waveId, limit: $limit, waveItem: $waveItem, ban: $ban, localtime: $localTime}\n    ) {\n      __typename\n      ...WaveItemContextItem\n      content {\n        __typename\n        ... on Digest {\n          id\n          title\n          streamId\n          duration\n          image {\n            __typename\n            src\n          }\n          author\n        }\n        ... on LifestyleNews {\n          id\n          title\n          streamId\n          duration\n          image {\n            __typename\n            src\n          }\n          author\n        }\n        ... on SberZvukDigest {\n          id\n          title\n          streamId\n          duration\n          image {\n            __typename\n            src\n          }\n          author\n        }\n        ... on Teaser {\n          id\n          title\n          streamId\n          duration\n          image {\n            __typename\n            src\n          }\n          author\n        }\n        ... on Jingle {\n          id\n          title\n          streamId\n          duration\n          image {\n            __typename\n            src\n          }\n          author\n        }\n        ... on Horoscope {\n          id\n          title\n          streamId\n          duration\n          image {\n            __typename\n            src\n          }\n          author\n        }\n      }\n    }\n  }\n}\nfragment WaveItemContextItem on WaveItem {\n  __typename\n  itemId\n  itemType\n  compilationId\n  sequence\n  skippable\n}",
                                        "variables": {
                                            "ban": False,
                                            "limit": 5,
                                            "localTime": "2022-02-23T19:59:14.535+04:00",
                                            "waveId": "1",
                                            "waveItem": {
                                                "compilationId": "582",
                                                "itemId": "44",
                                                "itemType": "jingle",
                                                "sequence": 1
                                            }
                                        }
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios GetWaveContent)'
                                    )
        return response

    def update_hidden_content_types(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                            "operationName": "updateHiddenContenTypes",
                                            "query":
                                            '''
                                            mutation updateHiddenContenTypes($lifestyleNews: [LifestyleNewsTypes!]!, $digest: [DigestTypes!]!, $horoscope: [ZodiacSigns!]!, $teaser: [TeaserGenres!]!) {
                                              wave {
                                                __typename
                                                updateHiddenContentTypes(
                                                  hiddenContentTypes: {lifestyleNews: $lifestyleNews, digest: $digest, horoscope: $horoscope, teaser: $teaser}
                                                )
                                              }
                                            }
                                            ''',
                                            "variables": {
                                                "digest": ["rambler_politics"],
                                                "horoscope": ["aries", "taurus", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"],
                                                "lifestyleNews": ["sport", "travelling", "money", "people"],
                                                "teaser": ["show_business", "psychology", "education", "child", "sport", "art", "motivation", "relationships"]
                                            }
                                        },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios updateHiddenContenTypes)'
                                    )
        return response

    def get_wave_onboarding_buttons(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'GetWaveOnboardingButtons',
                                        'query':
                                            '''
                                            query GetWaveOnboardingButtons {
                                              wave {
                                                __typename
                                                onboardingButtons {
                                                  __typename
                                                  name
                                                  title
                                                  subcategories {
                                                    __typename
                                                    name
                                                    title
                                                    image_src
                                                  }
                                                }
                                              }
                                            }
                                            ''',
                                        'variables': None
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios GetWaveOnboardingButtons)'
                                    )
        return response

    def get_wave_hidden_content_types(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'GetWaveHiddenContentTypes',
                                        'query':
                                            '''
                                            query GetWaveHiddenContentTypes {
                                              wave {
                                                __typename
                                                hiddenContentTypes {
                                                  __typename
                                                  onboarded
                                                  hiddenContent {
                                                    __typename
                                                    lifestyleNews
                                                    digest
                                                    horoscope
                                                    teaser
                                                  }
                                                }
                                              }
                                            }
                                            ''',
                                        'variables': None
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios GetWaveHiddenContentTypes)'
                                    )
        return response

    def get_available_waves(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'GetAvailableWaves',
                                        'query':
                                            '''
                                            query GetAvailableWaves {
                                              wave {
                                                __typename
                                                availableWaves {
                                                  __typename
                                                  id
                                                  title
                                                  description
                                                  image {
                                                    __typename
                                                    src
                                                  }
                                                }
                                              }
                                            }
                                            ''',
                                        'variables': None
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios GetAvailableWaves)'
                                    )
        return response

    def get_meta(self, play_lists_ids):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "GetMeta",
                                        "query": "query GetMeta($trackIds: [ID!]!, $artistsIds: [ID!]!, $releasesIds: [ID!]!, $playlistsIds: [ID!], $podcastsIds: [ID!]!, $episodesIds: [ID!]!, $booksIds: [ID!]!, $chaptersIds: [ID!]!) {\n  getTracks(ids: $trackIds) {\n    __typename\n    ...TrackAllData\n  }\n  getArtists(ids: $artistsIds) {\n    __typename\n    id\n    title\n    searchTitle\n    description\n    image {\n      __typename\n      src\n      palette\n      paletteBottom\n    }\n    animation {\n      __typename\n      effect\n      image\n    }\n    relatedArtists(limit: 10) {\n      __typename\n      id\n    }\n  }\n  getReleases(ids: $releasesIds) {\n    __typename\n    id\n    title\n    searchTitle\n    type\n    date\n    availability\n    explicit\n    image {\n      __typename\n      src\n      palette\n      paletteBottom\n    }\n    tracks {\n      __typename\n      ...TrackAllData\n    }\n    artists {\n      __typename\n      id\n    }\n  }\n  getPlaylists(ids: $playlistsIds) {\n    __typename\n    ...PlaylistAllData\n  }\n  getPodcasts(ids: $podcastsIds) {\n    __typename\n    id\n    title\n    description\n    updatedDate\n    availability\n    explicit\n    image {\n      __typename\n      src\n      palette\n      paletteBottom\n    }\n    episodes {\n      __typename\n      id\n    }\n  }\n  getEpisodes(ids: $episodesIds) {\n    __typename\n    ...EpisodeAllData\n  }\n  getBooks(ids: $booksIds) {\n    __typename\n    id\n    title\n    description\n    copyright\n    age\n    authorNames\n    availability\n    performer\n    image {\n      __typename\n      src\n      palette\n      paletteBottom\n    }\n    chapters {\n      __typename\n      id\n    }\n    publishers {\n      __typename\n      id\n    }\n  }\n  getChapters(ids: $chaptersIds) {\n    __typename\n    ...ChapterAllData\n  }\n}\nfragment TrackAllData on Track {\n  __typename\n  id\n  title\n  duration\n  searchTitle\n  position\n  availability\n  explicit\n  lyrics\n  hasFlac\n  image {\n    __typename\n    src\n    palette\n    paletteBottom\n  }\n  artists {\n    __typename\n    id\n    title\n  }\n  release {\n    __typename\n    id\n    title\n  }\n}\nfragment PlaylistAllData on Playlist {\n  __typename\n  id\n  title\n  searchTitle\n  updated\n  description\n  isPublic\n  duration\n  userId\n  shared\n  branded\n  buttons {\n    __typename\n    title\n    action {\n      __typename\n      ... on OpenUrlAction {\n        name\n        url\n        fallbackUrl\n        inWebkit\n        auth\n      }\n    }\n  }\n  image {\n    __typename\n    src\n    palette\n    paletteBottom\n  }\n  cover {\n    __typename\n    src\n  }\n  tracks {\n    __typename\n    id\n  }\n}\nfragment EpisodeAllData on Episode {\n  __typename\n  id\n  title\n  description\n  availability\n  duration\n  explicit\n  image {\n    __typename\n    src\n    palette\n    paletteBottom\n  }\n  podcast {\n    __typename\n    id\n  }\n}\nfragment ChapterAllData on Chapter {\n  __typename\n  id\n  title\n  authorNames\n  availability\n  position\n  duration\n  image {\n    __typename\n    src\n    palette\n    paletteBottom\n  }\n  book {\n    __typename\n    id\n    title\n  }\n}",
                                        "variables": {
                                            "artistsIds": [],
                                            "booksIds": [],
                                            "chaptersIds": [],
                                            "episodesIds": [],
                                            "playlistsIds": play_lists_ids,
                                            "podcastsIds": [],
                                            "releasesIds": [],
                                            "trackIds": []
                                        }
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios GetMeta)'
                                    )
        return response

    def get_disliked_collection(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'getDislikedCollection',
                                        'query':
                                            '''
                                            query getDislikedCollection {
                                              hidden_collection {
                                                __typename
                                                tracks {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                                artists {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                              }
                                            }
                                            ''',
                                        'variables': None
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios getDislikedCollection)'
                                    )
        return response

    def get_collection_data(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'getCollectionData',
                                        'query':
                                            '''
                                            query getCollectionData {
                                              collection {
                                                __typename
                                                tracks {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                                playlists {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                                artists {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                                releases {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                                episodes {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                                books {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                                chapters {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                                profiles {
                                                  __typename
                                                  id
                                                  collectionLastModified
                                                }
                                              }
                                            }
                                            ''',
                                        'variables': None
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios getCollectionData)'
                                    )
        return response

    def profiles(self, ids):
        # ["746246625"] ["717993527"]
        # ["506527198", "514072620", "386097314", "438615003", "331771699", "388922123", "371954642", "729177830", "420633244", "669505078", "471759800", "438616750"]
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'Profiles',
                                        'query':
                                            '''
                                            query Profiles($ids: [ID!]!) {
                                              profiles(ids: $ids) {
                                                __typename
                                                id
                                                type
                                                verified
                                                name
                                                description
                                                playlists {
                                                  __typename
                                                  id
                                                }
                                                image {
                                                  __typename
                                                  src
                                                }
                                                additionalData {
                                                  __typename
                                                  ... on CompanyProfileData {
                                                    id
                                                    cover {
                                                      __typename
                                                      src
                                                    }
                                                    banner {
                                                      __typename
                                                      srcMobile
                                                      srcWeb
                                                      link
                                                    }
                                                    site
                                                  }
                                                }
                                              }
                                            }
                                            ''',
                                        'variables': {
                                            'ids': ids
                                        }
                                    },
                                    headers={
                                        # 'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (ios Profiles)'
                                    )
        return response




    #-------WEB----------

    def get_tracks(self, ids, country_code="ru"):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'getTracks',
                                        'variables': {
                                            'withReleases': True,
                                            'withArtists': True,
                                            'ids': ids
                                        },
                                        'query':
                                            """
                                            query getTracks($ids: [ID!]!, $withReleases: Boolean = false, $withArtists: Boolean = false) {
                                                  getTracks(ids: $ids) {
                                                    id
                                                    title
                                                    searchTitle
                                                    position
                                                    duration
                                                    availability
                                                    artistTemplate
                                                    condition
                                                    explicit
                                                    lyrics
                                                    artists @include(if: $withArtists) {
                                                      id
                                                      title
                                                      searchTitle
                                                      description
                                                      hasPage
                                                      image {
                                                        src
                                                        palette
                                                        paletteBottom
                                                      }
                                                      secondImage {
                                                        src
                                                        palette
                                                        paletteBottom
                                                      }
                                                      animation {
                                                        artistId
                                                        effect
                                                        image
                                                        background {
                                                          type
                                                          image
                                                          color
                                                          gradient
                                                        }
                                                      }
                                                    }
                                                    release @include(if: $withReleases) {
                                                      id
                                                      title
                                                      searchTitle
                                                      type
                                                      date
                                                      image {
                                                        src
                                                        palette
                                                        paletteBottom
                                                      }
                                                      genres {
                                                        id
                                                        name
                                                        shortName
                                                      }
                                                      label {
                                                        id
                                                        title
                                                      }
                                                      availability
                                                      artistTemplate
                                                    }
                                                    hasFlac
                                                  }
                                                }
    
                                            """
                                    },
                                    headers={
                                        # 'x-auth-token': token,
                                        'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (getTracks)'
                                    )
        return response

    def playlists(self, country_code="ru"):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'playlists',
                                        'variables': {},
                                        'query':
                                            '''
                                             query playlists {
                                               collection {
                                                 playlists {
                                                   id
                                                   user_id: userId
                                                   last_modified: collectionLastModified
                                                 }
                                               }
                                             }
                                             '''
                                    },
                                    headers={
                                        # 'x-auth-token': token,
                                        'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (playlists)'
                                    )
        return response

    def collection(self, id, country_code="ru"):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'collection',
                                        'variables': {
                                            'id': id,
                                            'type': 'track'
                                        },
                                        'query':
                                            '''
                                            mutation collection($id: ID, $type: CollectionItemType) {
                                              collection {
                                                addItem(id: $id, type: $type)
                                              }
                                            }
                                            '''
                                    },
                                    headers={
                                        # 'x-auth-token': token,
                                        'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (collection)'
                                    )
        return response

    def hidden_collection(self, id, country_code="ru"):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'hiddenCollection',
                                        'variables': {
                                            'id': id,
                                            'type': 'track'
                                        },
                                        'query':
                                            '''
                                            mutation hiddenCollection($id: ID!, $type: CollectionItemType!) {
                                              hidden_collection {
                                                addItem(id: $id, type: $type)
                                              }
                                            }
                                            '''
                                    },
                                    headers={
                                        # 'x-auth-token': token,
                                        'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (hiddenCollection)'
                                    )
        return response

    def user_collection(self, country_code="ru"):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'userCollection',
                                        'variables': {},
                                        'query':
                                            '''
                                             query userCollection {
                                               collection {
                                                 artists {
                                                   id
                                                   last_modified: collectionLastModified
                                                 }
                                                 episodes {
                                                   id
                                                   last_modified: collectionLastModified
                                                 }
                                                 playlists {
                                                   id
                                                   last_modified: collectionLastModified
                                                 }                                                 
                                                 profiles {
                                                   id
                                                   last_modified: collectionLastModified
                                                 }                                                 
                                                 releases {
                                                   id
                                                   last_modified: collectionLastModified
                                                 }
                                                 tracks {
                                                   id
                                                   last_modified: collectionLastModified
                                                 }
                                               }
                                             }
                                             '''
                                    },
                                    headers={
                                        # 'x-auth-token': token,
                                        'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (userCollection)'
                                    )
        return response

    def get_all_hidden_collection(self, country_code="ru"):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'getAllHiddenCollection',
                                        'variables': {},
                                        'query':
                                            '''
                                             query getAllHiddenCollection {
                                               hidden_collection {
                                                 tracks {
                                                   id
                                                   collectionLastModified
                                                 }
                                                 artists {
                                                   id
                                                   collectionLastModified
                                                 }
                                               }
                                             }
                                             '''
                                    },
                                    headers={
                                        # 'x-auth-token': token,
                                        'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (getAllHiddenCollection)'
                                    )
        return response

    def profile(self, ids, country_code="ru"):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'profile',
                                        'variables': {
                                            'ids': ids
                                        },
                                        'query':
                                            '''
                                             query profile($ids: [ID!]!) {
                                               getProfiles(ids: $ids) {
                                                 id
                                                 name
                                                 type
                                                 image {
                                                   src
                                                 }
                                               }
                                             }
                                             '''
                                    },
                                    headers={
                                        # 'x-auth-token': token,
                                        'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (profile)'
                                    )
        return response

    def get_playlists(self, ids, shortTrackList=False, limNumber=3, country_code="ru"):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        'operationName': 'getPlaylists',
                                        'variables': {
                                            'shortTrackList': shortTrackList,
                                            'limNumber': limNumber,
                                            'ids': ids},
                                        'query':
                                            '''
                                            query getPlaylists($ids: [ID!]!, $shortTrackList: Boolean = %s, $limNumber: Int = %i) {
                                              getPlaylists(ids: $ids) {
                                                id
                                                title
                                                search_title: searchTitle
                                                updated
                                                description
                                                image {
                                                  src
                                                  palette
                                                  palette_bottom: paletteBottom
                                                }
                                                tracks @skip(if: $shortTrackList) {
                                                  id
                                                }
                                                ftracks(first: $limNumber) @include(if: $shortTrackList) {
                                                  id
                                                }
                                                buttons {
                                                  title
                                                  action {
                                                    ... on OpenUrlAction {
                                                      name
                                                      url
                                                      fallbackUrl
                                                      inWebkit
                                                      auth
                                                    }
                                                  }
                                                }
                                                branded
                                                cover {
                                                  src
                                                }
                                                is_public: isPublic
                                                isPublic
                                                duration
                                                is_deleted: isDeleted
                                                user_id: userId
                                                shared
                                              }
                                            }
                                        ''' % ('true' if shortTrackList else 'false', limNumber)
                                    },
                                    headers={
                                        # 'x-auth-token': token,
                                        'X-Visitor-Country-Code': country_code,
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql (getPlaylists)'
                                    )
        return response

    def get_playlists_ftracks(self, token, ids, first, country_code="ru"):
        headers = {"X-Auth-token": token, "X-Visitor-Country-Code": country_code}
        query = """
        query {
            getPlaylists(ids:%s) {
                id,
                title,
                userId,
                shared,
                description,
                updated
                image {
                    src,
                    palette,
                    paletteBottom
                },
                duration,
                isDeleted,
                isPublic,
                collectionLastModified,
                chart {
                    trackId,
                    positionChange
                },
                ftracks(first: %i){
                    id,
                    title,
                    image{
                        src,
                        palette,
                        paletteBottom
                    }
                }
            }
        }
        """ % (str(ids), first)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def get_artist(self, ids, token):
        headers = {"X-Auth-token": token}
        query = """
        query {
            getArtists(ids:%s) {
                id,
                title,
                searchTitle,
                description,
                hasPage,
                collectionLastModified
                image {
                    src,
                    palette,
                    paletteBottom
                },
                secondImage {
                    src,
                    palette,
                    paletteBottom
                },
                animation {
                    artistId,
                    image,
                    effect
                    background {
                        image,
                        gradient,
                        type,
                        color
                    }
                },
                releases {
                    id,
                    title,
                    date
                },
                popularTracks {
                    id,
                    title,
                    collectionLastModified
                },
                relatedArtists {
                    id,
                    title,
                    description
                }
            }
        }
        """ % str(ids)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_add(self, id_, item_type, token):
        headers = {"X-Auth-token": token}
        query = """
        mutation {
            collection {
                addItem(id:%s, type:%s)
            }
        }
        """ % (str(id_), item_type)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def get_podcast(self, ids, token):
        headers = {"X-Auth-token": token}
        query = """
        query {
            getPodcasts(ids:%s) {
                id,
                title,
                description,
                link,
                availability,
                completed,
                updatedDate,
                explicit,
                episodes {
                    id,
                    podcast {
                        id,
                        title,
                        description
                    },
                    title,
                    description,
                    image {
                        src,
                        palette,
                        paletteBottom
                    },
                    collectionLastModified
                },
                image {
                    src,
                    palette,
                    paletteBottom
                },
                authors {
                    id,
                    name
                }
            }
        }""" % str(ids)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def get_episode(self, ids, token, season):
        headers = {"X-Auth-token": token}
        query = """
        query {
            getEpisodes(ids:%s, seasons:%s){
                id,
                title,
                description,
                link,
                number,
                publicationDate,
                trackId,
                duration,
                availability,
                explicit,
                collectionLastModified,
                image{
                  src,
                  palette,
                  paletteBottom
                }
                podcast{
                  id,
                  title,
                  image{
                    src,
                    palette,
                    paletteBottom
                  }
                }
                season{
                  id,
                  seasonNumber,
                  name
                }
            }
        }""" % (str(ids), season)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def get_track(self, ids, token):
        headers = {"X-Auth-token": token}
        query = """
        query{
            getTracks(ids:%s){
                id,
                condition,
                title,
                searchTitle,
                title,
                position,
                duration,
                artistTemplate,
                explicit,
                lyrics,
                hasFlac,
                collectionLastModified
                availability
                image{
                    src,
                    palette,
                    paletteBottom
                },
                artists{
                    id,
                    title,
                    image{
                        src,
                        palette,
                        paletteBottom
                    }
                },
                release{
                    id,
                    title,
                    availability,
                    image{
                        src,
                        palette,
                        paletteBottom
                    }
                }
            }
        }
        """ % str(ids)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def get_release(self, ids, token):
        headers = {"X-Auth-token": token}
        query = """
            query{
                getReleases(ids:%s){
                    id,
                    title,
                    explicit,
                    availability,
                    date,
                    artistTemplate,
                    searchTitle,
                    type,
                    collectionLastModified
                    image{
                        src,
                        palette,
                        paletteBottom
                    }
                    label{
                        id,
                        title,
                        searchTitle,
                        description,
                        image{
                            src,
                            palette,
                            paletteBottom
                        },
                        hasImage
                    },
                    related{
                        id,
                        title,
                        searchTitle,
                        availability,
                        explicit,
                        image{
                            src,
                            palette,
                            paletteBottom
                        }
                    },
                    genres{
                        id,
                        parent{
                            id,
                            shortName,
                            sortOrder,
                            visible,
                            name,
                            rname
                        },
                        name,
                        shortName,
                        rname,
                        sortOrder,
                        visible
                    },
                tracks{
                    id,
                    availability,
                    title,
                    explicit,
                    position,
                    artists{
                        id,
                        title
                    }
                },
                artists{
                    id,
                    title
                }
            }
            }
            """ % str(ids)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_playlist_create(self, id_, name, token):
        headers = {"X-Auth-token": token}
        query = """
        mutation{
            playlist {
                create(name: %s, items: [{ type: track, item_id:%s}])
            }
        }
        """ % (name, id_)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_playlist_create_list(self, id_item, id_item2, id_item3, name, token):
        headers = {"X-Auth-token": token}
        query = """
        mutation{
            playlist {
                create(name: %s, items: [{ type: track, item_id:%s}, { type: track, item_id:%s}, { type: track, item_id:%s} ])
            }
        }
        """ % (name, id_item, id_item2, id_item3)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_playlist_add(self, id_, item_type, item_id, token):
        headers = {"X-Auth-token": token}
        query = """
        mutation{
            playlist {
                addItems(id:%s, items:[{type:%s, item_id:%s}])
            }
        }
        """ % (str(id_), item_type, str(item_id))
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_playlist_reorder(self, id_, id_item, token, id_item2, id_item3):
        headers = {"X-Auth-token": token}
        query = """
        mutation{
            playlist {
                reorder(id:%s, items:[{
                    type:track,
                    item_id:%s
                    },
                    {
                    type: track,
                    item_id: %s
                    },
                    {
                    type: track,
                    item_id: %s
                    }
                ])
            }
        }
        """ % (str(id_), id_item, id_item2, id_item3)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_playlist_update(self, id_, item_id, name, is_public, token):
        headers = {"X-Auth-token": token}
        query = """
        mutation{
            playlist {
                update(id: %s, name: %s, items:[{
                type:track, item_id: %s}], isPublic:%s)
            }
        }
        """ % (str(id_), name, item_id, is_public)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_playlist_setpublic(self, id_, token, is_public):
        headers = {"X-Auth-token": token}
        query = """
        mutation{
            playlist {
                setPublic(id: %s, isPublic: %s)
            }
        }
        """ % (str(id_), is_public)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_playlist_rename(self, id_, token, name):
        headers = {"X-Auth-token": token}
        query = """
        mutation{
            playlist {
                rename(id: %s, name: %s)
            }
        }
        """ % (id_, name)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def mutation_playlist_delete(self, id_, token):
        headers = {"X-Auth-token": token}
        query = """
        mutation{
            playlist {
                delete(id: %s)
            }
        }
        """ % str(id_)
        return self.client.post("/graphql/", headers=headers, json={'query': query})

    def get_collection(self, token):
        headers = {"X-Auth-token": token}
        query = """
        query {
            collection {
                tracks {
                    id,
                    title,
                    searchTitle,
                    duration,
                    collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                    }
                }
            releases {
                id,
                title,
                searchTitle,
                collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                    }
            }
            artists {
                id,
                title,
                searchTitle,
                collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                }
            }
            podcasts {
                id,
                title,
                description,
                collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                }
            },
            episodes {
                id,
                title,
                description,
                collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                }
            },
            chapters {
                id,
                title,
                collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                }
            },
            books {
                id,
                title,
                description,
                collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                }
            },
            playlists {
                id,
                description,
                title,
                shared,
                isPublic,
                isDeleted,
                collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                }
            },
            profiles
            {
                id,
                name,
                description,
                isPublicCollection
                collectionItemData{
                        itemStatus,
                        likesCount,
                        lastModified
                }
            }
        }
        }
        """
        return self.client.post("/graphql/", headers=headers, json={'query': query})
