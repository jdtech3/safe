from locust import HttpUser, task
from bs4 import BeautifulSoup
from decouple import config

class Utils:
    @staticmethod
    def get_csrf_token(html):
        soup = BeautifulSoup(html, features='html.parser')
        csrf = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        
        return csrf

class StudentUser(HttpUser):
    host = config('CSRF_TRUSTED_ORIGIN')
    test_username = config('TEST_USER_USERNAME')
    test_password = config('TEST_USER_PASSWORD')

    @task
    def do_quiz(self):
        login_resp = self.client.get('/evaluate/login/')
        login_data = {
            'csrfmiddlewaretoken': Utils.get_csrf_token(login_resp.text),
            'username': self.test_username,
            'password': self.test_password,
        }
        self.client.post('/evaluate/login/', data=login_data, headers={'Referer': self.host + '/evaluate/login/'})

        quiz_resp = self.client.get('/evaluate/quiz')
        quiz_data = {
            'csrfmiddlewaretoken': Utils.get_csrf_token(quiz_resp.text),
            'q_fire_hazard': 'A',
            'q_env_hazard': 'B',
            'q_fire_extinguisher': 'B',
            'q_pass_acronym': 'B',
            'q_list_ppe': 'first+piece\r\nsecond+piece\r\nthird+piece',
        }
        with self.client.post('/evaluate/quiz/', data=quiz_data, catch_response=True, headers={'Referer': self.host + '/evaluate/quiz/'}) as resp:
            if '4/4' not in resp.text:
                resp.failure('Thanks response incorrect')
