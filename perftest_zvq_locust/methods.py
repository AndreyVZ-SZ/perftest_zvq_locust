import logging


def log_info(response):
    logging.info(response.request.url)
    logging.info(response.request.headers)
    logging.info(response.request.body)
    logging.info(response.status_code)
    logging.info(response.json())


def check_response(response):
    if response.status_code != 200:
        logging.info("============ " + str(response.status_code) + " ==========")
        logging.info(response.request.headers)
        logging.info(response.request.body)
        logging.info("-----------------------------------")
        logging.info(response.json())


def headers_set_token(self, token):
    self.token = token
    self.client.headers.update({'x-auth-token': self.token,
                                'cookie': 'sauth=' + self.token,
                                'cookie': 'auth=' + self.token
                                })


def headers_set_token_id(self, token, id):
    self.token = token
    self.user_id = id
    self.client.headers.update({'x-auth-token': self.token,
                                'cookie': 'sauth=' + self.token,
                                'cookie': 'auth=' + self.token,
                                'cookie': 'user_id=' + id
                                })


def headers_set_id(self, id):
    self.user_id = id
    self.client.headers.update({'cookie': 'user_id=' + id})


def headers_ios_set_token_id(self, token, id):
    self.token = token
    self.user_id = id
    self.client.headers.update({'x-auth-token': self.token})


def headers_ios_set_token(self, token):
    self.token = token
    self.client.headers.update({'x-auth-token': self.token})
