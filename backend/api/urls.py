from django.urls import path, include,re_path
from .views import *
urlpatterns = [
    path('accounts',UserAccountList.as_view()),
    path('rightgroups',RightGroupsList.as_view()),
    path('rights',RightsList.as_view()),
    path('userrights',UserRightsList.as_view())
]
