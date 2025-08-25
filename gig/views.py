from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from gig.interactors.signup_interactor import SignupInteractor
from gig.interactors.login_interactor import LoginInteractor
from gig.interactors.profile_interactor import ProfileInteractor
from gig.presenter.signup_interactor_response import SignupInteractorResponse
from gig.presenter.login_interactor_response import LoginInteractorResponse
from gig.presenter.profile_interactor_response import ProfileInteractorResponse
from gig.storage.user_db import UserDB
from gig.jwt_authentication.jwt_tokens import UserAuthentication, CustomTokenObtainPairSerializer


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup_view(request):
    email = request.data.get("email")
    password = request.data.get("password")
    confirm_password = request.data.get("confirm_password")
    role = request.data.get("role")
    response = SignupInteractor(storage=UserDB(), response=SignupInteractorResponse(),
                                authentication=UserAuthentication()).signup_interactor(email=email, password=password,
                                                                                       confirm_password=confirm_password,
                                                                                       role=role)
    return response


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_view(request):
    email = request.data.get("email")
    password = request.data.get("password")
    response = LoginInteractor(storage=UserDB(), response=LoginInteractorResponse(),
                               authentication=UserAuthentication()).login_interactor(email=email, password=password)
    return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    user_id = request.user.user_id
    role = request.user.role

    response = ProfileInteractor(storage=UserDB(), response=ProfileInteractorResponse(),
                                 authentication=UserAuthentication()).profile_interactor(user_id=user_id, role=role)
    return response
