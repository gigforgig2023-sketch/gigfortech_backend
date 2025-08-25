import json
from django.http import HttpResponse


class ProfileInteractorResponse:
    @staticmethod
    def user_not_found_response() -> HttpResponse:
        return HttpResponse(json.dumps({
            "error_message": "User not found",
            "status": 404
        }, indent=4), status=404)

    @staticmethod
    def user_profile_dto_response(user_profile_dto) -> HttpResponse:
        return HttpResponse(json.dumps(user_profile_dto, indent=4, default=str), status=200)
