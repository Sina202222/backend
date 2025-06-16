from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        # پیاده‌سازی سفارشی شما
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        
        # Add fields from API registration
        user.phone_number = data.get('phone_number')
        user.date_of_birth = data.get('date_of_birth')
        
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
            
        if commit:
            user.save()
        return user

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # پیاده‌سازی سفارشی شما
        return super().pre_social_login(request, sociallogin)