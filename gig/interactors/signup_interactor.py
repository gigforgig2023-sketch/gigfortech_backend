from django.http import HttpResponse
from gig.exception import UserAlreadyExistsException, PasswordDoesNotMatchException
from gig.models import User
from gig.presenter.signup_interactor_response import SignupInteractorResponse
from gig.storage.storage_dto import SignupResponseDTO
from gig.storage.user_db import UserDB
from gig.jwt_authentication.jwt_tokens import UserAuthentication


class SignupInteractor:
    def __init__(self, storage: UserDB, response: SignupInteractorResponse, authentication: UserAuthentication):
        self.storage = storage
        self.response = response
        self.authentication = authentication

    def signup_interactor(self, email, password, confirm_password, role):
        try:
            if password != confirm_password:
                return self.response.password_does_not_match()
            self.storage.create_user_for_signup(email, password, role)
        except UserAlreadyExistsException:
            return self.response.user_already_exists_response()
        user = User.objects.get(email=email)
        tokens = self.authentication.create_tokens(user)
        user_signup_dto = SignupResponseDTO(
            access_token=tokens['access'],
            refresh_token=tokens['refresh'],
            role=role
        )
        return self.response.user_signup_dto_response(user_signup_dto)
