import json
import logging
import time

import gevent.monkey
gevent.monkey.patch_all()

from locust import HttpUser, TaskSet, task, between
#from locust_plugins.csvreader import CSVReader

from client_web import WebUser01, WebUser02
from client_ios import IosUser01
from client_android import AndroidUser01


#user_reader = CSVReader("resources/user_login.csv")


class FlowException(Exception):
    pass


class ZvukUser(HttpUser):
    host = "https://sber-zvuk.com"
    wait_time = between(0.3, 1)
    tasks = [AndroidUser01]
