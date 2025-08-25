import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class AccessTokenDTO:
    user_id: str
    access_token: str


@dataclass
class RefreshTokenDTO:
    user_id: str
    refresh_token: str


@dataclass
class CreateRefreshTokenDTO:
    access_token: str


@dataclass
class SingUpDTO:
    email: str
    role: str


@dataclass
class SignupResponseDTO:
    access_token: str
    refresh_token: str
    role: str


@dataclass
class LoginResponseDTO:
    access_token: str
    refresh_token: str
    role: str


@dataclass
class ProfileResponseDTO:
    user_id: str
    email: str
    username: str
    role: str
    full_name: str = None
    phone_number: str = None
    location: str = None
    profile_photo_url: str = None
    pan_number: str = None
    govt_id_number: str = None
    dob: str = None
    address: str = None
    state: str = None
    pincode: str = None
    created_at: str = None
    updated_at: str = None
    # Freelancer specific fields
    github_url: str = None
    linkedin_url: str = None
    portfolio_url: str = None
    credits: int = None
    rating_avg: float = None
    earnings_total: str = None
    conversion_rate: str = None
    # Client specific fields
    company_name: str = None
    industry: str = None
    company_size: str = None
    gst_number: str = None
    company_logo_url: str = None
