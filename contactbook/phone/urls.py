
from django.urls import path
from .views import loginview, index, registration, create, contactBookDetail, search, logout_view
urlpatterns = [
    path("login/", loginview, name="loginview"),
    path("", index, name="index"),
    path("logout/", logout_view, name="logout"),
    path("registration/", registration, name="registration"),
    path("create/", create, name="create"),
    path("details/<int:pk>/", contactBookDetail, name="contactBookDetail"),
    path("search/<str:search_term>/", search, name="search")
]
