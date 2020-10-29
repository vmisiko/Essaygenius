from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    
    path("signup/", views.signup, name = "signup"),
    path("user/", views.UserView.as_view(), name="userview")

]
