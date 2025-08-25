import json
from django.http import HttpResponse


class LoginInteractorResponse:
    @staticmethod
    def user_not_found_response() -> HttpResponse:
        return HttpResponse(json.dumps({
            "error_message": "User not found",
            "status": 404
        }, indent=4), status=404)

    @staticmethod
    def invalid_password_response() -> HttpResponse:
        return HttpResponse(json.dumps({
            "error_message": "Invalid password",
            "status": 401
        }, indent=4), status=401)

    @staticmethod
    def user_login_dto_response(user_login_dto) -> HttpResponse:
        user_login_dict = {
            "access_token": str(user_login_dto.access_token),
            "refresh_token": str(user_login_dto.refresh_token),
            "role": user_login_dto.role
        }
        return HttpResponse(json.dumps(user_login_dict, indent=4), status=200)
