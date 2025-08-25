import json
from textwrap import indent

from django.http import HttpResponse


class SignupInteractorResponse:
    @staticmethod
    def user_already_exists_response() -> HttpResponse:
        return HttpResponse(json.dumps({
            "error_message": "User Already exist",
            "status": 400
        }, indent=4), status=400)

    @staticmethod
    def password_does_not_match() -> HttpResponse:
        return HttpResponse(json.dumps({
            "error_message": "password does not match",
            "status": 400
        }))

    @staticmethod
    def missing_full_name_response() -> HttpResponse:
        return HttpResponse(json.dumps({
            "error_message": "full_name is required",
            "status": 400
        }, indent=4), status=400)

    @staticmethod
    def user_signup_dto_response(user_signup_dto) -> HttpResponse:
        user_signup_dict = {
            "access_token": str(user_signup_dto.access_token),
            "refresh_token": str(user_signup_dto.refresh_token)
        }
        return HttpResponse(json.dumps(user_signup_dict, indent=4), status=200)
