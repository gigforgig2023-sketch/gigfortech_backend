from django.db import models
from django.utils import timezone
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_photo_url = models.URLField(blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    govt_id_number = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True, db_index=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"


class FreelancerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="freelancer_profile")
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    credits = models.PositiveIntegerField(default=50)
    rating_avg = models.FloatField(default=0.0, db_index=True)
    earnings_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Freelancer Profile - {self.user.full_name}"


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="client_profile")
    company_name = models.CharField(max_length=255, blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=50, blank=True, null=True)
    gst_number = models.CharField(max_length=50, blank=True, null=True)
    company_logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Client Profile - {self.user.full_name}"


class UserOnboardingStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="onboarding_status")
    steps = models.JSONField(default=dict, help_text="Completed onboarding steps")
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Onboarding - {self.user.full_name} ({'Completed' if self.is_completed else 'In Progress'})"
