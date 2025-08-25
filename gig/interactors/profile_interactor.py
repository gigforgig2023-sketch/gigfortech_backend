from django.http import HttpResponse
from gig.exception import UserNotFoundException
from gig.models import User, FreelancerProfile, ClientProfile
from gig.presenter.profile_interactor_response import ProfileInteractorResponse
from gig.storage.storage_dto import ProfileResponseDTO
from gig.storage.user_db import UserDB
from gig.jwt_authentication.jwt_tokens import UserAuthentication


class ProfileInteractor:
    def __init__(self, storage: UserDB, response: ProfileInteractorResponse, authentication: UserAuthentication):
        self.storage = storage
        self.response = response
        self.authentication = authentication

    def profile_interactor(self, user_id, role):
        try:
            user_data = self.storage.get_user_profile_data(user_id, role)
            return self.response.user_profile_dto_response(user_data)
        except UserNotFoundException:
            return self.response.user_not_found_response()
