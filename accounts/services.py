import secrets

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User


class AccountService:

    @staticmethod
    def create_account(data: dict) -> User:
        """Create a user account and email them their credentials."""
        password = secrets.token_urlsafe(12)
        user = User.objects.create_user(
            username=data['email'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            matricule=data.get('matricule', ''),
            role=data['role'],
            password=password,
        )
        send_mail(
            subject='Your account has been created',
            message=(
                f'Hello {user.first_name},\n\n'
                f'Your account has been created.\n'
                f'Email: {user.email}\n'
                f'Temporary password: {password}\n\n'
                f'Please log in and change your password.'
            ),
            from_email='noreply@eduapp.com',
            recipient_list=[user.email],
        )
        return user

    @staticmethod
    def login(email: str, password: str) -> dict | None:
        """Authenticate by email and return JWT tokens, or None on failure."""
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        if not user.check_password(password):
            return None
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user': user,
        }

    @staticmethod
    def send_password_reset_email(email: str) -> None:
        """Send a password-reset link if the email belongs to an existing user."""
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return  # silently ignore to prevent email enumeration
        token_generator = PasswordResetTokenGenerator()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        send_mail(
            subject='Password Reset Request',
            message=(
                f'Hello {user.first_name},\n\n'
                f'Use the following credentials to reset your password:\n'
                f'UID: {uid}\n'
                f'Token: {token}'
            ),
            from_email='noreply@eduapp.com',
            recipient_list=[email],
        )

    @staticmethod
    def confirm_password_reset(uid: str, token: str, new_password: str) -> bool:
        """Validate the reset token and set a new password. Returns True on success."""
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, ValueError, OverflowError):
            return False
        token_generator = PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            return False
        user.set_password(new_password)
        user.save()
        return True

    @staticmethod
    def change_password(user: User, old_password: str, new_password: str) -> bool:
        """Verify the old password then update to the new one. Returns True on success."""
        if not user.check_password(old_password):
            return False
        user.set_password(new_password)
        user.save()
        return True
