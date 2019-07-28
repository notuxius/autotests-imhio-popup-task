# from json.decoder import JSONDecodeError
import time
from random import randint

from locust import HttpLocust, TaskSet, task, runners
from locust.log import console_logger
from requests import ReadTimeout, ConnectTimeout


class PopupUserTasks(TaskSet):
    @task
    def post_user_action(self):
        try:
            user_action = randint(0, 10)

            if 0 <= user_action <= 6:
                payload = {"user_action": str(user_action),
                           "feedback": "Load testing Locust {}".format(time.time())}
            else:
                payload = {"user_action": str(user_action),
                           "feedback": ""}

            resp = self.client.request(method="POST",
                                       url="/nps", json=payload, timeout=0.5)

            if resp:
                if resp.status_code != 200:
                    console_logger.error("ERROR: Bad response")
                    console_logger.error(resp.status_code)
                    runners.locust_runner.quit()

        except ConnectTimeout:
            console_logger.error("ERROR: Response connection time is more than 500ms")
            runners.locust_runner.quit()

        except ReadTimeout:
            console_logger.error("ERROR: Response read time is more than 500ms")
            runners.locust_runner.quit()

    # @task
    # def test_rps_time(self):
    #     if 0 < runners.locust_runner.stats.total.current_rps < 5:
    #         console_logger.error("ERROR: RPS is less than 5")
    #         console_logger.error(round(runners.locust_runner.stats.total.current_rps, 1))
    #         runners.locust_runner.quit()
    #
    #     if isinstance(runners.locust_runner.stats.total.get_current_response_time_percentile(0.8), int):
    #         resp_time_80_perc = runners.locust_runner.stats.total.get_current_response_time_percentile(0.8)
    #
    #         if resp_time_80_perc > 450:
    #             console_logger.error("ERROR: 80 percents of response time is more than 450ms")
    #             console_logger.error(resp_time_80_perc)
    #             runners.locust_runner.quit()


class PopupHttpUser(HttpLocust):
    task_set = PopupUserTasks
    host = "http://192.168.99.100:58001"
    # min_wait = 3000
    # max_wait = 3000
    stop_timeout = 60
