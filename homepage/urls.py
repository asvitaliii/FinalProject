from django.urls import path
from .views import index, register, sign_in, logout_user, ajax_reg, personal_account

urlpatterns = [
    path('', index, name='home_page'),
    path('register/', register, name='register'),
    path('sign_in/', sign_in, name='sign_in'),
    path('logout/', logout_user, name='logout'),
    path('ajax_reg/', ajax_reg, name='ajax_reg'),
    path('personal_account/', personal_account, name='personal_account'),
]
