import requests
from configuration import SERVICE_URL_USERS
from src.basecclasses.response_main import ResponseMain


def test_getting_users_list():
    res = requests.get(SERVICE_URL_USERS)
    # print(res.__getstate__())
    test_object = ResponseMain(res)
    test_object.assert_status_code(200)
    # src/schemas/user.py
    # pydantic
    # https://www.youtube.com/watch?v=FfwYEkAraII 11:15