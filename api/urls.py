from django.urls import path
from .views import UserRecordView, RegistrosViewSet, TagsViewSet

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('registros/', RegistrosViewSet.as_view(), name='registros'),
    path('registros/tag/', TagsViewSet.as_view(), name='tags'),
]