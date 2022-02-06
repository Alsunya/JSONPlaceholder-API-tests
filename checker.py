from constants import STATUS_CODE


class Checker:
    @staticmethod
    def check_get_posts(response):
        assert response.status_code == STATUS_CODE.OK.value, f"Status code isn't OK!" \
                                                             f"Actual code is {response.status_code}" \
                                                             f"Actual reason is {response.reason}"
        response = response.json()
        assert len(response) != 0, "The response is empty!"

    @staticmethod
    def check_get_post_with_userid_and_title(response, request):
        assert response.status_code == STATUS_CODE.OK.value, f"Status code isn't OK!" \
                                                             f"Actual code is {response.status_code}" \
                                                             f"Actual reason is {response.reason}"
        response = response.json()
        assert len(response) != 0, "The response is empty!"
        assert response[0]['userId'] == request['userId'], "Request and response user id do not match!"
        assert response[0]['title'] == request['title'], "Request and response title id do not match!"

    @staticmethod
    def check_get_post_with_userid_negative(response):
        assert response.status_code == STATUS_CODE.OK.value, f"Status code isn't OK!" \
                                                             f"Actual code is {response.status_code}" \
                                                             f"Actual reason is {response.reason}"
        response = response.json()
        assert response == [], f"Negative test did not passed!"

    @staticmethod
    def check_get_post_with_title_negative(response):
        assert response.status_code == STATUS_CODE.OK.value, f"Status code isn't OK!" \
                                                             f"Actual code is {response.status_code}" \
                                                             f"Actual reason is {response.reason}"
        response = response.json()
        assert response == [], f"Negative test did not passed!"