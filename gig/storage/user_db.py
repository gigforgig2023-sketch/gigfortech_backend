from django.contrib.auth.hashers import make_password, check_password

from gig.exception import UserAlreadyExistsException, UserNotFoundException, InvalidPasswordException
from gig.models import *
from gig.storage.storage_dto import SingUpDTO


class UserDB:
    def __init__(self):
        pass

    @staticmethod
    def create_user_for_signup(email, password, role):
        if User.objects.filter(email=email).exists():
            raise UserAlreadyExistsException()
        hashed_password = make_password(password)
        user = User.objects.create(username=email, email=email, password=hashed_password, role=role)
        user_signup_dto = SingUpDTO(
            email=user.email,
            role=role
        )
        return user_signup_dto

    @staticmethod
    def verify_user_credentials(email, password):
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return user
            else:
                raise InvalidPasswordException()
        except User.DoesNotExist:
            raise UserNotFoundException()

    @staticmethod
    def get_user_profile_data(user_id, role):
        try:
            user = User.objects.get(user_id=user_id)

            profile_data = {
                "user_id": str(user.user_id),
                "email": user.email,
                "username": user.username,
                "role": user.role,
                "phone_number": user.phone_number,
                "location": user.location,
                "profile_photo_url": user.profile_photo_url,
                "pan_number": user.pan_number,
                "govt_id_number": user.govt_id_number,
                "dob": user.dob.isoformat() if user.dob else None,
                "address": user.address,
                "state": user.state,
                "pincode": user.pincode,
                "created_at": user.created_at.isoformat() if user.created_at else None,
                "updated_at": user.updated_at.isoformat() if user.updated_at else None,
            }

            if role == User.ROLE_FREELANCER:
                try:
                    freelancer_profile = FreelancerProfile.objects.get(user=user)
                    profile_data.update({
                        "github_url": freelancer_profile.github_url,
                        "linkedin_url": freelancer_profile.linkedin_url,
                        "portfolio_url": freelancer_profile.portfolio_url,
                        "credits": freelancer_profile.credits,
                        "rating_avg": freelancer_profile.rating_avg,
                        "earnings_total": str(
                            freelancer_profile.earnings_total) if freelancer_profile.earnings_total else None,
                        "conversion_rate": str(
                            freelancer_profile.conversion_rate) if freelancer_profile.conversion_rate else None,
                    })
                except FreelancerProfile.DoesNotExist:
                    pass

            elif role == User.ROLE_CLIENT:
                try:
                    client_profile = ClientProfile.objects.get(user=user)
                    profile_data.update({
                        "company_name": client_profile.company_name,
                        "industry": client_profile.industry,
                        "company_size": client_profile.company_size,
                        "gst_number": client_profile.gst_number,
                        "company_logo_url": client_profile.company_logo_url,
                    })
                except ClientProfile.DoesNotExist:
                    pass

            return profile_data

        except User.DoesNotExist:
            raise UserNotFoundException()
