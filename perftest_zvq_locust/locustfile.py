import json
import logging
import time
import math

import gevent.monkey

gevent.monkey.patch_all()

from locust import HttpUser, between
from locust import LoadTestShape
# from locust_plugins.csvreader import CSVReader

from client_web import WebUser01
from client_ios import IosUser01
from client_android import AndroidUser01


# user_reader = CSVReader("resources/user_login.csv")


class FlowException(Exception):
    pass


class ZvukUser(HttpUser):
    host = "https://sber-zvuk.com"
    wait_time = between(0.3, 1)
    # tasks = [WebUser01]
    tasks = {
        WebUser01: 1,
        IosUser01: 1,
        AndroidUser01: 1
    }


class StepLoadShape(LoadTestShape):
    """
    A step load shape
    Keyword arguments:
        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds
    """
    step_time = 10
    step_load = 3#12
    spawn_rate = 3
    time_limit = 1200

    def tick(self):
        run_time = self.get_run_time()
        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)
