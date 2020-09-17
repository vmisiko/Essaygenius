from django.urls import path, include
from . import views

app_name = "Home"

urlpatterns = [
    
    path("", views.index, name = "index"),
    path("home/", views.HomePage.as_view(), name = "homepage"),
    path("orderlist/", views.OrderList.as_view(), name = "Orderlist"),
    # path("orderDetail/", views.OrderDetail.as_view(), name = "Orderdetail"),
    path("order/",  views.OrderUpload.as_view(), name = "order"),
    path("orderdetail/", views.OrderdetailApi.as_view(), name = "order"),
    path("orderdetailsdraft/<pk>/", views.OrderdetaildraftApi.as_view(), name="orderdraft"),
    path("instructions/<pk>/", views.OrderIntructionsApi.as_view(), name= "instructions"),
    path("uploads/<pk>/", views.OrderUploadApi.as_view(), name="uploads"),
    path('hello/', views.HelloView.as_view(), name='hello'),
    
]
