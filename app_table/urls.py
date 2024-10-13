from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as viewstoken
from api import views
from api.views import CustomAuthToken
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
    path('user/register/', views.UserRecordView.as_view(), name='register')
]