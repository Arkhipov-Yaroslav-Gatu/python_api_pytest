

from src.basecclasses.response_main import ResponseMain


def test_getting_users_list(get_response):
    ResponseMain(get_response).assert_status_code(200)
