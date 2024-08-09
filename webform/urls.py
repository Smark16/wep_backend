from  django.urls import path
from . import views

urlpatterns =[
     path('', views.ObtainPairView.as_view()),
     path('register', views.registrationView.as_view()),
     path("all_users", views.AllUsers.as_view()),

    #  background
    path('post_basics', views.post_basic.as_view()),

    # bussiness
    path("post_bussiness", views.post_bussiness.as_view()),

    #trade association
    path("post_trade", views.post_trade.as_view()),

    #women
    path("post_women", views.post_women.as_view()),
]