import locustfile


class GQL:

    def choose_operation(self):
        pass

    #------Android-------

    def get_public_profile_playlists_with_fixed_covers(self, ids):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "getPublicProfilePlaylistsWithFixedCovers",
                                        "variables": {
                                            "ids": ids,
                                            "first": 3
                                        },
                                        "query": "query getPublicProfilePlaylistsWithFixedCovers($ids: [ID!]!, $first: Int) { playlists(ids: $ids) { __typename ...PlaylistGqlFragment ftracks(first: $first) { __typename id release { __typename image { __typename ...ImageInfoGqlFragment } } } } } fragment PlaylistGqlFragment on Playlist { __typename id title searchTitle updated description image { __typename ...ImageInfoGqlFragment } tracks { __typename id } chart { __typename trackId positionChange } isPublic duration userId ...PlaylistBrandingInfoGqlFragment } fragment PlaylistBrandingInfoGqlFragment on Playlist { __typename id branded cover { __typename src } buttons { __typename title action { __typename ... on OpenUrlAction { name url fallbackUrl inWebkit auth } } } } fragment ImageInfoGqlFragment on ImageInfo { __typename src palette paletteBottom }"
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql'
                                    )
        return response

    def get_playlists_android(self, ids):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "getPlaylists",
                                        "variables": {
                                            "ids": ids
                                        },
                                        "query": "query getPlaylists($ids: [ID!]!) { playlists(ids: $ids) { __typename ...PlaylistGqlFragment } } fragment PlaylistGqlFragment on Playlist { __typename id title searchTitle updated description image { __typename ...ImageInfoGqlFragment } tracks { __typename id } chart { __typename trackId positionChange } isPublic duration userId ...PlaylistBrandingInfoGqlFragment } fragment PlaylistBrandingInfoGqlFragment on Playlist { __typename id branded cover { __typename src } buttons { __typename title action { __typename ... on OpenUrlAction { name url fallbackUrl inWebkit auth } } } } fragment ImageInfoGqlFragment on ImageInfo { __typename src palette paletteBottom }"
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql'
                                    )
        return response

    def wave_content(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "waveContent",
                                        "variables": {
                                            "input": {
                                                "waveId": "3",
                                                "limit": 5,
                                                "localtime": "2022-03-10T15:20:50.199+04:00"
                                            }
                                        },
                                        "query": "query waveContent($input: WaveContentInput!) { wave { __typename waveContent(contentInput: $input) { __typename itemId itemType compilationId sequence skippable content { __typename ... on Track { id } ... on Episode { id } ... on Chapter { id } ... on LifestyleNews { ...LifestyleNewsGqlFragment } ... on Digest { ...DigestGqlFragment } ... on SberZvukDigest { ...SberZvukDigestGqlFragment } ... on Horoscope { ...HoroscopeGqlFragment } ... on Jingle { ...JingleGqlFragment } ... on Teaser { ...TeaserGqlFragment } } } } } fragment LifestyleNewsGqlFragment on LifestyleNews { __typename id title streamId description image { __typename ...ImageInfoGqlFragment } duration availability author explicit publicationDate } fragment ImageInfoGqlFragment on ImageInfo { __typename src palette paletteBottom } fragment DigestGqlFragment on Digest { __typename id title streamId description image { __typename ...ImageInfoGqlFragment } duration availability author explicit publicationDate } fragment SberZvukDigestGqlFragment on SberZvukDigest { __typename id title streamId description image { __typename ...ImageInfoGqlFragment } duration availability author explicit publicationDate } fragment HoroscopeGqlFragment on Horoscope { __typename id title streamId description image { __typename ...ImageInfoGqlFragment } duration availability author explicit publicationDate } fragment JingleGqlFragment on Jingle { __typename id title streamId description image { __typename ...ImageInfoGqlFragment } duration availability author explicit publicationDate } fragment TeaserGqlFragment on Teaser { __typename id title streamId description image { __typename ...ImageInfoGqlFragment } duration availability author explicit publicationDate referenceItemId referenceItemType }"
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql'
                                    )
        return response

    def available_waves(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "availableWaves",
                                        "variables": {},
                                        "query": "query availableWaves { wave { __typename availableWaves { __typename ...WaveGqlFragment } } } fragment WaveGqlFragment on Wave { __typename id title description image { __typename src palette paletteBottom } }"
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql'
                                    )
        return response

    def hidden_content_types(self):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "hiddenContentTypes",
                                        "variables": {},
                                        "query": "query hiddenContentTypes { wave { __typename hiddenContentTypes { __typename ...HiddenContentTypesResponseGqlFragment } } } fragment HiddenContentTypesResponseGqlFragment on HiddenContentTypesResponse { __typename hiddenContent { __typename ...HiddenContentTypesGqlFragment } onboarded } fragment HiddenContentTypesGqlFragment on HiddenContentTypes { __typename digest horoscope lifestyleNews teaser }"
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql'
                                    )
        return response

    def get_profiles(self, ids):
        response = self.client.post("/api/v1/graphql",
                                    json={
                                        "operationName": "getProfiles",
                                        "variables": {"ids": ids},
                                        "query": "query getProfiles($ids: [ID!]!) { profiles(ids: $ids) { __typename ...ProfileGqlFragment } } fragment ProfileGqlFragment on Profile { __typename id type verified name description image { __typename src } playlists { __typename id } additionalData { __typename ... UserProfileDataGqlFragment ... CompanyProfileDataGqlFragment } } fragment UserProfileDataGqlFragment on UserProfileData { __typename id } fragment CompanyProfileDataGqlFragment on CompanyProfileData { __typename site cover { __typename src } banner { __typename srcMobile srcWeb link } }"
                                    },
                                    headers={
                                        'Content-Type': 'application/json'
                                    },
                                    name='/api/v1/graphql'
                                    )
        return response

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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
                                    )
        return response

    def profiles(self, ids):
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
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
                                    name='/api/v1/graphql'
                                    )
        return response


