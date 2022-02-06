import pytest
from http_client import HttpClient
from checker import Checker


def test_get_posts():
    """ Проверка получения постов
    """
    request = f"/posts"
    response = HttpClient().get(path=request)
    Checker.check_get_posts(response)


def test_get_post_with_userid_and_title(post):
    """" Проверка совпадения постов по userId и title в запросе и ответе
    """
    request = f"/posts?userId={post['userId']}&title={post['title']}"
    response = HttpClient().get(path=request)
    Checker.check_get_post_with_userid_and_title(response, post)


@pytest.mark.parametrize("userid_to_request", ["", "-12301", " ", "0", "9999999999999999999"])
def test_get_post_with_userid_negative(userid_to_request):
    """ Негативные тесты на несуществующий userId
    """
    request = f"/posts?userId={userid_to_request}"
    response = HttpClient().get(path=request)
    Checker.check_get_post_with_userid_negative(response)


@pytest.mark.parametrize("title_to_request", ["", " ", "0", "t8///,,!"])
def test_get_post_with_title_negative(title_to_request):
    """ Негативные тесты на несуществующий title
    """
    request = f"/posts?title={title_to_request}"
    response = HttpClient().get(path=request)
    Checker.check_get_post_with_title_negative(response)
