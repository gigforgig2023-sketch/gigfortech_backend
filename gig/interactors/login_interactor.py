from django.http import HttpResponse
from gig.exception import UserNotFoundException, InvalidPasswordException
from gig.models import User
from gig.presenter.login_interactor_response import LoginInteractorResponse
from gig.storage.storage_dto import LoginResponseDTO
from gig.storage.user_db import UserDB
from gig.jwt_authentication.jwt_tokens import UserAuthentication


class LoginInteractor:
    def __init__(self, storage: UserDB, response: LoginInteractorResponse, authentication: UserAuthentication):
        self.storage = storage
        self.response = response
        self.authentication = authentication

    def login_interactor(self, email, password):
        try:
            user = self.storage.verify_user_credentials(email, password)
            tokens = self.authentication.create_tokens(user)
            user_login_dto = LoginResponseDTO(
                access_token=tokens['access'],
                refresh_token=tokens['refresh'],
                role=user.role
            )
            return self.response.user_login_dto_response(user_login_dto)
        except UserNotFoundException:
            return self.response.user_not_found_response()
        except InvalidPasswordException:
            return self.response.invalid_password_response()
