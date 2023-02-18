import requests
from configuration import SERVICE_URL
from src.basecclasses.response_main import ResponseMain


def test_getting_posts():
    res = requests.get(url=SERVICE_URL)
    response = ResponseMain(res)
    response.assert_status_code(200)


